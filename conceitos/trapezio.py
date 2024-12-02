import math

# Definindo a função f(t)
def f(t):
    return math.sin(math.pi * t**2/2)

# Definindo a regra dos trapézios simples
def trapezoidal_rule_simple(a, b, n):
    h = (b - a) / n
    sum = (f(a) + f(b)) / 2
    for i in range(1, n):
        x = a + i * h
        sum += f(x)
    return h * sum

# Definindo a regra dos trapézios composta
def trapezoidal_rule_composite(a, b, n):
    h = (b - a) / n
    sum = (f(a) + f(b)) / 2
    for i in range(1, n):
        x = a + i * h
        sum += f(x)
    return h * sum

# Calculando a integral de f(t) usando a regra dos trapézios simples
integral_simple = trapezoidal_rule_simple(0, 2-math.sqrt(2), 1)
print("Integral usando a regra dos trapézios simples:", integral_simple)

# Calculando a integral de f(t) usando a regra dos trapézios composta com diferentes números de trapézios
for n in [3, 5, 10, 20, 60]:
    integral_composite = trapezoidal_rule_composite(0, 2-math.sqrt(2), n)
    print("Integral usando a regra dos trapézios composta com", n, "trapézios:", integral_composite)

t = [0, 120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200] # tempos em segundos
"""
Este script calcula a distância aproximada percorrida usando a regra do trapézio para integração numérica.
Variáveis:
    t (list): Uma lista de intervalos de tempo em segundos.
    v (list): Uma lista de velocidades em km/h correspondentes a cada intervalo de tempo.
    n (int): O número de intervalos, calculado como o comprimento da lista de tempos menos um.
    h (float): O tamanho de cada intervalo, calculado como a diferença entre os últimos e primeiros valores de tempo dividida pelo número de intervalos.
    areas (list): Uma lista para armazenar a área de cada trapézio.
    distancia (float): A distância total percorrida, calculada somando as áreas dos trapézios e convertendo de km/h para m/s.
O script itera através de cada intervalo, calcula a área do trapézio formado pelas velocidades nos pontos finais do intervalo, e soma essas áreas para aproximar a distância total percorrida. O resultado é impresso em metros.
"""
v = [20, 22, 23, 25, 30, 31, 32, 40, 45, 50, 65] # velocidades em km/h

n = len(t) - 1 # número de intervalos
h = (t[-1] - t[0]) / n # tamanho de cada intervalo

areas = []
for i in range(n):
    v1 = v[i]
    v2 = v[i+1]
    t1 = t[i]
    t2 = t[i+1]
    area = (v1 + v2) * (t2 - t1) / 2
    areas.append(area)

distancia = sum(areas) * 1000/3600 # convertendo de km/h para m/s

print(f"Aproximação da distância percorrida: {distancia:.0f} metros")

