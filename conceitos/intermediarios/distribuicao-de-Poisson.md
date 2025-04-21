# Distribuição de Poisson - Guia de Cálculo e Implementação

## 1. Conceito e Aplicação
A distribuição de Poisson modela eventos independentes que ocorrem em um intervalo fixo de tempo ou espaço com taxa média constante λ (lambda).

### Aplicações Comuns
- Chegada de clientes em um serviço
- Falhas em equipamentos
- Ocorrências de eventos raros
- Contagem de eventos em intervalos fixos

## 2. Fórmulas Principais

### 2.1 Probabilidade Pontual
Para calcular a probabilidade de exatamente k eventos:
```math
P(X = k) = \frac{e^{-λ}λ^k}{k!}
```

### 2.2 Probabilidade Acumulada
Para calcular a probabilidade de até k eventos:
```math
P(X ≤ k) = \sum_{i=0}^k \frac{e^{-λ}λ^i}{i!}
```

### 2.3 Ajuste do Parâmetro λ
Para ajustar λ para diferentes períodos:
```math
λ_{ajustado} = λ_{base} × \frac{período\_desejado}{período\_base}
```

## 3. Procedimento de Cálculo

### Passo 1: Definição dos Parâmetros
1. Identificar λ (taxa média)
2. Definir k (número de eventos)
3. Determinar o período de interesse

### Passo 2: Ajuste de Lambda
1. Verificar se λ precisa de ajuste para o período
2. Aplicar a fórmula de ajuste se necessário

### Passo 3: Cálculo da Probabilidade
1. Para probabilidade pontual: aplicar fórmula P(X = k)
2. Para probabilidade acumulada: somar P(X = i) de i=0 até k

## 4. Validações e Restrições
- k deve ser um número inteiro não-negativo
- λ deve ser um número positivo
- Período deve estar dentro dos limites válidos (ex: 1-30 dias)

## 5. Exemplos Práticos

### 5.1 Falhas em Equipamentos
- Calcular P(X = k) para falhas em período específico
- Ajustar λ conforme necessário para o período

### 5.2 Fluxo de Passageiros
- Modelar chegadas em terminal
- Calcular probabilidades acumuladas P(X ≤ k)

### 5.3 Caso Detalhado
Cálculo passo a passo de P(X ≤ 2) com λ = 3:
1. P(X = 0) = e⁻³
2. P(X = 1) = 3e⁻³
3. P(X = 2) = 4.5e⁻³
4. P(X ≤ 2) = soma dos anteriores

## 6. Tratamento de Erros
- Validação de tipos de dados
- Verificação de intervalos válidos
- Tratamento de casos extremos

## 7. Referências Técnicas
1. Teoria de Probabilidade
2. Análise de Eventos Discretos
3. Documentação Python (math, scipy.stats)

## 8. Probabilidade Complementar

### 8.1 Conceito
Para eventos onde precisamos calcular a probabilidade de ocorrerem mais do que k eventos, usamos a probabilidade complementar:
```math
P(X > k) = 1 - P(X ≤ k)
```

### 8.2 Fórmula Expandida
```math
P(X > k) = 1 - \sum_{i=0}^k \frac{e^{-λ}λ^i}{i!}
```

### 8.3 Procedimento de Cálculo
1. Calcular P(X ≤ k) usando a soma acumulada
2. Subtrair o resultado de 1
3. Arredondar para 4 casas decimais
4. Converter para percentual se necessário

## 9. Exemplo Prático: Fluxo em Caixa Eletrônico

### 9.1 Descrição do Problema
Analisar a probabilidade de haver mais que k clientes em espera em um caixa eletrônico, 
dado uma taxa média de chegada λ.

### 9.2 Parâmetros do Exemplo
- λ = 1.6 clientes/minuto (taxa média de chegada)
- k = 2 (número máximo aceitável de clientes em espera)
- Objetivo: Calcular P(X > 2)

### 9.3 Resolução Passo a Passo
1. Calcular P(X ≤ 2):
   ```math
   P(X ≤ 2) = e^{-1.6} + 1.6e^{-1.6} + \frac{(1.6)^2e^{-1.6}}{2}
   ```

2. Calcular o complemento:
   ```math
   P(X > 2) = 1 - P(X ≤ 2) = 0.2166
   ```

3. Converter para percentual:
   - 0.2166 → 21.66%

### 9.4 Interpretação
Há uma probabilidade de aproximadamente 21.66% de haver mais que 2 clientes em espera 
no caixa eletrônico em um dado momento, considerando a taxa média de 1.6 clientes 
por minuto.

### 9.5 Aplicações Práticas
- Dimensionamento de filas
- Planejamento de capacidade
- Definição de níveis de serviço
- Otimização de recursos

## 10. Validações Específicas para Probabilidade Complementar

### 10.1 Restrições Adicionais
- Resultado deve estar entre 0 e 1
- Soma de P(X ≤ k) e P(X > k) deve ser igual a 1
- Arredondamento deve preservar a precisão necessária

### 10.2 Casos Especiais
- k = 0: P(X > 0) = 1 - P(X = 0) = 1 - e^{-λ}
- λ muito grande: usar técnicas de aproximação numérica
- k muito grande: considerar aproximação normal

### 10.3 Boas Práticas
- Validar entradas antes do cálculo
- Usar funções matemáticas otimizadas
- Documentar pressupostos e limitações
- Incluir interpretação dos resultados