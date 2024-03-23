import numpy as np
from scipy.stats import t

# Notas dos alunos para cada professor
notas_professores = [
    [82, 64, 64, 79, 64, 76, 52, 61, 85],  # Professor 1
    [64, 88, 79, 67, 85, 100, 82],          # Professor 2
    [73, 91, 82, 85, 82, 67]                # Professor 3
]

# Nível de confiança (em percentual)
confianca = 95

# Número de professores
num_professores = len(notas_professores)

# Função para calcular o intervalo de confiança para a média
def calcular_intervalo_confianca(media, desvio_padrao, tamanho_amostra):
    # Valor crítico da distribuição t de Student para o nível de confiança desejado
    valor_critico = t.ppf((1 + confianca / 100) / 2, tamanho_amostra - 1)
    # Erro padrão da média
    erro_padrao = valor_critico * (desvio_padrao / np.sqrt(tamanho_amostra))
    # Intervalo de confiança
    intervalo_inferior = media - erro_padrao
    intervalo_superior = media + erro_padrao
    return intervalo_inferior, intervalo_superior

# Lista para armazenar os intervalos de confiança de cada professor
intervalos_confianca = []

# Loop para cada professor
for notas_professor in notas_professores:
    # Calcula a média das notas
    media = np.mean(notas_professor)
    # Calcula o desvio padrão amostral
    desvio_padrao = np.std(notas_professor, ddof=1)
    # Tamanho da amostra
    tamanho_amostra = len(notas_professor)
    # Calcula o intervalo de confiança para a média
    intervalo_confianca = calcular_intervalo_confianca(media, desvio_padrao, tamanho_amostra)
    # Adiciona o intervalo de confiança à lista
    intervalos_confianca.append(intervalo_confianca)

# Imprime os intervalos de confiança para cada professor
for i, intervalo in enumerate(intervalos_confianca):
    print(f"Professor {i+1}: Intervalo de Confiança = {intervalo}")
