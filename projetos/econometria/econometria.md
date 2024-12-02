# Econometria Aplicada

## Materiais Relacionados no Projeto
### Implementações Práticas
- **regressao_linear.py**: Implementação de regressão linear usando álgebra matricial e scikit-learn
  - Inclui exemplos de regressão simples e múltipla
  - Demonstra cálculo de coeficientes usando numpy/sympy
  - Contém visualizações usando matplotlib

### Recursos Adicionais
- Links para artigos e referências: https://revista.gru.ifsp.edu.br/semat/article/download/200/96/1115

## 1. Fundamentos da Regressão Linear
### 1.1 Conceitos Básicos
- Definição e tipos de regressão
- Regressão simples: Y = β₀ + β₁X + ε
- Regressão múltipla: Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + ε

### 1.2 Álgebra Matricial
- Fórmula dos coeficientes: β = (X'X)^(-1)X'Y
- Construção de matrizes
- Implementação com numpy/sympy

## 2. Estimação e Significância
### 2.1 Métodos de Estimação
- Mínimos Quadrados Ordinários (MQO)
- Máxima Verossimilhança (MV)

### 2.2 Testes Estatísticos
- Teste F (significância geral)
- Teste t (significância individual)
- P-valor e intervalos de confiança

## 3. Validação de Modelos
### 3.1 Pressupostos
- Linearidade
- Independência
- Homocedasticidade
- Normalidade
- Multicolinearidade

### 3.2 Diagnósticos
- Análise de resíduos
- R² e R² ajustado
- Testes específicos (Durbin-Watson, White)

## 4. Aplicações Práticas
### 4.1 Implementação
- Python (scikit-learn, statsmodels)
- R e outros softwares estatísticos

### 4.2 Interpretação
- Análise de coeficientes
- Avaliação de modelos
- Aplicações econômicas

## Básico para Regressão Linear (algebra matricial para determinação de coeficiente)

No exemplo implementado em `regressao_linear.py`, aplicamos um método para calcular os coeficientes de uma regressão linear utilizando álgebra matricial. O processo segue os seguintes passos:

1. Importar as bibliotecas necessárias (numpy para cálculos e sympy para manipulação matricial)
2. Preparar os dados de entrada (X e Y)
3. Construir as matrizes necessárias para o cálculo
4. Calcular os coeficientes usando a fórmula $$\hat{\beta} = (X'X)^{-1}X'Y$$
5. Avaliar o ajuste do modelo através do R²

A implementação completa pode ser encontrada em `regressao_linear.py`. Aqui está uma visão geral do processo:

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

Para exemplos práticos e a implementação detalhada, consulte o arquivo `regressao_linear.py`. Este código implementa a regressão linear utilizando álgebra matricial em Python, sem depender de pacotes estatísticos específicos. Ele calcula os coeficientes β0 (intercepto) e β1 (coeficiente angular), bem como o coeficiente de determinação R² para avaliar a qualidade do ajuste do modelo.

## Modelos de Regressão

### Introdução aos Modelos de Regressão Linear

- A regressão linear é uma técnica estatística para modelar a relação entre uma variável dependente (Y) e uma ou mais variáveis independentes (X).

- Existem dois tipos principais:
  - Regressão linear simples: uma variável independente
  - Regressão linear múltipla: duas ou mais variáveis independentes

### Implementação Prática em Python

Foram implementados dois exemplos práticos de regressão linear usando scikit-learn:

#### 1. Regressão Linear Simples
- Geração de dados sintéticos com relação linear (y = 2x + 1) e ruído aleatório
- Uso do `LinearRegression()` do scikit-learn para ajuste do modelo
- Visualização gráfica mostrando:
  - Pontos de dados (scatter plot)
  - Linha de regressão ajustada (em vermelho)
  - A relação linear entre uma variável independente (X) e uma dependente (y)

#### 2. Regressão Linear Múltipla
- Dados sintéticos com duas variáveis independentes (X₁, X₂)
- Relação: y = 2X₁ + 3X₂ + 1 + ruído
- Divisão dos dados em conjuntos de treino (80%) e teste (20%)
- Avaliação do modelo usando R²:
  - R² do conjunto de treino: indica ajuste aos dados de treinamento
  - R² do conjunto de teste: indica capacidade de generalização
- Coeficientes do modelo mostram a influência de cada variável
- Intercepto representa o valor base quando todas variáveis são zero

O código completo pode ser encontrado em `regressao_linear.py`, demonstrando:
- Geração de dados aleatórios controlados (usando `np.random.seed`)
- Implementação prática usando scikit-learn
- Técnicas de visualização com matplotlib
- Avaliação de modelo usando métricas padrão

Esta implementação serve como base para entender:
- Como ajustar modelos de regressão linear
- Como avaliar a qualidade do ajuste
- Como interpretar os resultados em contextos práticos

## Diferenças entre Regressão Simples e Múltipla

### Regressão Linear Simples
- Utiliza apenas uma variável independente (X) para prever a variável dependente (Y)
- Representada pela equação: Y = β₀ + β₁X + ε

### Regressão Linear Múltipla  
- Utiliza duas ou mais variáveis independentes (X₁, X₂, ..., Xₖ) para prever Y
- Representada pela equação: Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + ε

## Representação Matemática e Geométrica

### Representação Matemática
- Regressão simples: Y = β₀ + β₁X + ε
- Regressão múltipla: Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + ε

Onde:
- Y: variável dependente
- X: variável(is) independente(s)  
- β₀: intercepto
- β₁, β₂, ..., βₖ: coeficientes de regressão
- ε: termo de erro aleatório

### Representação Geométrica
- Regressão simples: reta em um plano bidimensional
- Regressão múltipla: plano ou hiperplano em espaço multidimensional

## Pressupostos dos Modelos de Regressão

1. Linearidade: relação linear entre X e Y

2. Independência: observações independentes entre si

3. Homocedasticidade: variância constante dos resíduos

4. Normalidade: distribuição normal dos resíduos

5. Ausência de multicolinearidade: variáveis independentes não altamente correlacionadas entre si

6. Ausência de outliers significativos

7. Tamanho amostral adequado

O cumprimento desses pressupostos é essencial para a validade e confiabilidade do modelo de regressão linear.

## Estimação de Parâmetros

A Aula 2 aborda os seguintes tópicos principais sobre análise e validação de modelos de regressão:

## Estimação de Parâmetros

- Método dos Mínimos Quadrados Ordinários (MQO)
  - Princípios e pressupostos do método
  - Cálculo dos estimadores e resíduos

- Método da Máxima Verossimilhança (MV)
  - Comparação com MQO
  - Vantagens para modelos não-lineares

### Testes de Significância

- Teste F
  - Avalia a significância geral do modelo
  - Cálculo da estatística F e interpretação

- Teste t
  - Avalia a significância individual dos parâmetros
  - Cálculo da estatística t e interpretação

### Análise dos Parâmetros

- Teste de significância (p-valor)
- Intervalos de confiança
- Erros Tipo I e Tipo II

### Coeficiente de Determinação

- R² e R² ajustado
- Interpretação e limitações

Enfatiza a importância desses métodos para validar modelos de regressão, testar hipóteses e avaliar o poder explicativo das variáveis independentes. São apresentados conceitos teóricos e exemplos práticos de cálculo e interpretação das estatísticas.

### Análise e Validação dos Modelos

- Testes de significância (teste F e teste t)
- Análise de variância (ANOVA)
- Coeficiente de determinação (R²)
- Intervalos de confiança
- Teste de significância dos parâmetros (p-valor)

### Violação de Hipóteses

- Heteroscedasticidade
- Autocorrelação serial dos resíduos
- Multicolinearidade  
- Não normalidade dos resíduos
- Testes para detectar violações (ex: Durbin-Watson, White)
- Consequências e possíveis correções

### Aplicações Práticas

- Uso de softwares estatísticos como Excel, R e Gretl
- Exemplos de interpretação de resultados
- Dicas para construção e validação de modelos econométricos

### Implementação Prática em Python

Foram implementados dois exemplos práticos de regressão linear usando scikit-learn:

#### 1. Regressão Linear Simples
- Geração de dados sintéticos com relação linear (y = 2x + 1) e ruído aleatório
- Uso do `LinearRegression()` do scikit-learn para ajuste do modelo
- Visualização gráfica mostrando:
  - Pontos de dados (scatter plot)
  - Linha de regressão ajustada (em vermelho)
  - A relação linear entre uma variável independente (X) e uma dependente (y)

#### 2. Regressão Linear Múltipla
- Dados sintéticos com duas variáveis independentes (X₁, X₂)
- Relação: y = 2X₁ + 3X₂ + 1 + ruído
- Divisão dos dados em conjuntos de treino (80%) e teste (20%)
- Avaliação do modelo usando R²:
  - R² do conjunto de treino: indica ajuste aos dados de treinamento
  - R² do conjunto de teste: indica capacidade de generalização
- Coeficientes do modelo mostram a influência de cada variável
- Intercepto representa o valor base quando todas variáveis são zero

O código completo pode ser encontrado em `regressao_linear.py`, demonstrando:
- Geração de dados aleatórios controlados (usando `np.random.seed`)
- Implementação prática usando scikit-learn
- Técnicas de visualização com matplotlib
- Avaliação de modelo usando métricas padrão

Esta implementação serve como base para entender:
- Como ajustar modelos de regressão linear
- Como avaliar a qualidade do ajuste
- Como interpretar os resultados em contextos práticos

[5] https://revista.gru.ifsp.edu.br/semat/article/download/200/96/1115