# Regressão Linear Múltipla - Análise de Tempo de Preparo em Restaurante

## Introdução
Este código implementa um modelo de regressão linear múltipla para prever o tempo de preparo de pratos em um restaurante com base em diferentes variáveis.

## Variáveis do Modelo
- **Temperatura** (quantitativa contínua): Temperatura ambiente em °C
- **Promoção** (qualitativa nominal): 0 = sem promoção, 1 = com promoção
- **Número de Funcionários** (quantitativa discreta): Quantidade de funcionários na cozinha
- **Tempo de Preparo** (quantitativa contínua): Tempo em minutos (variável resposta)

## Implementação

### 1. Preparação dos Dados
- Geração de dados sintéticos com 200 amostras
- Variáveis independentes:
  - Temperatura: entre 15°C e 35°C
  - Promoção: valores binários (0 ou 1)
  - Número de funcionários: entre 2 e 8

### 2. Criação do Modelo
- Utilização do LinearRegression do scikit-learn
- Divisão dos dados em treino (80%) e teste (20%)
- Ajuste do modelo aos dados de treino

### 3. Avaliação do Modelo
- Métricas utilizadas:
  - R² (coeficiente de determinação)
  - MSE (erro quadrático médio)
- Visualizações:
  - Gráfico de valores reais vs. previstos
  - Gráfico de resíduos

### 4. Previsões
O modelo permite fazer previsões para novos cenários, fornecendo estimativas do tempo de preparo baseadas nas variáveis de entrada.

## Resultados
O modelo gera:
- Coeficientes para cada variável
- Intercepto do modelo
- Score R² indicando a qualidade do ajuste
- Visualizações para análise de desempenho

## Como Usar
1. Execute o código com os dados desejados
2. Analise os resultados através das métricas e gráficos
3. Use o modelo para fazer previsões com novos dados

## Dependências
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn