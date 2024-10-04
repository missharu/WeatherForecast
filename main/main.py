import requests
import pandas as pd

# Obtendo dados climáticos da API OpenWeather
def obter_dados_climaticos(cidade, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter dados da cidade {cidade}. Código de erro: {response.status_code}")
        return None

# Exibindo e salvando os dados em CSV
def exibir_dados_climaticos(dados):
    if dados:
        # Extrair dados importantes
        nome_cidade = dados['name']
        data = pd.to_datetime(dados['dt'], unit='s').strftime('%Y-%m-%d %H:%M:%S')
        temperatura = dados['main']['temp']
        umidade = dados['main']['humidity']
        vento = dados['wind']['speed']

        # Exibir no terminal
        print(f"\nDados climáticos de {nome_cidade}:")
        print(f"Data: {data}")
        print(f"Temperatura: {temperatura}°C")
        print(f"Umidade: {umidade}%")
        print(f"Velocidade do vento: {vento} m/s")

        # Salvar em CSV
        dados_climaticos = {
            "Cidade": [nome_cidade],
            "Data": [data],
            "Temperatura (°C)": [temperatura],
            "Umidade (%)": [umidade],
            "Velocidade do vento (m/s)": [vento]
        }

        df = pd.DataFrame(dados_climaticos)
        df.to_csv(f'dados_climaticos_{nome_cidade}.csv', index=False)
        print(f"\nDados salvos em 'dados_climaticos_{nome_cidade}.csv'")

# Chave da API OpenWeather
api_key = "e8e327ab7c5cff80d5ec6976e349a09b"

# Cidade do usuário
cidade_usuario = input("Digite o nome da cidade para obter dados climáticos: ")

# Dados climáticos
dados = obter_dados_climaticos(cidade_usuario, api_key)

# Exibir dados e salvar em CSV
exibir_dados_climaticos(dados)
