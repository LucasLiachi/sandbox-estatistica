# Probabilidade

## Introdução

A probabilidade é um ramo da matemática que lida com a análise de fenômenos aleatórios e a quantificação da incerteza. É fundamental para estatística, ciência de dados, inteligência artificial, física quântica, entre outros campos.

## Conceitos Fundamentais

### Definição Clássica (Laplace)

A definição clássica de probabilidade, proposta por Pierre-Simon Laplace, estabelece:

$$P(A) = \frac{\text{número de casos favoráveis}}{\text{número de casos possíveis}}$$

Esta abordagem pressupõe um conjunto finito de resultados possíveis, todos igualmente prováveis.

**Exemplo**: Ao lançar um dado de seis faces, a probabilidade de obter um número par é:
- Casos favoráveis: 3 (números 2, 4, 6)
- Casos possíveis: 6 (números 1, 2, 3, 4, 5, 6)
- Portanto, $P(\text{número par}) = \frac{3}{6} = \frac{1}{2} = 0.5 \text{ ou } 50\%$

### Axiomas de Probabilidade (Kolmogorov)

A teoria moderna da probabilidade é baseada em três axiomas desenvolvidos por Andrey Kolmogorov:

1. **Não-negatividade**: $P(A) \geq 0$ para qualquer evento $A$
2. **Normalização**: $P(\Omega) = 1$, onde $\Omega$ é o espaço amostral (conjunto de todos os resultados possíveis)
3. **Aditividade**: Se $A$ e $B$ são eventos mutuamente exclusivos, então $P(A \cup B) = P(A) + P(B)$

### Propriedades Derivadas

A partir dos axiomas, podemos derivar várias propriedades úteis:

- $P(\emptyset) = 0$ (a probabilidade do conjunto vazio é zero)
- $P(A^c) = 1 - P(A)$ (probabilidade do complemento)
- $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ (regra da adição)
- $0 \leq P(A) \leq 1$ para qualquer evento $A$

## Probabilidade Condicional

A probabilidade condicional $P(A|B)$ representa a chance de ocorrência do evento $A$ dado que o evento $B$ já ocorreu:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

### Regra da Multiplicação

A partir da definição de probabilidade condicional, obtemos:

$$P(A \cap B) = P(B) \cdot P(A|B) = P(A) \cdot P(B|A)$$

### Eventos Independentes

Dois eventos $A$ e $B$ são independentes se a ocorrência de um não afeta a probabilidade do outro. Matematicamente:

$$P(A|B) = P(A) \quad \text{ou equivalentemente} \quad P(A \cap B) = P(A) \cdot P(B)$$

## Variáveis Aleatórias

Uma variável aleatória é uma função que associa a cada resultado de um experimento aleatório um valor numérico. Existem dois tipos principais:

### Variáveis Aleatórias Discretas

Assumem valores em um conjunto discreto (finito ou contável). São caracterizadas por:

- **Função Massa de Probabilidade (PMF)**: $P(X = x)$
- **Função de Distribuição Acumulada (CDF)**: $F_X(x) = P(X \leq x)$

**Exemplos**: Distribuição binomial, Poisson, geométrica, hipergeométrica.

### Variáveis Aleatórias Contínuas

Assumem valores em um intervalo contínuo. São caracterizadas por:

- **Função Densidade de Probabilidade (PDF)**: $f(x)$
- **Função de Distribuição Acumulada (CDF)**: $F_X(x) = P(X \leq x) = \int_{-\infty}^{x} f(t) dt$

Para uma PDF válida, deve-se ter:
1. $f(x) \geq 0$ para todo $x$
2. $\int_{-\infty}^{\infty} f(x) dx = 1$

A probabilidade de $X$ estar em um intervalo $[a, b]$ é:

$$P(a \leq X \leq b) = \int_{a}^{b} f(x) dx$$

**Exemplos**: Distribuição normal, exponencial, uniforme, beta, gama.

## Distribuições de Probabilidade Comuns

### Distribuição Normal (Gaussiana)

A distribuição normal é uma das mais importantes em estatística, caracterizada por sua curva em forma de sino simétrica.

