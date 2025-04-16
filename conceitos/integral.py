import sympy as sp
import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt

# Definindo símbolos e funções simbólicas
p = sp.symbols('p')
Q = 100 - 20*p + 2*p**2

# Análise simbólica usando sympy
print("=== Análise Simbólica ===")

# Calculando a primitiva de Q(p)
primitiva = sp.integrate(Q, p)
print("Primitiva de Q(p):", primitiva)

# Calculando a derivada de Q(p)
derivada = Q.diff(p)
print("Derivada de Q(p):", derivada)

# Definindo os limites a e b para a integral definida
a = 5
b = 15

# Calculando a integral definida
intervalo = (p, a, b)
integral = sp.integrate(Q, intervalo)
print(f"Integral de Q(p) no intervalo de ${a} a ${b}:", integral)

# Calculando a receita total
receita_total = integral.evalf()
print(f"Receita total gerada pelas vendas no intervalo de ${a} a ${b}:", receita_total)

# Análise da função de receita
print("\n=== Análise da Função de Receita ===")
# Definir a função de receita R(p)
R = p * Q
print("Função de receita R(p):", R)

# Calcular a derivada da função de receita
dR_dp = sp.diff(R, p)
print("Derivada da receita dR/dp:", dR_dp)

# Encontrar o preço que maximiza a receita
p_max = sp.solve(dR_dp, p)
print("Preço(s) que maximiza(m) a receita:", p_max)

# Análise numérica e visualização
print("\n=== Análise Numérica e Visualização ===")

# Converter a expressão simbólica em função numérica para plotagem
Q_lambda = sp.lambdify(p, Q, 'numpy')

# Criar dados para plotagem
p_vals = np.linspace(0, 20, 1000)
Q_vals = Q_lambda(p_vals)

# Plotar a função de demanda
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(p_vals, Q_vals)
plt.title('Função de Demanda Q(p)')
plt.xlabel('Preço (p)')
plt.ylabel('Quantidade (Q)')
plt.grid(True)

# Plotar a função de receita
R_lambda = sp.lambdify(p, R, 'numpy')
R_vals = R_lambda(p_vals)

plt.subplot(1, 2, 2)
plt.plot(p_vals, R_vals)
plt.title('Função de Receita R(p)')
plt.xlabel('Preço (p)')
plt.ylabel('Receita (R)')
plt.grid(True)

plt.tight_layout()
plt.show()
