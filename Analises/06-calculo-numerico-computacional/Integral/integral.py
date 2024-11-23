import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt

# Defina a função que você deseja integrar
def f(x):
    return x**3 * np.sin(x) / (x**4 + 1)

# Defina os limites de integração
a = 0
b = 5

# Calcule a integral
resultado, erro = spi.quad(f, a, b)

# Apresente o resultado da integral
print(f"O resultado da integral é: {resultado}")

# Aproxime a derivada da função f(x) usando a fórmula da diferença finita
dx = 0.001
dfdx = lambda x: (f(x+dx) - f(x))/dx

# Apresente a derivada da função f(x)
print(f"A derivada aproximada da função f(x) é: {dfdx(2)}")

# Crie o gráfico de f(x)
x = np.linspace(a, b, 1000)
plt.plot(x, f(x))
plt.title('Gráfico de f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()