- **Parâmetros**: Média $\mu$ e desvio padrão $\sigma$
- **PDF**: $f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$
- **Propriedades**:
  - Simétrica em torno da média $\mu$
  - Aproximadamente 68% dos valores estão a menos de um desvio padrão da média
  - Aproximadamente 95% dos valores estão a menos de dois desvios padrão da média
  - Aproximadamente 99.7% dos valores estão a menos de três desvios padrão da média (regra 68-95-99.7)

### Distribuição Exponencial

Usada para modelar o tempo de espera até a ocorrência de um evento em um processo de Poisson.

- **Parâmetro**: Taxa $\lambda > 0$
- **PDF**: $f(x) = \lambda e^{-\lambda x}, \quad x \geq 0$
- **Média**: $E[X] = \frac{1}{\lambda}$
- **Variância**: $Var[X] = \frac{1}{\lambda^2}$
- **Propriedade de falta de memória**: $P(X > s + t | X > t) = P(X > s)$

### Distribuição Uniforme

Todos os valores em um intervalo têm a mesma probabilidade de ocorrência.

- **Parâmetros**: Limites inferior $a$ e superior $b$
- **PDF**: $f(x) = \frac{1}{b-a}, \quad a \leq x \leq b$
- **Média**: $E[X] = \frac{a+b}{2}$
- **Variância**: $Var[X] = \frac{(b-a)^2}{12}$

## Estatísticas Descritivas

As estatísticas descritivas resumem as principais características de um conjunto de dados:

### Medidas de Tendência Central

- **Média**: $\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$
- **Mediana**: Valor central quando os dados estão ordenados
- **Moda**: Valor mais frequente

### Medidas de Dispersão

- **Variância**: $s^2 = \frac{1}{n-1}\sum_{i=1}^{n} (x_i - \bar{x})^2$
- **Desvio Padrão**: $s = \sqrt{s^2}$
- **Amplitude**: Diferença entre o valor máximo e mínimo
- **Intervalo Interquartil (IQR)**: Diferença entre o 3º e 1º quartis

## Intervalos de Confiança

Um intervalo de confiança (IC) fornece um intervalo de valores que provavelmente contém um parâmetro populacional desconhecido.

### Intervalo de Confiança para a Média

Para uma amostra com distribuição normal ou tamanho grande:

$$IC_{(1-\alpha)} = \bar{x} \pm t_{\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}}$$

Onde:
- $\bar{x}$ é a média amostral
- $s$ é o desvio padrão amostral
- $n$ é o tamanho da amostra
- $t_{\alpha/2, n-1}$ é o valor crítico da distribuição t com $n-1$ graus de liberdade

### Interpretação Correta

Um intervalo de confiança de 95% significa que, se o processo de amostragem fosse repetido muitas vezes, aproximadamente 95% dos intervalos calculados conteriam o verdadeiro valor do parâmetro populacional.

## Aplicações Práticas

A probabilidade é usada em diversos campos:

- **Estatística**: Inferência estatística, testes de hipóteses
- **Finanças**: Modelagem de risco, precificação de ativos
- **Engenharia**: Controle de qualidade, confiabilidade
- **Ciência de Dados**: Machine learning, análise preditiva
- **Medicina**: Ensaios clínicos, epidemiologia
- **Física**: Mecânica quântica, termodinâmica estatística
- **Jogos e Apostas**: Estratégias ótimas, cálculo de odds

## Recursos para Aprendizado

### Bibliotecas Python para Probabilidade e Estatística

```python
# Bibliotecas essenciais
import numpy as np          # Cálculos numéricos
import scipy.stats as stats # Distribuições e testes estatísticos
import pandas as pd         # Manipulação de dados
import matplotlib.pyplot as plt  # Visualização
import seaborn as sns       # Visualização estatística avançada

# Exemplo: Distribuição normal
x = np.linspace(-3, 3, 100)
plt.plot(x, stats.norm.pdf(x))
plt.title('Distribuição Normal Padrão')
plt.show()
```

### Referências Bibliográficas

