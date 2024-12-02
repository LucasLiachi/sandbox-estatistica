# Distribuição Binomial de Newton - Exemplo

## Descrição do Problema
Este exemplo calcula a probabilidade de obter exatamente 5 sucessos em 5 tentativas, com uma probabilidade de sucesso de 0,75.

## Fórmula
A fórmula da probabilidade binomial é:

$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$

Onde:
- $n$ é o número de tentativas
- $k$ é o número de sucessos
- $p$ é a probabilidade de sucesso
- $(1-p)$ é a probabilidade de falha

## Cálculo do Exemplo
No nosso caso:
- $n = 5$ (tentativas)
- $k = 5$ (sucessos)
- $p = 0,75$ (probabilidade de sucesso)

Portanto:
$P(X = 5) = (0,75)^5 (0,25)^{5-5} = (0,75)^5 (1)$

Nota: Esta é uma versão simplificada, pois omite o fator de combinação $\binom{n}{k}$ que deveria ser incluído para o cálculo completo.