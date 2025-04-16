'''
Buscaria 3 etapas em que utilizarei o modelo de regressão como base:
1 - Coleta de dados (ou construção de dados fictícios para modelo)
2 - Preparação dos dados
3 - Interpretação dos resultados.

Fiz um exemplo em Python utilizando as bibliotecas
'''
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

np.random.seed(42)
n_samples = 1000
education_levels = np.random.choice(
    ['< Ensino Médio', 'Ensino Médio', 'Ensino Superior', 'Pós-Graduação'],
    size=n_samples,
    p=[0.3, 0.3, 0.25, 0.15] 
)
base_income = 2000
education_effects = {
    '< Ensino Médio': 0,
    'Ensino Médio': 1000,
    'Ensino Superior': 2500,
    'Pós-Graduação': 4000
}

income = np.array([
    education_effects[edu] + base_income + np.random.normal(0, 1000)
    for edu in education_levels
])


df = pd.DataFrame({
    'education': education_levels,
    'income': income
})

'''
2 - Preparação dos dados

Aganizando os dados em uma tabela (chamada DataFrame) com duas colunas: educação do pai e renda familiar.
Criando variáveis especiais chamadas "dummy" para representar cada nível de educação, exceto "menos que ensino médio", que será usado como base de comparação.
'''

dummy_vars = pd.get_dummies(df['education'], prefix='edu', drop_first=True)
X = dummy_vars
y = df['income']

'''
3 - Executando a regressão
usou um método chamado "regressão linear" para analisar como a educação do pai afeta a renda familiar.

'''

model = LinearRegression()
model.fit(X, y)

'''
4 - Interpretação dos resultados
O código mostra vários números importantes:
Coeficientes: Mostram quanto a renda aumenta, em média, para cada nível de educação comparado com "menos que ensino médio".
Intercepto: Representa a renda média para famílias onde o pai tem menos que ensino médio.
R² Score: Indica o quão bem o modelo explica a variação na renda familiar.
Visualizando os resultados
João criou um gráfico de caixas para mostrar visualmente como a renda familiar varia de acordo com a educação do pai.
Análise estatística detalhada
Por fim, João fez uma análise estatística mais aprofundada:
Ele calculou intervalos de confiança para seus resultados.
Determinou p-valores, que indicam o quão confiáveis são os resultados.
Esta análise mostra:
A estimativa para cada nível de educação
O erro padrão, que indica a precisão da estimativa
O valor-t, que ajuda a determinar a significância estatística
O p-valor, que indica a probabilidade de obter esses resultados por acaso
Com essa análise, João pode ter uma ideia mais clara de como a educação do pai está relacionada com a renda familiar e quão confiáveis são suas conclusões.

'''

print("=== Regression Results ===")
print("\nCoefficients:")
for name, coef in zip(X.columns, model.coef_):
    print(f"{name}: {coef:.2f}")
print(f"\nIntercept: {model.intercept_:.2f}")
print(f"R² Score: {model.score(X, y):.4f}")

# Visualize results
plt.figure(figsize=(10, 6))
sns.boxplot(x='education', y='income', data=df)
plt.xticks(rotation=45)
plt.title('Family Income by Father\'s Education Level')
plt.tight_layout()
# Save the figure instead of showing it
plt.savefig('renda-familiar-boxplot.png')
plt.close()

# Calculate confidence intervals and p-values
X_with_const = np.column_stack([np.ones(len(X)), X])
coef = np.append(model.intercept_, model.coef_)
y_pred = model.predict(X)
n = len(y)
p = X_with_const.shape[1]
dof = n - p
mse = np.sum((y - y_pred) ** 2) / dof
var_coef = mse * np.linalg.inv(X_with_const.T @ X_with_const).diagonal()
t_stat = coef / np.sqrt(var_coef)
p_values = 2 * (1 - stats.t.cdf(np.abs(t_stat), dof))

print("\n=== Statistical Analysis ===")
print("\nParameter  Estimate    Std.Error    t-value    p-value")
print("-" * 55)
names = ['Intercept'] + list(X.columns)
for i, name in enumerate(names):
    print(f"{name:10} {coef[i]:10.2f} {np.sqrt(var_coef[i]):10.2f} "
          f"{t_stat[i]:10.2f} {p_values[i]:10.4f}")
    
'''

Coefficients:
edu_Ensino Médio: 1085.52
edu_Ensino Superior: 2415.71
edu_Pós-Graduação: 3908.57

Intercept: 2107.47
R² Score: 0.6558

=== Statistical Analysis ===

Parameter  Estimate    Std.Error    t-value    p-value
-------------------------------------------------------
Intercept     2107.47      55.31      38.10     0.0000
edu_Ensino Médio    1085.52      79.87      13.59     0.0000
edu_Ensino Superior    2415.71      85.03      28.41     0.0000
edu_Pós-Graduação    3908.57      97.15      40.23     0.0000

'''