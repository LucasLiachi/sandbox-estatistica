# Probabilidade e Intervalos de Confiança

## Conceitos Fundamentais

### Probabilidade
A probabilidade é uma medida numérica da chance de um evento ocorrer. Formalmente:

$$ P(A) = \frac{n(A)}{n(S)} $$

Onde:
- $P(A)$ é a probabilidade do evento A
- $n(A)$ é o número de casos favoráveis
- $n(S)$ é o número total de casos possíveis

### Intervalos de Confiança
O intervalo de confiança é um intervalo estimado de um parâmetro populacional baseado em uma amostra.

#### Fórmula do Intervalo de Confiança para Média
$$ IC_{(1-\alpha)} = \bar{x} \pm t_{\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}} $$

Onde:
- $\bar{x}$ é a média amostral
- $t_{\alpha/2, n-1}$ é o valor crítico da distribuição t de Student
- $s$ é o desvio padrão amostral
- $n$ é o tamanho da amostra
- $(1-\alpha)$ é o nível de confiança

## Implementação em Python

```python
from scipy import stats
import numpy as np

def calcular_ic(dados, confianca=0.95):
    media = np.mean(dados)
    erro = stats.t.ppf((1 + confianca) / 2, len(dados) - 1) * (np.std(dados, ddof=1) / np.sqrt(len(dados)))
    return media - erro, media + erro
```

## Exemplo Prático

Para uma amostra de notas de alunos:
```python
notas = [82, 64, 64, 79, 64, 76, 52, 61, 85]
ic_inferior, ic_superior = calcular_ic(notas)
```

## Interpretação
O intervalo calculado contém o verdadeiro valor do parâmetro populacional com a confiança especificada (geralmente 95%).

## Referências

1. Montgomery, D. C., & Runger, G. C. (2010). *Applied Statistics and Probability for Engineers*. John Wiley & Sons.
2. Wasserman, L. (2004). *All of Statistics: A Concise Course in Statistical Inference*. Springer.
3. Casella, G., & Berger, R. L. (2002). *Statistical Inference*. Duxbury.

## Visualização
Para visualizar intervalos de confiança e exemplos interativos, consulte o notebook:
`recursos/notebooks/probabilidade_tutorial.ipynb`
