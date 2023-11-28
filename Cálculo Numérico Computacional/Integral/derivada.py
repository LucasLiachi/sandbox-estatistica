import sympy as sp

# definir a função de demanda q(p) e a constante a e b
p = sp.Symbol('p')
a = 100
b = 2
q = a - b * p

# definir a função de receita R(p)
R = p * q

# calcular a derivada da função de receita em relação a p
dR_dp = sp.diff(R, p)

# encontrar o preço que maximiza a receita
p_max = sp.solve(dR_dp, p)[0]

print("A função de demanda é:", q)
print("A função de receita é:", R)
print("A derivada da função de receita em relação a p é:", dR_dp)
print("O preço que maximiza a receita é:", p_max)
