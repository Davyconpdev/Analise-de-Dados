import requests
import pandas as pd
from datetime import datetime

def get_bitcoin_df() -> pd.DataFrame:
    # URL da API com cotações do Bitcoin
    url = "https://api.coinbase.com/v2/prices/spot"

    # Requisição GET
    response = requests.get(url)
    data = response.json()

    # Extraindo dados relevantes
    preco = float(data['data']['amount'])
    ativo = data['data']['base']       
    moeda = data['data']['currency']    
    horario_coleta = datetime.now()

    # Cria DataFrame
    df = pd.DataFrame([{
        'Ativo': ativo,
        'Preco': preco,
        'Moeda': moeda,
        'Horario_coleta': horario_coleta
    }])

    return df

if __name__ == "__main__":
    df = get_bitcoin_df()
    print(df)
    print("✅ Cotação do Bitcoin obtida com sucesso!")