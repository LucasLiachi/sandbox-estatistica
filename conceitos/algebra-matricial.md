# Regressão Linear (algebra matricial para determinação de coeficiente)

No exemplo implementado em `algebra-matricial.py`, aplicamos um método para calcular os coeficientes de uma regressão linear utilizando álgebra matricial. O processo segue os seguintes passos:

1. Importar as bibliotecas necessárias (numpy para cálculos e sympy para manipulação matricial)
2. Preparar os dados de entrada (X e Y)
3. Construir as matrizes necessárias para o cálculo
4. Calcular os coeficientes usando a fórmula $$\hat{\beta} = (X'X)^{-1}X'Y$$
5. Avaliar o ajuste do modelo através do R²

A implementação completa pode ser encontrada em `algebra-matricial.py`. Aqui está uma visão geral do processo:

### 1. Bibliotecas e Preparação
Utilizamos numpy para operações numéricas e sympy.matrices para cálculos matriciais específicos.

### 2. Construção das Matrizes
- Matriz X: combina uma coluna de 1's (para o intercepto) com os valores independentes
- Matriz Y: valores dependentes em formato de coluna

### 3. Cálculo dos Coeficientes
Aplicamos a fórmula matricial $$\hat{\beta} = (X'X)^{-1}X'Y$$ onde:
- X' é a transposta de X
- (X'X)^-1 é a inversa do produto de X' e X
- O resultado β contém o intercepto (β0) e o coeficiente angular (β1)

### 4. Avaliação do Modelo
Calculamos o R² para medir a qualidade do ajuste:
- R² = 1 - (SS_res / SS_tot)
- SS_res: soma dos quadrados dos resíduos
- SS_tot: soma total dos quadrados

Para exemplos práticos e a implementação detalhada, consulte o arquivo `algebra-matricial.py`. Este código implementa a regressão linear utilizando álgebra matricial em Python, sem depender de pacotes estatísticos específicos. Ele calcula os coeficientes β0 (intercepto) e β1 (coeficiente angular), bem como o coeficiente de determinação R² para avaliar a qualidade do ajuste do modelo.
