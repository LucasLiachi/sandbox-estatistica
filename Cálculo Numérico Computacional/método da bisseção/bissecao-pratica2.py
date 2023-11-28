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

tempo_entrega_projeto(20)

'''
A função tempo_entrega_projeto(num_historias) calcula o tempo de entrega de um projeto com base no número de histórias fornecido como entrada num_historias.

O método utilizado é o método da bissecção para encontrar a raiz da função f(x). 
O objetivo é encontrar o valor de x que faz f(x) = 0.

A função f(x) é definida usando uma expressão lambda lambda x: num_historias / (taxa * x) - 1. 
Essa função representa a diferença entre o tempo estimado para concluir o projeto (calculado dividindo o número de histórias pelo tempo de desenvolvimento x por história) e o tempo disponível para concluir o projeto (calculado subtraindo 1 do resultado anterior). O valor de taxa é fixado em 0,1042.

O intervalo de busca é definido como a = 100 e b = 300. O valor de eps é definido como 1e-6 para controlar a precisão da solução.

O método da bissecção é implementado com um loop while que continua a dividir o intervalo ao meio e atualizar os limites superior e inferior do intervalo até que a diferença entre eles seja menor que eps. O valor médio c do intervalo é calculado como (a + b) / 2 e a função f(c) é avaliada. Se o resultado for menor que zero, o valor de c se torna o novo limite superior (b = c). Caso contrário, o valor de c se torna o novo limite inferior (a = c).

O resultado final é o valor de c encontrado após a convergência. Ele representa o tempo de entrega em horas necessário para concluir o projeto com base no número de histórias fornecido.

'''

def taxa_conclusao_historias_por_tempo(n_historias_semana, dias_trabalho_semana, horas_trabalho_dia, fator_eficiencia):
    horas_trabalho_semana = dias_trabalho_semana * horas_trabalho_dia
    historias_por_hora = n_historias_semana / (horas_trabalho_semana * fator_eficiencia)
    return historias_por_hora

def tempo_para_entregar(num_historias, taxa_conclusao_historias_por_hora):
    tempo = num_historias / taxa_conclusao_historias_por_hora
    return tempo

def bissecao(f, a, b, precisao):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("A função deve ter sinais opostos nos extremos do intervalo.")
    while (b - a) / 2 > precisao:
        c = (a + b) / 2
        fc = f(c)
        if fc == 0:
            return c
        elif fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (a + b) / 2

n_historias_semana = 3
dias_trabalho_semana = 5
horas_trabalho_dia = 8
fator_eficiencia = 0.6
num_historias = 20
a = 100
b = 300
precisao = 0.01

taxa_conclusao_historias_por_hora = taxa_conclusao_historias_por_tempo(n_historias_semana, dias_trabalho_semana, horas_trabalho_dia, fator_eficiencia)

tempo_necessario = bissecao(lambda x: tempo_para_entregar(num_historias, taxa_conclusao_historias_por_hora) - x, a, b, precisao)

print(f"A taxa de conclusão de histórias por hora é de {taxa_conclusao_historias_por_hora:.4f}.")
print(f"O tempo necessário para entregar um projeto com {num_historias} histórias é de {tempo_necessario:.2f} horas.")
