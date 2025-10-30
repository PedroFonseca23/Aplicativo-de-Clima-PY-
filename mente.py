
import requests
import json

API_KEY = "8d6e73efb63542de160a6dea42e8ee8b"
CIDADE = "Rio De Janeiro" 
IDIOMA = "pt_br"
UNIDADE = "metric"

URL_API = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&lang={IDIOMA}&units={UNIDADE}"

def buscar_clima():
    
    print(f"Buscando clima para: {CIDADE}...\n")

    try:
        
        resposta = requests.get(URL_API)
        resposta.raise_for_status()

        
        dados_clima = resposta.json() 

        clima_principal = dados_clima['main']
        temperatura = clima_principal['temp']
        sensacao_termica = clima_principal['feels_like']
        umidade = clima_principal ['humidity']

        descricao_clima = dados_clima ['weather'][0]['description']

        print("--- Clima Atual ---")
        print(f"Descricao: {descricao_clima.capitalize()}")
        print(f"Temperatura: {temperatura}°C")
        print(f"Sensação Térmica: {sensacao_termica}°C")
        print(f"Umidade: {umidade}%")
        
    except requests.exceptions.HTTPError as http_err:
        if resposta.status_code == 401:
            print("ERRO: Problema de autenticação. Verifique sua API Key.")
        elif resposta.status_code == 404:
            print(f"ERRO: Cidade '{CIDADE}' não encontrada.")
        else:
            print(f"ERRO HTTP: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"ERRO: Problema de conexão com a internet. {conn_err}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    buscar_clima()