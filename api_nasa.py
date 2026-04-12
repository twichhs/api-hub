import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("API_KEY")

url = "https://api.nasa.gov/planetary/apod"
params = {'api_key': key}

response = requests.get(url, params=params)

print("Status:", response.status_code)

try:
    data = response.json()
    print(json.dumps(data, indent=4, ensure_ascii=False))

    image_url = data.get("hdurl") or data.get("url")
    print("URL da imagem:", image_url)

    img = requests.get(image_url).content
    os.makedirs("images", exist_ok=True)

    nome_arquivo = image_url.split("/")[-1]

    caminho = os.path.join("images", nome_arquivo)

    with open(caminho, "wb") as f:
        f.write(img)

    print("Imagem salva em:", caminho)

except Exception as e:
    print("Erro ao converter para JSON!")
    print("Resposta bruta:")
    print(response.text)