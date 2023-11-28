import numpy as np
from sklearn.linear_model import LinearRegression

# Dados de entrada
posse_bola = [50, 45, 45, 50, 70, 50, 60, 55, 50, 70]
pontos = [80, 75, 90, 70, 85, 75, 65, 80, 85, 90]

# Cria o modelo de regressão linear
modelo = LinearRegression().fit(np.array(posse_bola).reshape(-1, 1), np.array(pontos))

# Percentual de posse de bola na partida atual
posse_bola_atual = 30

# Faz a previsão dos pontos para o percentual de posse de bola atual
pontos_previstos = modelo.predict(np.array(posse_bola_atual).reshape(-1, 1))

# Apresenta a previsão dos pontos
print(f"Para um percentual de posse de bola de {posse_bola_atual}%, a previsão de pontos é de {pontos_previstos[0]:.2f}")
