import sympy as sp

# Definindo a função quadrática Q(p) que modela a relação entre o preço de um produto e a quantidade demandada pelos consumidores
p = sp.symbols('p')
Q = 100 - 20*p + 2*p**2

# Calculando a primitiva de Q(p)
primitiva = sp.integrate(Q, p)
print("Primitiva de Q(p):", primitiva)

# Calculando a derivada de Q(p)
derivada = Q.diff(p)
print("Derivada de Q(p):", derivada)


# Definindo os limites a e b

a = 5
b = 15

# Calculando a integral de Q(p) no intervalo de $a a $b
intervalo = (p, 5, 15)
integral = sp.integrate(Q, intervalo)
print("Integral de Q(p) no intervalo de $5 a $15:", integral)

# Calculando a receita total gerada pelas vendas de sapatos no intervalo de $5 a $15
receita_total = integral.evalf()
print("Receita total gerada pelas vendas de sapatos no intervalo de $5 a $15:", receita_total)