1. Casella, G., & Berger, R. L. (2002). *Statistical Inference*. Duxbury Press.
2. Ross, S. M. (2014). *A First Course in Probability*. Pearson.
3. Wasserman, L. (2004). *All of Statistics: A Concise Course in Statistical Inference*. Springer.
4. DeGroot, M. H., & Schervish, M. J. (2012). *Probability and Statistics*. Addison-Wesley.
5. Montgomery, D. C., & Runger, G. C. (2010). *Applied Statistics and Probability for Engineers*. John Wiley & Sons.

# Validação de Funções Densidade de Probabilidade (PDF)

Este módulo implementa um sistema completo para validação de Funções Densidade de Probabilidade (PDF) usando Python e SymPy. O código é especialmente útil para análise estatística em controle de qualidade industrial.

## Funcionalidades Principais

### 1. Verificação de Positividade
```python
verificar_positividade(funcao, var, dominio)
```
- **Entrada**: Função simbólica, variável e domínio
- **Saída**: Boolean indicando se a função é não-negativa em todo domínio
- **Funcionamento**: 
  - Encontra pontos críticos através da derivada
  - Verifica valores nos extremos do domínio
  - Testa a função em pontos críticos

### 2. Verificação de Integral Unitária
```python
verificar_integral_unitaria(funcao, var, dominio)
```
- **Entrada**: Função simbólica, variável e domínio
- **Saída**: Boolean indicando se a integral é igual a 1
- **Funcionamento**:
  - Calcula integral simbólica no domínio
  - Verifica se o resultado é aproximadamente 1
  - Usa tolerância numérica para comparações

### 3. Cálculo de Probabilidade
```python
calcular_probabilidade(funcao, var, limite)
```
- **Entrada**: Função simbólica, variável e limites do intervalo
- **Saída**: Valor numérico da probabilidade
- **Funcionamento**:
  - Calcula integral definida no intervalo especificado
  - Retorna probabilidade P(a ≤ X ≤ b)

## Recursos Avançados

### Geração de Relatórios LaTeX
```python
gerar_relatorio_latex(funcao, var, dominio, resultados)
```
- Gera documentação matemática formatada
- Inclui expressões simbólicas e resultados
- Facilita integração com documentos técnicos

### Tratamento de Erros
- Validação de domínio e expressões
- Mensagens detalhadas de erro
- Sugestões de correção

## Exemplos de Uso

### 1. Distribuição Exponencial
```python
funcao_exp = "2 * exp(-2*x)"
resultados = validar_pdf(funcao_exp, 'x', (0, float('inf')))
```
- PDF válida
- Domínio: [0, ∞)
- P(X > 10) = e^(-20)

### 2. Distribuição Triangular
```python
funcao_tri = "Piecewise((2*x, x >= 0) & (x <= 1/2), (2*(1-x), x > 1/2) & (x <= 1), (0, True))"
resultados = validar_pdf(funcao_tri, 'x', (0, 1))
```
- Exemplo de função definida por partes
- Domínio finito [0, 1]
- Integral unitária verificada

## Requisitos Técnicos

### Dependências
- SymPy: Para computação simbólica
- NumPy: Para cálculos numéricos
- Python typing: Para anotações de tipo

### Tipos de Dados
- `sp.Expr`: Expressões simbólicas do SymPy
- `Union[float, str]`: Suporte para valores numéricos e simbólicos
- `Tuple`: Para representação de intervalos

## Tratamento de Erros

### Classe CustomException
```python
class PDFValidationError(Exception)
```
- Exceção personalizada para erros de validação
- Mensagens detalhadas para debugging
- Sugestões de correção quando aplicável

### Validações Principais
1. Positividade da função no domínio
2. Integral unitária (∫f(x)dx = 1)
3. Domínio bem definido
4. Expressões matemáticas válidas

## Considerações de Uso

### Performance
- Uso de computação simbólica para precisão
- Tolerância numérica configurável
- Otimização para domínios infinitos

### Boas Práticas
- Documentação detalhada das funções
- Tipos fortemente tipados
- Tratamento robusto de erros
- Testes incluídos no código

## Limitações e Considerações
- Algumas integrais complexas podem ser computacionalmente intensivas
- Funções descontínuas requerem atenção especial
- Domínios infinitos podem precisar de tratamento específico