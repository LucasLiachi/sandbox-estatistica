import sqlite3
import pandas as pd
import requests

# Função para criar uma tabela e inserir dados no banco de dados SQLite
def criar_e_inserir_no_banco_de_dados(data, tabela, conexao):
    df = pd.DataFrame(data)
    df.to_sql(tabela, conexao, if_exists='replace', index=False)

# URL da API do Banco Central do Brasil (dados da série temporal)
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"

# Fazer a requisição à API do Banco Central
response = requests.get(url)
data = response.json()

# Criar conexão com o banco de dados SQLite
conexao = sqlite3.connect('3. Database/3.4. Economia/bcb_data.db')

# Inserir os dados coletados na tabela 'bcb_series' no banco de dados
criar_e_inserir_no_banco_de_dados(data, 'bcb_series', conexao)

# Fechar a conexão com o banco de dados
conexao.close()

print("Dados salvos no banco de dados 'bcb_data.db' com sucesso!")