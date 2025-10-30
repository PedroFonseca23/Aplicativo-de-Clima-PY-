import requests
import tkinter as tk
from tkinter import messagebox 



def buscar_clima_api(cidade):
    API_KEY = "8d6e73efb63542de160a6dea42e8ee8b" 
    IDIOMA = "pt_br"
    UNIDADE = "metric"
    URL_API = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang={IDIOMA}&units={UNIDADE}"

    try:
        resposta = requests.get(URL_API)
        resposta.raise_for_status() 
        
        dados_clima = resposta.json()
        
       
        clima_principal = dados_clima['main']
        temperatura = clima_principal['temp']
        sensacao_termica = clima_principal['feels_like']
        umidade = clima_principal['humidity']
        descricao_clima = dados_clima['weather'][0]['description']


        return {
            "descricao": descricao_clima.capitalize(),
            "temperatura": f"{temperatura}°C",
            "sensacao": f"Sensação: {sensacao_termica}°C",
            "umidade": f"Umidade: {umidade}%"
        }

    
    except requests.exceptions.HTTPError as http_err:
        if resposta.status_code == 404:
            return {"erro": f"Cidade '{cidade}' não encontrada."}
        elif resposta.status_code == 401:
            return {"erro": "Erro de autenticação. Verifique a API Key."}
        else:
            return {"erro": f"Erro HTTP: {http_err}"}
    except requests.exceptions.ConnectionError:
        return {"erro": "Erro de conexão com a internet."}
    except Exception as e:
        return {"erro": f"Ocorreu um erro: {e}"}


def ao_clicar_buscar():
    cidade = entry_cidade.get() 
    if not cidade:
        messagebox.showwarning("Aviso", "Por favor, digite o nome de uma cidade.")
        return

    label_resultado_desc.config(text=f"Buscando clima para {cidade}...")
   
    label_resultado_temp.config(text="")
    label_resultado_sens.config(text="")
    label_resultado_umid.config(text="")
    
   
    janela.update_idletasks() 

   
    resultado = buscar_clima_api(cidade)

 
    if "erro" in resultado:
 
        messagebox.showerror("Erro", resultado["erro"])
        label_resultado_desc.config(text="Tente novamente.")
    else:
  
        label_resultado_desc.config(text=resultado['descricao'])
        label_resultado_temp.config(text=resultado['temperatura'])
        label_resultado_sens.config(text=resultado['sensacao'])
        label_resultado_umid.config(text=resultado['umidade'])




janela = tk.Tk()
janela.title("Aplicativo de Clima")
janela.geometry("350x300") 
janela.configure(bg="#f0f0f0") 


frame_entrada = tk.Frame(janela, bg="#f0f0f0")
frame_entrada.pack(pady=20) 

label_instrucao = tk.Label(frame_entrada, text="Digite a cidade:", font=("Arial", 12), bg="#f0f0f0")
label_instrucao.pack(side=tk.LEFT, padx=5) 
entry_cidade = tk.Entry(frame_entrada, width=20, font=("Arial", 12))
entry_cidade.pack(side=tk.LEFT)


botao_buscar = tk.Button(janela, text="Buscar Clima", font=("Arial", 12, "bold"), command=ao_clicar_buscar)
botao_buscar.pack(pady=10)


frame_resultados = tk.Frame(janela, bg="#f0f0f0")
frame_resultados.pack(pady=20)

label_resultado_desc = tk.Label(frame_resultados, text="", font=("Arial", 14, "bold"), bg="#f0f0f0")
label_resultado_desc.pack(pady=5)

label_resultado_temp = tk.Label(frame_resultados, text="", font=("Arial", 12), bg="#f0f0f0")
label_resultado_temp.pack(pady=2)

label_resultado_sens = tk.Label(frame_resultados, text="", font=("Arial", 12), bg="#f0f0f0")
label_resultado_sens.pack(pady=2)

label_resultado_umid = tk.Label(frame_resultados, text="", font=("Arial", 12), bg="#f0f0f0")
label_resultado_umid.pack(pady=2)

janela.mainloop()