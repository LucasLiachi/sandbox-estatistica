import requests
import sqlite3
import pandas as pd

# Configurações da API
base_url = "https://servicos-datasus.saude.gov.br"
token_endpoint = "/token"
patient_endpoint = "/fhir/r4/Patient"

# Credenciais de acesso (substitua com suas credenciais reais)
client_id = "your_client_id"
client_secret = "your_client_secret"

# Função para obter o token de acesso
def obter_token(base_url, client_id, client_secret):
    url = base_url + token_endpoint
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise Exception(f"Erro ao obter token: {response.status_code}, {response.text}")

# Função para requisitar dados da API
def requisitar_dados_api(url, token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao acessar a API: {response.status_code}, {response.text}")

# Função para criar uma tabela e inserir dados no banco de dados SQLite
def criar_e_inserir_no_banco_de_dados(dados, tabela, conexao):
    if dados:
        df = pd.json_normalize(dados['entry'])  # 'entry' contém os dados relevantes
        df.to_sql(tabela, conexao, if_exists='replace', index=False)
    else:
        print("Nenhum dado disponível para inserir no banco de dados.")

# Obter o token de acesso
token = obter_token(base_url, client_id, client_secret)

# URL do endpoint de pacientes
patient_url = base_url + patient_endpoint

# Requisição dos dados da API
dados = requisitar_dados_api(patient_url, token)

# Criar conexão com o banco de dados SQLite
conexao = sqlite3.connect('db/rnds_saude.db')

# Nome da tabela
tabela = 'pacientes_covid19'

# Chamar a função para inserir os dados no banco de dados
criar_e_inserir_no_banco_de_dados(dados, tabela, conexao)

# Fechar a conexão com o banco de dados
conexao.close()
