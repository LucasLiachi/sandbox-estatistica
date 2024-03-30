import numpy as np
import pandas as pd

# Definindo os valores para cada grupo
fundamental = [30.85, 30.34, 24.90, 31.36, 30.14, 30.69, 23.91, 24.07, 25.96, 25.47, 
               33.17, 30.39, 33.49, 27.78, 30.25, 23.73, 27.63, 26.38, 25.24, 26.25, 
               24.28, 31.48, 29.59, 25.97, 31.53, 37.86, 31.44, 28.54, 32.49, 34.11, 
               28.98, 3.58]

medio = [31.01, 25.82, 22.59, 29.66, 26.36, 32.50, 26.27, 26.79, 22.67, 32.11, 
         26.08, 21.49, 25.29, 26.82]

superior = [21.67, 20.39, 28.80, 25.78, 27.88, 25.87, 20.01, 24.83, 21.76, 31.07, 
            24.81, 3.78]

# Calculando a média total de todos os grupos
dados_totais = fundamental + medio + superior
media_total = np.mean(dados_totais)

# Definindo o número de observações em cada grupo
n_fundamental = len(fundamental)
n_medio = len(medio)
n_superior = len(superior)

# Calculando a Soma de Quadrados Total (SQT) com a média amostral geral
sqt = np.sum((dados_totais - media_total)**2)

# Calculando a Soma de Quadrados Dentro do grupo (SQD) para cada grupo individualmente
sqd_fundamental = np.sum((fundamental - np.mean(fundamental))**2)
sqd_medio = np.sum((medio - np.mean(medio))**2)
sqd_superior = np.sum((superior - np.mean(superior))**2)

# Calculando a Soma de Quadrados Entre grupos (SQE)
sqe = sqd_fundamental + sqd_medio + sqd_superior

# Calculando os Graus de Liberdade
df_between = 3 - 1
df_within = len(dados_totais) - 3

# Calculando os Quadrados Médios
qme = sqe / df_between
qmd = sqd_fundamental / (n_fundamental - 1) + sqd_medio / (n_medio - 1) + sqd_superior / (n_superior - 1)

# Criando a tabela de resultados
tabela_anova = pd.DataFrame({
    'Fonte de Variação': ['Entre Grupos', 'Dentro dos Grupos', 'Total'],
    'Soma de Quadrados (SQ)': [sqe, sqd_fundamental + sqd_medio + sqd_superior, sqt],
    'Graus de Liberdade (df)': [df_between, df_within, len(dados_totais) - 1],
    'Quadrados Médios (QM)': [qme, qmd, '-'],
    'Valor F': [qme / qmd, '-', '-']
})

# Exibindo a tabela de resultados
print("Tabela ANOVA:")
print(tabela_anova)
