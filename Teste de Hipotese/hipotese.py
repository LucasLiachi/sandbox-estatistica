import pandas as pd
from scipy import stats

# Crie um DataFrame com os dados das marcas
data = {
    'Marca': ['A', 'B', 'C', 'D'],
    'Média de Venda': [20, 12, 17, 15],
    'Desvio Padrão das Vendas': [2, 8, 5, 5],
    'Custo de Compra': [10.0, 14.0, 15.0, 12.0]
}

df = pd.DataFrame(data)

# Realize o teste t-student para cada par de marcas para as médias de vendas
marcas = df['Marca'].tolist()
marcas_escolhidas = []

for i in range(len(marcas)):
    for j in range(i + 1, len(marcas)):
        marca1 = marcas[i]
        marca2 = marcas[j]
        
        media1 = df[df['Marca'] == marca1]['Média de Venda'].values[0]
        media2 = df[df['Marca'] == marca2]['Média de Venda'].values[0]
        
        desvio1 = df[df['Marca'] == marca1]['Desvio Padrão das Vendas'].values[0]
        desvio2 = df[df['Marca'] == marca2]['Desvio Padrão das Vendas'].values[0]
        
        n = 4  # Número de observações
        
        # Calcule a estatística t
        t_statistic = (media1 - media2) / ((desvio1**2/n) + (desvio2**2/n))**0.5
        
        # Calcule os graus de liberdade
        graus_liberdade = 2 * n - 2
        
        # Calcule o p-valor
        p_valor = 2 * (1 - stats.t.cdf(abs(t_statistic), df=graus_liberdade))
        
        # Verifique se o p-valor é menor ou igual a 0.05 (5%)
        if p_valor <= 0.05:
            marcas_escolhidas.extend([marca1, marca2])

# Crie uma nova coluna no DataFrame com as marcas escolhidas
df['Marcas Escolhidas'] = df['Marca'].apply(lambda x: 'Sim' if x in marcas_escolhidas else 'Não')

print(df)

