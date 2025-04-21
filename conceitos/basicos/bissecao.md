# Método da Bisseção

O método da bisseção é uma técnica numérica para encontrar raízes de funções contínuas. É um método simples e robusto, baseado no Teorema do Valor Intermediário, que garante que se uma função contínua f(x) tem valores de sinais opostos nos extremos de um intervalo [a,b], então ela tem pelo menos uma raiz nesse intervalo.

## Algoritmo

1. Começar com um intervalo [a,b] onde f(a) e f(b) têm sinais opostos
2. Calcular o ponto médio c = (a + b) / 2
3. Se f(c) ≈ 0 (dentro da tolerância desejada), c é a raiz
4. Caso contrário, verificar os sinais:
   - Se f(a) e f(c) têm sinais opostos, a raiz está em [a,c]
   - Se f(c) e f(b) têm sinais opostos, a raiz está em [c,b]
5. Repetir os passos 2-4 até encontrar a raiz com a precisão desejada

## Exemplos Práticos

### 1. Objeto em Queda com Resistência do Ar

Um objeto de massa m é abandonado de uma altura S0. A altura S(t) em função do tempo é dada por:

S(t) = S0 - (mg/k)t + [(mg/k²)](1 - exp(-kt/m))

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
f(t) = 100 * sin(πt/10) + 1500 * exp(-0.1t) - 2000

O método da bisseção pode encontrar momentos específicos, como quando o jogador atinge determinada pontuação.

### 3. Tempo de Entrega de Projeto

Para um projeto de software com histórias de usuário, podemos calcular o tempo de entrega usando:

tempo = (número de histórias) / (taxa de conclusão)

onde:
- Taxa base = 3 histórias/semana
- Dias de trabalho = 5 dias/semana
- Horas por dia = 8 horas
- Fator de eficiência = 0.6 (baseado na senioridade da equipe)

O método da bisseção é usado para encontrar o tempo necessário para entregar um número específico de histórias.

## Implementação

A implementação em Python está disponível no arquivo `bissecao.py`, que inclui:

1. Função genérica do método da bisseção
2. Implementações específicas para cada exemplo
3. Visualizações gráficas dos resultados
4. Interface interativa para testes

## Considerações Práticas

- A escolha do intervalo inicial [a,b] é crucial
- A tolerância (epsilon) deve ser adequada ao problema
- O método sempre converge, mas pode ser lento
- Útil quando a função é complicada ou não tem forma analítica
- Pode ser usado em conjunto com métodos gráficos para melhor compreensão

## Vantagens e Desvantagens

### Vantagens
- Método simples e robusto
- Sempre converge se as condições iniciais são adequadas
- Fácil de implementar
- Não requer cálculo de derivadas

### Desvantagens
- Convergência relativamente lenta
- Requer um intervalo inicial com mudança de sinal
- Pode não encontrar todas as raízes se houver múltiplas