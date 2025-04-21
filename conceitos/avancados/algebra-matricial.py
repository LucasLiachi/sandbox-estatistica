import numpy as np

# Dados de exemplo
X = np.array([[1, 1], [1, 2], [1, 3], [1, 4]])  # Matriz de design (com coluna de 1s para o intercepto)
Y = np.array([2, 3, 4, 5])  # Vetor de respostas

# Calcular X transposta
X_t = X.T

# Calcular (X'X)^-1
X_t_X_inv = np.linalg.inv(X_t @ X)

# Calcular os coeficientes
beta = X_t_X_inv @ X_t @ Y

# Extrair os coeficientes
b0, b1 = beta[0], beta[1]

print(f"Intercepto (β0): {b0}")
print(f"Coeficiente angular (β1): {b1}")

## Calcular Y estimado
Y_est = X @ beta

# Calcular o coeficiente de determinação (R²)
SS_tot = np.sum((Y - np.mean(Y)) ** 2)
SS_res = np.sum((Y - Y_est) ** 2)
R2 = 1 - (SS_res / SS_tot)

print(f"Coeficiente de determinação (R²): {R2}")