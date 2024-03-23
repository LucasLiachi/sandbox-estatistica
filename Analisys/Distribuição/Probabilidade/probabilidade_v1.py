import numpy as np
from scipy.stats import t

# Definindo as notas dos alunos para cada professor
notas_professor_1 = np.array([82, 64, 64, 79, 64, 76, 52, 61, 85])
notas_professor_2 = np.array([64, 88, 79, 67, 85, 100, 82])
notas_professor_3 = np.array([73, 91, 82, 85, 82, 67])

# Calculando as médias das notas para cada professor
media_professor_1 = np.mean(notas_professor_1)
media_professor_2 = np.mean(notas_professor_2)
media_professor_3 = np.mean(notas_professor_3)

# Calculando os desvios padrão amostrais para cada professor
desvio_padrao_professor_1 = np.std(notas_professor_1, ddof=1)  # Usamos ddof=1 para calcular o desvio padrão amostral
desvio_padrao_professor_2 = np.std(notas_professor_2, ddof=1)
desvio_padrao_professor_3 = np.std(notas_professor_3, ddof=1)

# Definindo o nível de confiança (95%)
nivel_confianca = 0.95

# Calculando o valor crítico (t) para o nível de confiança desejado e para cada professor
t_valor_professor_1 = t.ppf((1 + nivel_confianca) / 2, df=len(notas_professor_1) - 1)
t_valor_professor_2 = t.ppf((1 + nivel_confianca) / 2, df=len(notas_professor_2) - 1)
t_valor_professor_3 = t.ppf((1 + nivel_confianca) / 2, df=len(notas_professor_3) - 1)

# Calculando o intervalo de confiança para a média de cada professor
intervalo_confianca_professor_1 = t_valor_professor_1 * (desvio_padrao_professor_1 / np.sqrt(len(notas_professor_1)))
intervalo_confianca_professor_2 = t_valor_professor_2 * (desvio_padrao_professor_2 / np.sqrt(len(notas_professor_2)))
intervalo_confianca_professor_3 = t_valor_professor_3 * (desvio_padrao_professor_3 / np.sqrt(len(notas_professor_3)))

# Calculando os limites inferiores e superiores dos intervalos de confiança para cada professor
limite_inferior_professor_1 = media_professor_1 - intervalo_confianca_professor_1
limite_superior_professor_1 = media_professor_1 + intervalo_confianca_professor_1

limite_inferior_professor_2 = media_professor_2 - intervalo_confianca_professor_2
limite_superior_professor_2 = media_professor_2 + intervalo_confianca_professor_2

limite_inferior_professor_3 = media_professor_3 - intervalo_confianca_professor_3
limite_superior_professor_3 = media_professor_3 + intervalo_confianca_professor_3

# Exibindo os resultados
print("Intervalo de confiança para a média do Professor 1:", (limite_inferior_professor_1, limite_superior_professor_1))
print("Intervalo de confiança para a média do Professor 2:", (limite_inferior_professor_2, limite_superior_professor_2))
print("Intervalo de confiança para a média do Professor 3:", (limite_inferior_professor_3, limite_superior_professor_3))