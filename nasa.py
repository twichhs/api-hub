import json
import requests
import os
from dotenv import load_dotenv


def main_nasa():
    load_dotenv()
    key = os.getenv("NASA")
    
    if not key:
        print("Erro: API key NASA não configurada no arquivo .env")
        return

    url = "https://api.nasa.gov/planetary/apod"
    params = {'api_key': key}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        print("Status:", response.status_code)

        data = response.json()
        print(json.dumps(data, indent=4, ensure_ascii=False))

        image_url = data.get("hdurl") or data.get("url")
        print("URL da imagem:", image_url)

        if not image_url:
            print("Erro: Nenhuma URL de imagem encontrada na resposta")
            return

        img = requests.get(image_url, timeout=10).content
        os.makedirs("images", exist_ok=True)

        nome_arquivo = image_url.split("/")[-1]
        caminho = os.path.join("images", nome_arquivo)

        with open(caminho, "wb") as f:
            f.write(img)

        print("Imagem salva em:", caminho)

    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP: {e.response.status_code} - {e.response.reason}")
        print("Resposta do servidor:", e.response.text)
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
    except json.JSONDecodeError:
        print("Erro ao converter resposta para JSON!")
        print("Resposta bruta:", response.text)
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main_nasa()