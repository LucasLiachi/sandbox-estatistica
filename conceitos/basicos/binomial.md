# Distribuição Binomial

## Definição

A distribuição binomial é um modelo probabilístico discreto que descreve o número de sucessos em uma sequência de n tentativas independentes (também chamadas de ensaios de Bernoulli), onde cada tentativa tem apenas dois resultados possíveis: sucesso (com probabilidade p) ou fracasso (com probabilidade 1-p).

## Contexto

A distribuição binomial é usada em situações onde:
- Temos um número fixo de tentativas (n)
- Cada tentativa é independente das demais
- Cada tentativa tem apenas dois resultados possíveis (sucesso/fracasso)
- A probabilidade de sucesso (p) é constante em todas as tentativas

## Fórmula

A probabilidade de se obter exatamente k sucessos em n tentativas é dada por:

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

Onde:
- $n$ é o número de tentativas
- $k$ é o número de sucessos
- $p$ é a probabilidade de sucesso em cada tentativa
- $\binom{n}{k}$ é o coeficiente binomial, dado por $\frac{n!}{k!(n-k)!}$

## Propriedades

- **Média (Valor Esperado)**: $\mu = n \times p$
- **Variância**: $\sigma^2 = n \times p \times (1-p)$
- **Desvio Padrão**: $\sigma = \sqrt{n \times p \times (1-p)}$
- **Função Massa de Probabilidade (PMF)**: $P(X = k)$
- **Função de Distribuição Acumulada (CDF)**: $P(X \leq k)$
- **Função de Sobrevivência (SF)**: $P(X > k)$

## Exemplos de Aplicação

### Exemplo 1: Lançamento de Moeda
Ao lançar uma moeda justa 5 vezes, qual é a probabilidade de obter exatamente 3 caras?

- n = 5 (tentativas)
- k = 3 (sucessos desejados)
- p = 0.5 (probabilidade de cara em cada lançamento)

Aplicando a fórmula:
$$P(X = 3) = \binom{5}{3} (0.5)^3 (0.5)^{5-3} = 10 \times 0.125 \times 0.25 = 0.3125$$

### Exemplo 2: Controle de Qualidade
Em uma linha de produção, 5% das peças são defeituosas. Ao selecionar aleatoriamente 20 peças, qual é a probabilidade de encontrar no máximo 2 peças defeituosas?

- n = 20 (peças selecionadas)
- k ≤ 2 (quantidade de peças defeituosas)
- p = 0.05 (probabilidade de peça defeituosa)

Neste caso, precisamos calcular a CDF:
$$P(X \leq 2) = P(X = 0) + P(X = 1) + P(X = 2)$$

## Método de Newton-Raphson

O método de Newton-Raphson é um algoritmo iterativo para encontrar raízes de funções. Embora não seja diretamente relacionado à distribuição binomial, pode ser usado em cálculos estatísticos avançados envolvendo distribuições binomiais.

### A Fórmula do Método de Newton

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

Onde:
- $x_n$ é a aproximação atual
- $x_{n+1}$ é a próxima aproximação
- $f(x_n)$ é o valor da função na aproximação atual
- $f'(x_n)$ é o valor da derivada da função na aproximação atual

### Passos para implementar o método de Newton:

1. Escolha uma aproximação inicial $x_0$
2. Calcule $f(x_0)$ e $f'(x_0)$
3. Calcule a nova aproximação usando a fórmula
4. Repita até que a diferença entre duas aproximações consecutivas seja menor que uma tolerância predefinida

## Testes Estatísticos com Distribuição Binomial

A distribuição binomial é fundamental para vários testes estatísticos, incluindo:

1. **Teste Binomial**: Usado para testar se a proporção de sucessos em uma sequência de tentativas difere significativamente de um valor esperado.

2. **Teste de Hipótese para Proporções**: Usado para comparar proporções entre grupos.

3. **Intervalos de Confiança para Proporções**: Usados para estimar o intervalo provável que contém o verdadeiro valor da proporção populacional.

## Diferença entre Distribuição Binomial e Distribuição de Bernoulli

- A **distribuição de Bernoulli** modela um único experimento com dois resultados possíveis (sucesso/fracasso).
- A **distribuição binomial** modela o número de sucessos em n experimentos de Bernoulli independentes.

Ou seja, a distribuição de Bernoulli é um caso especial da distribuição binomial onde n=1.

## Aproximações para a Distribuição Binomial

Para valores grandes de n, a distribuição binomial pode ser aproximada por:

1. **Distribuição Normal**: Quando n é grande e p não está muito próximo de 0 ou 1, a distribuição binomial pode ser aproximada por uma distribuição normal com média μ = np e variância σ² = np(1-p).

2. **Distribuição de Poisson**: Quando n é grande e p é pequeno (de modo que np seja moderado), a distribuição binomial pode ser aproximada por uma distribuição de Poisson com λ = np.

## Implementação em Python

Para trabalhar com a distribuição binomial em Python, pode-se usar o módulo `scipy.stats` que fornece a função `binom` ou implementar manualmente a fórmula.

```python
from scipy.stats import binom

# Calcular a PMF: P(X = k)
probability = binom.pmf(k, n, p)

# Calcular a CDF: P(X ≤ k)
cumulative_probability = binom.cdf(k, n, p)

# Calcular a SF: P(X > k)
survival_probability = binom.sf(k, n, p)
```

## Aplicações Reais

A distribuição binomial tem aplicações em diversas áreas:

1. **Medicina**: Analisar sucessos/fracassos em tratamentos médicos
2. **Controle de Qualidade**: Modelar defeitos em processos de produção
3. **Finanças**: Modelar sucessos/fracassos em operações financeiras
4. **Pesquisas de Opinião**: Analisar respostas sim/não em enquetes
5. **Ciência da Computação**: Modelar erros em transmissão de dados
6. **Ecologia**: Estudar presença/ausência de espécies em habitats

## Referências

1. Larson, R., & Farber, B. (2014). *Elementary Statistics: Picturing the World* (6ª ed.). Pearson.
2. Ross, S. M. (2014). *Introduction to Probability and Statistics for Engineers and Scientists* (5ª ed.). Academic Press.
3. Montgomery, D. C., & Runger, G. C. (2013). *Applied Statistics and Probability for Engineers* (6ª ed.). Wiley.