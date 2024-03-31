import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual, Output
import ipywidgets as widgets

# Definição da função que será usada no exemplo
def f(t):
    return 100 * np.sin(np.pi * t / 10) + 1500 * np.exp(-0.1 * t) - 2000

# Definição do método de bisseção
def bissecao(f, a, b, eps=1e-6):
    while abs(b-a) > eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

# Criação do gráfico
t = np.linspace(0, 30, 100)
fig, ax = plt.subplots()
ax.plot(t, f(t))
ax.axhline(y=0, color='black', linestyle='--')
ax.set_xlabel('Tempo (min)')
ax.set_ylabel('Pontuação')
ax.set_title('Desempenho de um jogador de basquete')

# Criação do widget para escolher o intervalo de busca
a_widget = widgets.FloatSlider(min=0, max=30, step=0.1, value=10, description='a:')
b_widget = widgets.FloatSlider(min=0, max=30, step=0.1, value=20, description='b:')
eps_widget = widgets.FloatLogSlider(value=-6, base=10, min=-10, max=0, step=1, description='eps:')
out = Output()

# Função que será chamada quando o botão "Calcular" for pressionado
def calcular(a, b, eps):
    with out:
        out.clear_output()
        raiz = bissecao(f, a, b, eps)
        ax.plot(raiz, f(raiz), 'ro')
        display(fig)
        plt.close()

# Criação do botão para calcular a raiz
calcular_button = widgets.Button(description='Calcular')
calcular_button.on_click(lambda button: calcular(a_widget.value, b_widget.value, 10**eps_widget.value))

# Criação do widget com os controles
widget_box = widgets.VBox([a_widget, b_widget, eps_widget, calcular_button, out])
display(widget_box)
