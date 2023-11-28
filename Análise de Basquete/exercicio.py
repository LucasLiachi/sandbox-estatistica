import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo
pontos_equipe_a = [60, 70, 80, 90, 100]
pontos_equipe_b = [20, 75, 80, 85, 90]

# Cálculo da média e desvio padrão
media_a = np.mean(pontos_equipe_a)
media_b = np.mean(pontos_equipe_b)
desvio_padrao_a = np.std(pontos_equipe_a)
desvio_padrao_b = np.std(pontos_equipe_b)

# Plot dos pontos
plt.scatter(pontos_equipe_a, pontos_equipe_b)
plt.xlabel('Pontos Equipe A')
plt.ylabel('Pontos Equipe B')

# Cálculo da regressão linear
coeficientes = np.polyfit(pontos_equipe_a, pontos_equipe_b, 1)
funcao_regressao = np.poly1d(coeficientes)
x_regressao = np.linspace(min(pontos_equipe_a), max(pontos_equipe_a), 100)
plt.plot(x_regressao, funcao_regressao(x_regressao), 'r')

# Cálculo da raiz da função usando método da bissecção
def funcao(pontos_a):
    pontos_b = funcao_regressao(pontos_a)
    return pontos_a - pontos_b

a = min(pontos_equipe_a)
b = max(pontos_equipe_a)
tolerancia = 1e-6

while abs(a - b) > tolerancia:
    c = (a + b) / 2
    if funcao(a) * funcao(c) < 0:
        b = c
    else:
        a = c

pontos_equipe_a_raiz = c
pontos_equipe_b_raiz = funcao_regressao(c)

# Plot da raiz da função
plt.scatter(pontos_equipe_a_raiz, pontos_equipe_b_raiz, c='r', marker='x')

plt.show()

print("Pontos Equipe A raiz: ", pontos_equipe_a_raiz)
print("Pontos Equipe B raiz: ", pontos_equipe_b_raiz)