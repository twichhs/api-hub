import requests


def main_crip(cripto:str = "bitcoin", moeda_preco:str = "brl" ) -> str:
    '''
    cripto exemplos    
    bitcoin  
    ethereum  
    solana  

    moeda_preco exemplos     
    Dolar -> usd
    Real  -> brl
    '''

    url_crip = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": cripto,
        "vs_currencies": moeda_preco,
        "include_24hr_change": "true"
    }

    response = requests.get(url_crip, params=params)

    data = response.json()
    simbolo = {
        "usd" : "$",
        "brl" : "R$",
        "eur" : "€"
    }

    print(f"Cripto: {cripto.upper()}\nValor: {simbolo.get(moeda_preco)}{data[cripto][moeda_preco]}\nTaxa de Variacao(24h): {data[cripto][f"{moeda_preco}_24h_change"]}")


if __name__ == "__main__":
    main_crip(cripto="bitcoin", moeda_preco="eur")