import requests
import json
import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Função para fazer a requisição de dados da API
def requisitar_dados_api(url, parametros={}):
    resposta = requests.get(url, params=parametros)
    objetos = json.loads(resposta.text)
    return objetos['dados']

# Função para criar uma tabela e inserir dados no banco de dados SQLite
def criar_e_inserir_no_banco_de_dados(dados, tabela, conexao):
    if tabela == 'deputado_especifico':
        df = pd.json_normalize(dados)
    else:
        df = pd.DataFrame(dados)
    df.to_sql(tabela, conexao, if_exists='replace', index=False)

# URL base da API
url_api = 'https://dadosabertos.camara.leg.br/api/v2/deputados'

# Criar conexão com o banco de dados SQLite
conexao = sqlite3.connect('db/camara.db')

# Requisição dos dados de todos os deputados
dados_todos_deputados = requisitar_dados_api(url_api)

# Inserir dados de todos os deputados na tabela 'deputados' no banco de dados
criar_e_inserir_no_banco_de_dados(dados_todos_deputados, 'deputados', conexao)

# Requisição dos dados de um deputado específico (utilizando parâmetros)
id_deputado = 204554
parametros_deputado = {'id': id_deputado}
dados_deputado_especifico = requisitar_dados_api(url_api, parametros_deputado)

# Inserir dados do deputado específico na tabela 'deputado_especifico' no banco de dados
criar_e_inserir_no_banco_de_dados(dados_deputado_especifico, 'deputado_especifico', conexao)

# Exemplo: Criar um DataFrame com os dados de todos os deputados a partir do banco de dados
df_todos_deputados_from_db = pd.read_sql_query('SELECT * FROM deputados', conexao)

# Exemplo: Criar um gráfico de contagem de deputados por partido usando seaborn
plt.figure(figsize=(12, 6))
sns.countplot(x='siglaPartido', data=df_todos_deputados_from_db, order=df_todos_deputados_from_db['siglaPartido'].value_counts().index)
plt.title('Contagem de Deputados por Partido')
plt.xlabel('Sigla do Partido')
plt.ylabel('Número de Deputados')
plt.show()

# Fechar a conexão com o banco de dados
conexao.close()
