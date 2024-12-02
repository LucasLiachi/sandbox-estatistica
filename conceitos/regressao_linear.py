import numpy as np

# Modelos de Regressão
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Exemplo 1: Regressão Linear Simples
np.random.seed(42)
X_simple = np.random.rand(100, 1) * 10
y_simple = 2 * X_simple + 1 + np.random.randn(100, 1)

# Criar e treinar o modelo
model_simple = LinearRegression()
model_simple.fit(X_simple, y_simple)

# Visualizar os resultados
plt.scatter(X_simple, y_simple)
plt.plot(X_simple, model_simple.predict(X_simple), color='red')
plt.title('Regressão Linear Simples')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Exemplo 2: Regressão Linear Múltipla
X_multi = np.random.rand(100, 2) * 10
y_multi = 2 * X_multi[:, 0] + 3 * X_multi[:, 1] + 1 + np.random.randn(100)

# Dividir dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_multi, y_multi, test_size=0.2, random_state=42)

# Criar e treinar o modelo
model_multi = LinearRegression()
model_multi.fit(X_train, y_train)

# Avaliar o modelo
train_score = model_multi.score(X_train, y_train)
test_score = model_multi.score(X_test, y_test)

print("\nRegressão Linear Múltipla:")
print(f"R² (treino): {train_score:.4f}")
print(f"R² (teste): {test_score:.4f}")
print(f"Coeficientes: {model_multi.coef_}")
print(f"Intercepto: {model_multi.intercept_}")