'''
Este código calcula o valor do teste t e o p-valor para comparar duas amostras independentes amostra_A e amostra_B. 
Em seguida, imprime as estatísticas descritivas e a decisão do teste de hipóteses com um nível de significância de 0,05. 
Lembre-se de ajustar os dados de entrada e o nível de significância conforme necessário para o seu problema específico.
'''

import numpy as np # numpy é usado para trabalhar com arrays e realizar operações numéricas.
from scipy import stats #scipy.stats é usado para realizar o teste t de Student.

# Dados das amostras e nível de significancia
amostra_A = np.array([14, 16, 15, 17, 16, 18, 15, 17, 16, 15]) #arrays numpy contendo os dados da amostra A
amostra_B = np.array([18, 20, 19, 21, 20, 22, 19, 21, 20, 19]) #arrays numpy contendo os dados da amostra B
significancia = 0.05  # nível de significância

# Calculando as estatísticas descritivas
media_A = np.mean(amostra_A) # np.mean() é usado para calcular a média das amostras.
media_B = np.mean(amostra_B)
n_A = len(amostra_A) # len() é usado para calcular o tamanho das amostras.
n_B = len(amostra_B)
std_A = np.std(amostra_A, ddof=1)  # np.std() é usado para calcular o desvio padrão das amostras. O parâmetro ddof=1 é usado para calcular o desvio padrão amostral, em vez do desvio padrão populacional.
std_B = np.std(amostra_B, ddof=1)

# Calculando o valor do t e p-valor
t_statistic, p_value = stats.ttest_ind(amostra_A, amostra_B) # stats.ttest_ind() é usado para calcular o teste t de Student para amostras independentes.

# Imprimindo as estatísticas descritivas
print("Estatísticas Descritivas:")
print("Média da Amostra A:", media_A)
print("Média da Amostra B:", media_B)
print("Desvio Padrão da Amostra A:", std_A)
print("Desvio Padrão da Amostra B:", std_B)
print("")

# Imprimindo o valor do t e p-valor
print("Teste de Hipóteses:")
print("Valor de t:", t_statistic)
print("p-valor:", p_value)
if p_value < significancia:
    print("Rejeitamos a hipótese nula: as médias das amostras são estatisticamente diferentes.")
else:
    print("Não rejeitamos a hipótese nula: não há evidências suficientes para afirmar que as médias das amostras são diferentes.")
