import numpy as np
from scipy.stats import t

# Notas dos alunos para cada professor
notas_professores = [
    [82, 64, 64, 79, 64, 76, 52, 61, 85],  # Professor 1
    [64, 88, 79, 67, 85, 100, 82],         # Professor 2
    [73, 91, 82, 85, 82, 67]               # Professor 3
]

def calcular_intervalo_confianca(notas, nivel_confianca=0.95):
    media = np.mean(notas)
    desvio_padrao = np.std(notas, ddof=1)
    tamanho_amostra = len(notas)
    
    t_valor = t.ppf((1 + nivel_confianca) / 2, df=tamanho_amostra - 1)
    erro_padrao = t_valor * (desvio_padrao / np.sqrt(tamanho_amostra))
    
    return media - erro_padrao, media + erro_padrao

# Calcular e exibir os intervalos de confiança
for i, notas in enumerate(notas_professores, 1):
    lim_inferior, lim_superior = calcular_intervalo_confianca(notas)
    print(f"Professor {i}: IC = ({lim_inferior:.2f}, {lim_superior:.2f})")
