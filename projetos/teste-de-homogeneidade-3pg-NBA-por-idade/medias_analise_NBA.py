import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Passo 1: Conectar ao banco de dados SQLite
# Estabelece uma conexão com o banco de dados que contém os dados dos jogadores da NBA.
conexao = sqlite3.connect('Analises/01-medias/medias_NBA_players.db')

# Passo 2: Consulta SQL para obter os dados relevantes
# Seleciona os campos PLAYER_ID, PLAYER_AGE, FG3M (arremessos de 3 pontos convertidos) 
# e FG3A (arremessos de 3 pontos tentados) para análise.
query = """
SELECT PLAYER_ID, PLAYER_AGE, FG3M, FG3A
FROM nba_players_stats
WHERE FG3A > 0  -- Filtra apenas jogadores que tentaram pelo menos um arremesso de 3 pontos.
"""

# Executa a consulta e carrega os resultados em um DataFrame do pandas.
df = pd.read_sql_query(query, conexao)

# Passo 3: Calcular a porcentagem de acertos de arremessos de 3 pontos (FG3_PCT)
# Adiciona uma nova coluna ao DataFrame com a taxa de conversão de arremessos de 3 pontos.
df['FG3_PCT'] = df['FG3M'] / df['FG3A']

# Passo 4: Agrupar jogadores por faixa etária
# Cria uma nova coluna AGE_GROUP que categoriza os jogadores em faixas etárias específicas.
df['AGE_GROUP'] = pd.cut(
    df['PLAYER_AGE'], 
    bins=[0, 23, 27, 31, 100],  # Define os limites das faixas etárias.
    labels=['< 23 anos', '23-27 anos', '28-31 anos', '> 31 anos']  # Nomeia as faixas etárias.
)

# Passo 5: Definir função para calcular o desvio relativo médio
# Essa função calcula o desvio padrão relativo à média para medir a homogeneidade do grupo.
def desvio_relativo_medio(grupo):
    desvios = grupo.std()   # Calcula o desvio padrão.
    medias = grupo.mean()   # Calcula a média.
    return desvios / medias # Retorna o desvio relativo médio.

# Passo 6: Calcular desvios relativos médios por faixa etária
# Agrupa os dados por faixa etária e aplica a função `desvio_relativo_medio` na coluna FG3_PCT.
resultados = (
    df.groupby('AGE_GROUP', observed=True)['FG3_PCT']
    .apply(desvio_relativo_medio)
    .sort_values()  # Ordena os resultados em ordem crescente de desvio relativo médio.
)

# Passo 7: Fechar a conexão com o banco de dados
conexao.close()

# Passo 8: Exibir os resultados no console
print("Homogeneidade dos arremessos de 3 pontos por grupo etário:")
for grupo, valor in resultados.items():
    print(f"{grupo}: {valor:.4f}")

# Passo 9: Criar um gráfico para visualização dos resultados
plt.figure(figsize=(10, 6))  # Define o tamanho do gráfico.
resultados.plot(kind='bar')  # Cria um gráfico de barras com os resultados.
plt.title('Homogeneidade dos Arremessos de 3 Pontos por Grupo Etário')  # Título do gráfico.
plt.xlabel('Grupo Etário')   # Rótulo do eixo X.
plt.ylabel('Desvio Relativo Médio')  # Rótulo do eixo Y.
plt.xticks(rotation=45)      # Rotaciona os rótulos do eixo X para melhor legibilidade.
plt.tight_layout()           # Ajusta automaticamente o layout do gráfico.

# Passo 10: Salvar o gráfico como um arquivo PNG
plt.savefig('Analises/01-medias/homogeneidade_fg3.png')  
print("O gráfico foi salvo como 'homogeneidade_fg3.png'.")
