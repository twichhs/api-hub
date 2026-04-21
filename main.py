from pyfiglet import figlet_format
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import IntPrompt, Prompt
from rich.text import Text
from rich.rule import Rule
from gemini_agent import main_run #arquivo
from nasa import main_nasa #arquivo
from cripto import main_crip #arquivo
from countries import main_country # arquivo
import requests
import json
from time import sleep

console = Console()

def show_header():
    console.clear()
    banner = figlet_format("API /HUB", font="big")
    subtitle = Text("Utilize diversas APIs por meio deste hub!", style="bold #9D7CFF")
    console.print(
        Panel.fit(
            f"[bold #6827F5]{banner}[/bold #6827F5]",
            border_style="#30028C",
            title="[bold white]API /HUB[/bold white]",
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


if __name__ == "__main__":
    while True:
        show_header()
        prompt_type = ask_choice(
            "Modo de uso",
            {
                "1": "Chat com Gemini AI",
                "2": "Imagem Astronômica do Dia (NASA)",
                "3": "Preços de Criptocorrências",
                "4": "Informações De Países",
                "0": "Exit",
            },)

        if prompt_type == 1:
            main_run()
            sleep(2)

        if prompt_type == 2:
            main_nasa()
            sleep(2)


        if prompt_type == 3:
            while True:

                cripto = str(input("Cripto/Moeda >> "))
                valor_conversao = str(input("Moeda de Conversão >> "))

                main_crip(cripto , valor_conversao)

                continuar = ask_choice(
                "Modo de uso",
                {
                    "1": "Fazer uma nova cotação",
                    "2": "Voltar ao menu"
                },)

                if continuar == 2:
                    break
        
        if prompt_type == 4:
            pais_c = ask_choice(
            "Modo de uso",
            {
                "1": "País",
                "2": "Lingua"
            },)

            argumento = str(input(">> "))
            main_country(pais_c, argumento)
            sleep(2)


        
        if prompt_type == 0:
            break