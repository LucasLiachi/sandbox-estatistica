import requests
import pandas as pd
import sqlite3
from elasticsearch import Elasticsearch

# Função para criar uma tabela e inserir dados no banco de dados SQLite
def criar_e_inserir_no_banco_de_dados(dados, tabela, conexao):
    df = pd.json_normalize(dados)
    
    # Convertendo todos os dados para string para evitar problemas de tipo
    df = df.apply(lambda x: x.astype(str) if x.notnull().all() else x)
    
    df.to_sql(tabela, conexao, if_exists='replace', index=False)

# Função para requisitar dados da API Elasticsearch
def requisitar_dados_api(url, usuario, senha):
    response = requests.get(url, auth=(usuario, senha))
    response.raise_for_status()
    return [hit['_source'] for hit in response.json()['hits']['hits']]

# Parâmetros da API
url_base = 'https://elasticsearch-saps.saude.gov.br/desc-esus-notifica-estado-*/_search'
usuario = 'user-public-notificacoes'
senha = 'Za4qNXdyQNSa9YaA'

# Conexão com o Elasticsearch utilizando basic_auth em vez de http_auth
es = Elasticsearch(
    ['https://elasticsearch-saps.saude.gov.br'],
    basic_auth=(usuario, senha)
)

# Montagem do corpo da consulta para a API Elasticsearch
query = {
    "query": {
        "match_all": {}
    },
    "size": 10000000  # Defina um valor apropriado conforme a necessidade
}

# Requisição dos dados da API Elasticsearch
dados_notificacoes = requisitar_dados_api(url_base, usuario, senha)

# Criar conexão com o banco de dados SQLite
conexao = sqlite3.connect('3. Database/3.3. Saúde/notificacoes_sindrome_gripal.db')

# Inserir dados no banco de dados
criar_e_inserir_no_banco_de_dados(dados_notificacoes, 'notificacoes_sindrome_gripal', conexao)

# Fechar a conexão
conexao.close()
