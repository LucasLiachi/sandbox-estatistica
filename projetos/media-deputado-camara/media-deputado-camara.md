# Análise de Deputados da Câmara
# Análise de Deputados da Câmara

Este script Python realiza uma análise dos dados dos deputados da Câmara dos Deputados do Brasil, utilizando a API de Dados Abertos.

## Funcionalidades

### 1. Coleta de Dados (`get_deputies_data`)
- Realiza uma requisição à API da Câmara dos Deputados
- Endpoint utilizado: `https://dadosabertos.camara.leg.br/api/v2/deputados`
- Retorna os dados brutos dos deputados em formato JSON

### 2. Atualização do Banco de Dados (`update_database`)
- Converte os dados recebidos em um DataFrame do Pandas
- Adiciona timestamp da última atualização
- Armazena os dados em um banco SQLite local
- O banco é criado/atualizado no mesmo diretório do script

### 3. Análise dos Dados (`analyze_from_database`)
- Consulta o banco de dados SQLite
- Realiza duas análises principais:
  1. Média de deputados por partido em cada estado
  2. Distribuição total de deputados por partido

### Visualizações Geradas
O script gera dois gráficos:
1. Gráfico de barras mostrando a média de deputados por partido em cada estado
2. Gráfico de barras mostrando o número total de deputados por partido

## Resultados
O script exibe:
- Confirmação da atualização do banco de dados
- Tabela com análise estadual, ordenada pela média de deputados por partido
- Visualizações gráficas dos dados

## Como Executar
Para executar a análise:
1. Certifique-se de ter todas as dependências instaladas
2. Execute o script Python
3. Os gráficos serão exibidos automaticamente
4. Os resultados da análise serão impressos no console

## Dependências
- requests
- pandas
- matplotlib
- seaborn
- sqlite3

## Observações
- O banco de dados é atualizado a cada execução
- Os dados são obtidos em tempo real da API da Câmara
- As visualizações são geradas automaticamente