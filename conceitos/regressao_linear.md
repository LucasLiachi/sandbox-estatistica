# Modelos de Regressão

## Introdução aos Modelos de Regressão Linear

- A regressão linear é uma técnica estatística para modelar a relação entre uma variável dependente (Y) e uma ou mais variáveis independentes (X).

- Existem dois tipos principais:
  - Regressão linear simples: uma variável independente
  - Regressão linear múltipla: duas ou mais variáveis independentes

## Implementação Prática em Python

Foram implementados dois exemplos práticos de regressão linear usando scikit-learn:

### 1. Regressão Linear Simples
- Geração de dados sintéticos com relação linear (y = 2x + 1) e ruído aleatório
- Uso do `LinearRegression()` do scikit-learn para ajuste do modelo
- Visualização gráfica mostrando:
  - Pontos de dados (scatter plot)
  - Linha de regressão ajustada (em vermelho)
  - A relação linear entre uma variável independente (X) e uma dependente (y)

### 2. Regressão Linear Múltipla
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

# Diferenças entre Regressão Simples e Múltipla

## Regressão Linear Simples
- Utiliza apenas uma variável independente (X) para prever a variável dependente (Y)
- Representada pela equação: Y = β₀ + β₁X + ε

## Regressão Linear Múltipla  
- Utiliza duas ou mais variáveis independentes (X₁, X₂, ..., Xₖ) para prever Y
- Representada pela equação: Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + ε

# Representação Matemática e Geométrica

## Representação Matemática
- Regressão simples: Y = β₀ + β₁X + ε
- Regressão múltipla: Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + ε

Onde:
- Y: variável dependente
- X: variável(is) independente(s)  
- β₀: intercepto
- β₁, β₂, ..., βₖ: coeficientes de regressão
- ε: termo de erro aleatório

## Representação Geométrica
- Regressão simples: reta em um plano bidimensional
- Regressão múltipla: plano ou hiperplano em espaço multidimensional

# Pressupostos dos Modelos de Regressão

1. Linearidade: relação linear entre X e Y

2. Independência: observações independentes entre si

3. Homocedasticidade: variância constante dos resíduos

4. Normalidade: distribuição normal dos resíduos

5. Ausência de multicolinearidade: variáveis independentes não altamente correlacionadas entre si

6. Ausência de outliers significativos

7. Tamanho amostral adequado

O cumprimento desses pressupostos é essencial para a validade e confiabilidade do modelo de regressão linear.
