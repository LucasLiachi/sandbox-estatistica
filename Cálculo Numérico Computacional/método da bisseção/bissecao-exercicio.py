m = 2 # kg
S0 = 40 # m
k = 0.6 # kg/s
g = 9.81 # m/s^2

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 7, 1)
S = S0 - ((m*g/k)*t) + (((((m**2)*g)/(k**2)))*(1 - np.exp(-k*t/m)))

%matplotlib inline
import matplotlib.pyplot as plt

# Plota o gráfico
plt.plot(t, S)
plt.axhline(y=0, color='r', linestyle='-')
plt.xlabel('Tempo (s)')
plt.ylabel('Altura (m)')

# Exibe o gráfico na tela
plt.show()
