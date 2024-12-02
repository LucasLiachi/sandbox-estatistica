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
