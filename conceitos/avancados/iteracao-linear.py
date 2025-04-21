# Importação da biblioteca math para usar a função cos(x)
import math

# Definição da função f(x)
def f(x):
    return math.cos(x) - 5*x + 1

# Definição da função g(x) na forma x = g(x)
def g(x):
    return (math.cos(x) + 1)/5

# Escolha do valor inicial x0
x0 = 0.5

# Definição da tolerância
tolerance = 1e-6

# Iteração linear para encontrar o ponto fixo de g(x)
xn = x0
xn1 = g(xn)
while abs(xn1 - xn) > tolerance:
    xn = xn1
    xn1 = g(xn)

# Estimativa da raiz da função f(x)
root = xn1

print("A raiz da função f(x) é aproximadamente", root)
