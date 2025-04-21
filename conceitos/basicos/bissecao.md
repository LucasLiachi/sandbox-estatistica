# Método da Bisseção

O método da bisseção é uma técnica numérica para encontrar raízes de funções contínuas. É um método simples e robusto, baseado no Teorema do Valor Intermediário, que garante que se uma função contínua f(x) tem valores de sinais opostos nos extremos de um intervalo [a,b], então ela tem pelo menos uma raiz nesse intervalo.

## Fundamentos Matemáticos

O método da bisseção se baseia no **Teorema do Valor Intermediário**:

> Se uma função f é contínua em um intervalo fechado [a,b], e f(a) e f(b) têm sinais opostos (ou seja, f(a) · f(b) < 0), então existe pelo menos um ponto c no intervalo (a,b) tal que f(c) = 0.

Este teorema não fornece um método para encontrar o valor exato de c, mas o método da bisseção aproveita esta propriedade para estreitar progressivamente o intervalo que contém a raiz.

## Algoritmo

1. Começar com um intervalo [a,b] onde f(a) e f(b) têm sinais opostos
2. Calcular o ponto médio c = (a + b) / 2
3. Se f(c) ≈ 0 (dentro da tolerância desejada), c é a raiz
4. Caso contrário, verificar os sinais:
   - Se f(a) e f(c) têm sinais opostos, a raiz está em [a,c]
   - Se f(c) e f(b) têm sinais opostos, a raiz está em [c,b]
5. Repetir os passos 2-4 até encontrar a raiz com a precisão desejada ou atingir o número máximo de iterações

## Convergência e Erro

O método da bisseção tem uma taxa de convergência linear. Em cada iteração, o intervalo que contém a raiz é reduzido pela metade, o que significa que após n iterações, o erro máximo é:

$$\text{Erro} \leq \frac{b - a}{2^n}$$

Para atingir uma precisão ε, o número máximo de iterações necessárias é:

$$n \geq \log_2\left(\frac{b-a}{\varepsilon}\right)$$

## Implementação em Python

A implementação básica do método da bisseção em Python é relativamente simples:

```python
def bissecao(f, a, b, eps=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("A função deve ter sinais opostos nos extremos do intervalo.")
    
    iteracao = 0
    while (b - a) > eps and iteracao < max_iter:
        c = (a + b) / 2
        if abs(f(c)) < eps:
            return c, iteracao
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteracao += 1
    
    return (a + b) / 2, iteracao
```

Para uma implementação mais completa, com recursos de visualização e análise do processo de convergência, consulte o arquivo `bissecao.py`.

## Exemplos Práticos

### 1. Objeto em Queda com Resistência do Ar

Um objeto de massa m é abandonado de uma altura S0. A altura S(t) em função do tempo é dada por:

$$S(t) = S_0 - \frac{mg}{k}t + \frac{mg}{k^2}\left(1 - e^{-\frac{kt}{m}}\right)$$

onde:
- m = 2 kg (massa)
- S0 = 40 m (altura inicial)
- k = 0.6 kg/s (coeficiente de resistência do ar)
- g = 9.81 m/s² (aceleração da gravidade)

O método da bisseção é usado para encontrar o momento exato em que o objeto atinge o solo (S(t) = 0).

### 2. Desempenho de Jogador de Basquete

A função que descreve a pontuação de um jogador ao longo do tempo considera:

- Taxa de acerto de arremessos
- Habilidade de movimentação
- Fadiga ao longo do tempo
- Defesa do time adversário
- Estratégia de jogo

A função é modelada como:

$$f(t) = 100 \cdot \sin(\pi t/10) + 1500 \cdot e^{-0.1t} - 2000$$

O método da bisseção pode encontrar momentos específicos, como quando o jogador atinge determinada pontuação.

### 3. Tempo de Entrega de Projeto

Para um projeto de software com histórias de usuário, podemos calcular o tempo de entrega usando uma função que relaciona o número de histórias completadas com o tempo:

$$\text{histórias\_completadas} = \text{taxa\_hora} \cdot \text{horas}$$

onde:
- Taxa base = 3 histórias/semana
- Dias de trabalho = 5 dias/semana
- Horas por dia = 8 horas
- Fator de eficiência = 0.6 (baseado na senioridade da equipe)

O método da bisseção é usado para encontrar o tempo necessário para entregar um número específico de histórias.

## Vantagens e Desvantagens

### Vantagens
- **Simplicidade**: Fácil de entender e implementar
- **Robustez**: Sempre converge se as condições iniciais são adequadas
- **Confiabilidade**: Fornece uma estimativa do erro máximo
- **Não requer derivadas**: Útil para funções complexas ou sem forma analítica

### Desvantagens
- **Convergência lenta**: Taxa de convergência linear (reduz o erro pela metade a cada iteração)
- **Requer intervalo inicial**: Necessita de um intervalo [a,b] onde f(a) e f(b) têm sinais opostos
- **Pode não encontrar todas as raízes**: Se houver múltiplas raízes, é necessário dividir o intervalo
- **Ineficiente para polinômios de alto grau**: Outros métodos como Newton-Raphson convergem mais rapidamente

## Comparação com Outros Métodos

| Método | Convergência | Complexidade | Requisitos | Robustez |
|--------|--------------|--------------|------------|----------|
| Bisseção | Linear | Baixa | Intervalo com mudança de sinal | Alta |
| Newton-Raphson | Quadrática | Média | Ponto inicial e função derivável | Média |
| Secante | Superlinear | Média | Dois pontos iniciais | Média |
| Falsa Posição | Linear | Média | Intervalo com mudança de sinal | Alta |
| Ponto Fixo | Linear | Baixa | Ponto inicial e função bem comportada | Baixa |

## Aplicações Práticas

O método da bisseção é utilizado em diversas áreas:

1. **Engenharia**: cálculos de resistência de materiais, designs estruturais
2. **Física**: encontrar pontos de equilíbrio em sistemas dinâmicos
3. **Economia**: determinar taxas de juros de equilíbrio
4. **Computação gráfica**: interseções de raios com superfícies
5. **Química**: equilíbrio químico
6. **Finanças**: cálculo de TIR (Taxa Interna de Retorno)

## Recursos Adicionais

- Para uma exploração interativa do método da bisseção, consulte o notebook `bissecao.ipynb`
- Para exemplos práticos de implementação e uso, veja o script `bissecao.py`

## Referências

1. Burden, R. L., & Faires, J. D. (2010). Numerical Analysis (9th ed.). Brooks/Cole.
2. Chapra, S. C., & Canale, R. P. (2015). Numerical Methods for Engineers (7th ed.). McGraw-Hill.
3. Heath, M. T. (2018). Scientific Computing: An Introductory Survey (2nd ed.). SIAM.