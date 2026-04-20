from google import genai
import os
from dotenv import load_dotenv
from PIL import Image
from pyfiglet import figlet_format
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import IntPrompt, Prompt
from rich.text import Text
from rich.rule import Rule
import json
from datetime import datetime



def main_run():
    load_dotenv()
    key = os.getenv("GEMINI")
    
    if not key:
        print("Erro: API key GEMINI não configurada no arquivo .env")
        return
    
    client = genai.Client(api_key=key)
    console = Console()

    modelo = "gemini-3-flash-preview"
    memoria = "memoria.json"
    LIMITE = 10

    def load_chat():
        if os.path.exists(memoria):
            with open(memoria , "r") as f:
                return json.load(f)
        return []


    def save_chat(new):
        with open(memoria, "w") as fw:
            json.dump(new, fw, indent=2)


    def show_header():
        console.clear()
        banner = figlet_format("GEMINI FLASH", font="big")
        subtitle = Text("Terminal interativo com chat e envio de arquivos", style="bold #9D7CFF")
        console.print(
            Panel.fit(
                f"[bold #6827F5]{banner}[/bold #6827F5]",
                border_style="#07349C",
                title="[bold white]Gemini API[/bold white]",
                subtitle="[bold #00C2FF]Pronto para conversar[/bold #00C2FF]",
                padding=(1, 2),
            )
        )
        console.print(subtitle, justify="center")
        console.print()


    def show_menu(title, options):
        body = "\n".join(f"[bold cyan]{key}[/bold cyan]  {label}" for key, label in options.items())
        console.print(
            Panel(
                body,
                title=f"[bold white]{title}[/bold white]",
                border_style="#355CFF",
                padding=(1, 2),
            )
        )


    def ask_choice(title, options):
        valid_choices = sorted(options.keys())
        show_menu(title, options)
        return IntPrompt.ask(
            "[bold #FFD166]Escolha uma opção[/bold #FFD166]",
            choices=valid_choices,
        )


    def ask_text(label):
        return Prompt.ask(f"[bold #00C2FF]{label}[/bold #00C2FF]").strip()


    def render_response(response_text):
        console.print()
        console.print(Rule("[bold #6827F5]Resposta do Gemini[/bold #6827F5]"))
        console.print(
            Panel(
                Markdown(response_text),
                border_style="#00A896",
                padding=(1, 2),
            )
        )
        console.print()


    def run_chat_with_memory(prompt_text):
        historico_ongoing = load_chat()
        historico_ongoing = historico_ongoing[-LIMITE:]

        while True:
            historico_ongoing.append({
                "role" : "user",
                "parts" : [prompt_text],
                "date" : datetime.now().isoformat()
            })

            historico_para_api = []
            for msg in historico_ongoing:
                historico_para_api.append(
                    genai.types.Content(
                        role=msg["role"],
                        parts=[genai.types.Part(text=part) if isinstance(part, str) else part for part in msg["parts"]]
                    )
                )

            response_gemini = client.models.generate_content(
                model=modelo, # gemini-2.5-flash
                contents=historico_para_api,
            )

            historico_ongoing.append({
                "role" : "model",
                "parts" : [response_gemini.text],
                "date" : datetime.now().isoformat()
            })
            historico_ongoing = historico_ongoing[-LIMITE:]
            save_chat(historico_ongoing)

            render_response(response_gemini.text)
            continue_chat = ask_choice(
                "Conversa continua",
                {
                    "1": "Enviar outra mensagem",
                    "2": "Voltar ao menu principal",
                },
            )

            if continue_chat == 2:
                return

            while True:
                prompt_text = ask_text("Digite sua proxima mensagem")
                if prompt_text:
                    break
                console.print("[bold red]A mensagem nao pode ficar vazia.[/bold red]")


    while True:
            show_header()
            prompt_type = ask_choice(
                "Modo de uso",
                {
                    "1": "Chat",
                    "2": "Chat com arquivo",
                    "3": "Sair",
                },
            )

            if prompt_type == 3:
                console.print("[bold #7BD389]Sessao encerrada.[/bold #7BD389]")
                break

            prompt_memory = ask_choice(
                "Estilo da conversa",
                {
                    "1": "Prompt unico sem memoria",
                    "2": "Continuar conversa com memoria",
                },
            )

            prompt_model = ask_choice(
                "Modelo",
                {
                    "1": "Gemini 3 Flash",
                    "2": "Gemini 2.5 Flash"
                }

            )

            if prompt_model == 2:
                modelo = "gemini-2.5-flash"

            prompt_text = ask_text(">> ")
            if not prompt_text:
                console.print("[bold red]O prompt nao pode ficar vazio.[/bold red]")
                Prompt.ask("[dim]Pressione Enter para continuar[/dim]", default="")
                continue

            if prompt_type == 2:
                prompt_content_path = ask_text("Informe o caminho do arquivo")
                if not os.path.exists(prompt_content_path):
                    console.print(f"[bold red]Arquivo nao encontrado:[/bold red] {prompt_content_path}")
                    Prompt.ask("[dim]Pressione Enter para continuar[/dim]", default="")
                    continue

            if prompt_type == 1:
                if prompt_memory == 2:
                    run_chat_with_memory(prompt_text)
                    continue
                else:
                    response_gemini = client.models.generate_content(
                        model= modelo,
                        contents= prompt_text,
                    )

            if prompt_type == 2:
                content_type = ask_choice(
                    "Tipo de arquivo",
                    {
                        "1": "Imagem",
                        "2": "Documento",
                    },
                )
                
                if content_type == 1:
                    image = Image.open(prompt_content_path)
                    response_gemini = client.models.generate_content(
                    model=modelo,
                    contents=[image, prompt_text]
                    )

                if content_type == 2:
                    myfile = client.files.upload(file=prompt_content_path)

                    response_gemini = client.models.generate_content(
                    model=modelo,
                    contents=[prompt_text, myfile]
                    )


                # Usar o código abaixo para imagens grandes
                # my_file = client.files.upload(file="path/to/sample.jpg")

            render_response(response_gemini.text)
            Prompt.ask("[dim]Pressione Enter para voltar ao menu[/dim]", default="")


if __name__ == "__main__":
    main_run()
