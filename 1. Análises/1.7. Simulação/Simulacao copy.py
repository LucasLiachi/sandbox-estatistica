import numpy as np
import matplotlib.pyplot as plt

# Simulação dos pedidos de refrigerante A ao longo de uma semana (7 dias)
np.random.seed(42)  # Para garantir reproducibilidade dos resultados

# Gerar os números de pedidos para cada dia da semana (simulando uma distribuição)
pedidos_por_dia = np.random.poisson(lam=2, size=7)  # Média de 2 pedidos por dia

# Histograma das ocorrências dos números de pedidos
plt.figure(figsize=(8, 5))
plt.hist(pedidos_por_dia, bins=np.arange(min(pedidos_por_dia), max(pedidos_por_dia) + 1.5) - 0.5, edgecolor='black', alpha=0.7)
plt.xticks(np.arange(min(pedidos_por_dia), max(pedidos_por_dia) + 1))
plt.xlabel('Número de Pedidos por Dia')
plt.ylabel('Frequência')
plt.title('Histograma de Pedidos de Refrigerante A por Dia')
plt.grid(True)
plt.show()

# Expectativa da ocorrência dos números (média dos pedidos)
expectativa = np.mean(pedidos_por_dia)
print(f'Expectativa de pedidos por dia: {expectativa:.2f}')

# Probabilidade da ocorrência dos elementos
total_dias = len(pedidos_por_dia)
probabilidade = pedidos_por_dia / total_dias
print('Probabilidade de pedidos por dia:')
for dia, prob in enumerate(probabilidade, start=1):
    print(f'Dia {dia}: {prob:.2f}')

# Universo de casos analisados
print(f'Número total de dias analisados: {total_dias}')
