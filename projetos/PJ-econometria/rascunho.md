# Econometria Aplicada

## Índice
1. [Materiais Relacionados](#materiais-relacionados)
2. [Fundamentos da Regressão Linear](#1-fundamentos-da-regressão-linear)
3. [Modelos de Regressão](#modelos-de-regressão)
4. [Estimação e Validação](#estimação-e-validação)
5. [Implementações Práticas](#implementações-práticas)
6. [Análise e Validação dos Modelos](#análise-e-validação-dos-modelos)
7. [Resolução de Modelos Econométricos em Software](#resolução-de-modelos-econométricos-em-software)

## Materiais Relacionados
### Implementações
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

## Modelos de Regressão
### Diferenças entre Regressão Simples e Múltipla
- Regressão Linear Simples:
  - Uma variável independente (X)
  - Equação: Y = β₀ + β₁X + ε
  - Representa uma reta em plano bidimensional

- Regressão Linear Múltipla:
  - Duas ou mais variáveis independentes
  - Equação: Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + ε
  - Representa um plano ou hiperplano

### Pressupostos dos Modelos
1. Linearidade
2. Independência
3. Homocedasticidade
4. Normalidade
5. Ausência de multicolinearidade
6. Ausência de outliers significativos
7. Tamanho amostral adequado

## Estimação e Validação
### Métodos de Estimação
- Mínimos Quadrados Ordinários (MQO)
- Máxima Verossimilhança (MV)

### Testes Estatísticos
- Teste F (significância geral)
- Teste t (significância individual)
- P-valor e intervalos de confiança
- Análise de variância (ANOVA)

### Diagnósticos
- R² e R² ajustado
- Análise de resíduos
- Testes específicos (Durbin-Watson, White)

### Violação de Hipóteses
- Heteroscedasticidade
- Autocorrelação
- Multicolinearidade
- Não normalidade

## Implementações Práticas
### Processo de Implementação
1. Bibliotecas e Preparação
2. Construção das Matrizes
3. Cálculo dos Coeficientes
4. Avaliação do Modelo

### Exemplos com Python
#### 1. Regressão Linear Simples
- Geração de dados sintéticos
- Uso do LinearRegression()
- Visualização com matplotlib

#### 2. Regressão Linear Múltipla
- Implementação com múltiplas variáveis
- Divisão treino/teste
- Avaliação de performance

## Análise e Validação dos Modelos
### Estimação de Parâmetros
- Método dos Mínimos Quadrados Ordinários (MQO)
- Método da Máxima Verossimilhança (MV)

### Testes de Significância
- Teste F para significância geral do modelo
- Teste t para significância individual dos parâmetros

### Análise dos Parâmetros
- Interpretação dos coeficientes
- Intervalos de confiança
- Erros Tipo I e Tipo II

### Coeficiente de Determinação
- R² e R² ajustado
- Interpretação e limitações

## Resolução de Modelos Econométricos em Software
### Excel e Microsoft Mathematics
- Análise de regressão no Excel
- Interpretação das saídas: R múltiplo, R² ajustado, Erro-padrão, ANOVA

### Software R
- Instalação do R e RStudio
- Implementação de modelos econométricos no R

### Software Gretl
- Introdução ao Gretl
- Importação de dados e realização de regressões
- Interpretação dos resultados

### Variáveis Dummy
- Uso de variáveis dummy em modelos econométricos
- Interpretação de coeficientes de variáveis dummy
- Aplicações práticas (ex: efeitos sazonais, categorias qualitativas)
