import sqlite3
import pandas as pd
import requests
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

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

# Carregar os dados para análise
df = pd.read_sql_query("SELECT * FROM bcb_series", conexao)

# Fechar a conexão com o banco de dados
conexao.close()

# Converter coluna 'data' para datetime e 'valor' para float (se necessário)
df['data'] = pd.to_datetime(df['data'])
df['valor'] = pd.to_numeric(df['valor'], errors='coerce')

# Análise descritiva dos dados
print("Resumo Estatístico:")
print(df.describe())

# Visualização da série temporal
plt.figure(figsize=(10, 6))
plt.plot(df['data'], df['valor'], label='Série Temporal')
plt.xlabel('Data')
plt.ylabel('Valor')
plt.title('Série Temporal - Banco Central')
plt.legend()
plt.show()

# Exemplo de Regressão Linear Simples (usando valores fictícios)
# Nota: Substitua 'variavel_independente' e 'variavel_dependente' pelos nomes corretos das colunas

# Criando variáveis fictícias para demonstração (ajuste conforme necessário)
df['variavel_independente'] = range(len(df))  # Exemplo: índice temporal como variável independente
df['variavel_dependente'] = df['valor']      # Exemplo: valor como variável dependente

X = df['variavel_independente'].values.reshape(-1, 1)  # Variável independente
y = df['variavel_dependente'].values                  # Variável dependente

modelo = LinearRegression()
modelo.fit(X, y)

print("\nResultados da Regressão Linear Simples:")
print("Intercepto:", modelo.intercept_)
print("Coeficiente:", modelo.coef_)

# Predições e visualização do ajuste do modelo
y_pred = modelo.predict(X)

plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Dados Reais')
plt.plot(X, y_pred, color='red', label='Ajuste do Modelo')
plt.xlabel('Variável Independente (Exemplo)')
plt.ylabel('Variável Dependente (Exemplo)')
plt.title('Regressão Linear Simples')
plt.legend()
plt.show()