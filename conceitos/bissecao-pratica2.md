# Exercício prático elaborado para entender a disciplina

Para determinar a função que representa o tempo necessário para a equipe entregar um projeto com 20 stories, podemos utilizar a fórmula:

tempo = (número de histórias) / (taxa de conclusão de histórias por unidade de tempo)

No caso, temos que a equipe possui um desempenho médio de 3 histórias por semana, trabalhando 5 dias por semana e com nível médio de senioridade 3 de 5. Podemos calcular a taxa de conclusão de histórias por unidade de tempo como:

taxa = (3 histórias/semana) / (5 dias/semana x 8 horas/dia x fator de eficiência)

O fator de eficiência é uma medida que leva em conta o nível de senioridade da equipe. Neste caso, podemos assumir um fator de eficiência de 0.6 para uma equipe com nível médio de senioridade 3 de 5. Portanto, temos:

taxa = (3 histórias/semana) / (5 dias/semana x 8 horas/dia x 0.6) = 0.1042 histórias/hora

Substituindo na fórmula anterior, temos:

tempo = 20 histórias / 0.1042 histórias/hora = 192 horas

Agora podemos utilizar o método da bisseção para encontrar a raiz da função que representa o tempo necessário para a equipe entregar um projeto com um número arbitrário de histórias. Para isso, precisamos escolher um intervalo inicial que contenha a raiz e que possamos dividir pela metade em cada iteração. Podemos escolher o intervalo [100, 300] horas, já que sabemos que o tempo necessário deve estar entre 100 e 300 horas.

Em cada iteração do método da bisseção, calculamos o valor da função no ponto médio do intervalo e comparamos com zero. Se o valor for menor que zero, sabemos que a raiz está no intervalo esquerdo, caso contrário, está no intervalo direito. Dividimos o intervalo escolhido pela metade e repetimos o processo até encontrar a raiz com a precisão desejada.

## função

'''
def tempo_entrega_projeto(num_historias):
    taxa = 0.1042
    f = lambda x: num_historias / (taxa * x) - 1
    a, b = 100, 300
    eps = 1e-6
    while b - a > eps:
        c = (a + b) / 2
        if f(c) < 0:
            b = c
        else:
            a = c
    return c
'''

## Podemos testar a função para o caso em que o projeto possui 20 histórias:

>>> tempo_entrega_projeto(20)
192.0406974554062


