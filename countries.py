import requests


def main_country(requests_type: int , par:str):
    '''
    1 = PAIS  
    2 = LINGUA
    '''
    url_pais = "https://restcountries.com/v3.1/name/"
    url_linguagem = "https://restcountries.com/v3.1/lang/"

    par = par.lower()

    if requests_type == 1:
        response = requests.get(url=url_pais + par)

        if response.status_code != 200:
            print("Erro na requisição!")
        else:
            data = response.json()[0]

            resultado = f"""
    ========================
    País       : {data["name"]["common"]}
    Capital    : {data.get("capital", ["N/A"])[0]}
    População  : {data.get("population", 0):,}
    Moeda      : {list(data.get("currencies", {}).keys())[0]}
    ========================
    """

            print(f"Request code: {response.status_code}")
            print(resultado)



    elif requests_type == 2:
        response = requests.get(url=url_linguagem + par)

        if response.status_code != 200:
            print("Erro na requisição!")
        else:
            data = response.json()

            print(f"\nTotal de países encontrados: {len(data)}\n")

            resultado = ""

            for pais in data[:10]:
                nome = pais["name"]["common"]
                capital = pais.get("capital", ["N/A"])[0]
                populacao = f"{pais.get('population', 0):,}".replace(",", ".")
                moeda = list(pais.get("currencies", {}).keys())

                resultado += f"""
    ========================
    País       : {nome}
    Capital    : {capital}
    População  : {populacao}
    Moeda      : {", ".join(moeda) if moeda else "N/A"}
    ========================
    """

            print(resultado)

    else:
        print("Opção inválida!")