import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Definir backend não interativo
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# Criando dados fictícios
np.random.seed(42)
metros_quadrados = np.random.randint(30, 200, 100)
aluguel = 1000 + 20 * metros_quadrados + np.random.normal(0, 500, 100)

# Criando um DataFrame
df = pd.DataFrame({'metros_quadrados': metros_quadrados, 'aluguel': aluguel})

# Dividindo os dados em treino e teste
X = df[['metros_quadrados']]
y = df['aluguel']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando e treinando o modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Fazendo previsões
y_pred = modelo.predict(X_test)

# Avaliando o modelo
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"Coeficiente (inclinação): {modelo.coef_[0]:.2f}")
print(f"Intercepto: {modelo.intercept_:.2f}")
print(f"R² Score: {r2:.2f}")
print(f"Erro Quadrático Médio: {mse:.2f}")

# Visualizando os resultados
plt.figure(figsize=(10, 6))  # Definir tamanho da figura
plt.scatter(X, y, color='blue', alpha=0.5)
plt.plot(X, modelo.predict(X), color='red', linewidth=2)
plt.xlabel('Metros Quadrados')
plt.ylabel('Valor do Aluguel')
plt.title('Regressão Linear: Metros Quadrados vs. Valor do Aluguel')

# Criar diretório se não existir
os.makedirs('analise-aluguel', exist_ok=True)

# Salvando o gráfico
plt.savefig('projetos/analise-aluguel/regressao_aluguel.png')
plt.close()  # Liberar memória

# Função para prever aluguel
def prever_aluguel(metros):
    return modelo.predict([[metros]])[0]

# Exemplo de uso
metros_exemplo = 100
aluguel_previsto = prever_aluguel(metros_exemplo)
print(f"Aluguel previsto para {metros_exemplo}m²: R${aluguel_previsto:.2f}")