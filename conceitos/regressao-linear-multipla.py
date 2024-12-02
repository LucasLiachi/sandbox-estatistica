import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# 1. Generate synthetic data
n_samples = 200
temperatura = np.random.uniform(15, 35, n_samples)
promocao = np.random.randint(0, 2, n_samples)
num_funcionarios = np.random.randint(2, 8, n_samples)

# Create target variable with some realistic relationships
tempo_preparo = (
    20 +  # base time
    0.3 * temperatura +  # temperature effect
    -5 * promocao +  # promotion effect (speeds up preparation)
    -2 * num_funcionarios +  # more staff reduces time
    np.random.normal(0, 2, n_samples)  # random noise
)

# Create DataFrame
data = pd.DataFrame({
    'Temperatura': temperatura,
    'Promocao': promocao,
    'Num_Funcionarios': num_funcionarios,
    'Tempo_Preparo': tempo_preparo
})

# 2. Create and train the model
X = data[['Temperatura', 'Promocao', 'Num_Funcionarios']]
y = data['Tempo_Preparo']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# 3. Model evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Results:")
print(f"Coeficientes: {dict(zip(X.columns, model.coef_))}")
print(f"Intercepto: {model.intercept_:.2f}")
print(f"R² Score: {r2:.3f}")
print(f"MSE: {mse:.3f}")

# 4. Visualize results
plt.figure(figsize=(12, 4))

# Actual vs Predicted plot
plt.subplot(121)
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Tempo Real')
plt.ylabel('Tempo Previsto')
plt.title('Valores Reais vs. Previstos')

# Residual plot
plt.subplot(122)
residuals = y_test - y_pred
plt.scatter(y_pred, residuals, alpha=0.5)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Previsões')
plt.ylabel('Resíduos')
plt.title('Gráfico de Resíduos')

plt.tight_layout()
plt.show()

# 5. Make predictions with new data
novo_cenario = pd.DataFrame({
    'Temperatura': [25, 30, 20],
    'Promocao': [0, 1, 0],
    'Num_Funcionarios': [4, 6, 3]
})

previsoes = model.predict(novo_cenario)
print("\nPrevisões para novos cenários:")
for i, prev in enumerate(previsoes):
    print(f"Cenário {i+1}: {prev:.2f} minutos")