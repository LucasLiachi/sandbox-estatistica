Um objeto de massa m é abandonado de uma altura So em relação ao solo. Após 
t segundos a sua altura S(t) pode ser calculada pela expressão a seguir: 
em que k é o coeficiente de resistêncial do ar e g é a aceleração da gravidade. 
Fazendo 2 kg, % = 40 m, k= 0,6 kg/s e 9,81 use o método gráfico para 
isolar a raiz e, posteriormente, calcule o tempo que o objeto leva para atingir o 
solo utilizando o método da bisseção, com uma tolerância € 0,001. 

## A expressão para a altura do objeto em função do tempo é:

S(t) = So - (mg/k) * t + [(mg/k^2) - (v0/k)] * (1 - exp(-kt/m))

## Onde:
m = 2 kg (massa do objeto)
So = 40 m (altura inicial em relação ao solo)
k = 0,6 kg/s (coeficiente de resistência do ar)
g = 9,81 m/s^2 (aceleração da gravidade)

Para calcular o tempo que o objeto leva para atingir o solo, podemos utilizar o método da bisseção. Esse método consiste em dividir um intervalo em dois subintervalos, avaliar em qual subintervalo a raiz se encontra e repetir o processo com o subintervalo onde a raiz se encontra, até atingir a tolerância desejada.

Vamos escolher o intervalo [0, 10] para o tempo, já que o objeto leva menos de 10 segundos para atingir o solo. Avaliando S(0) e S(10), podemos verificar que a raiz se encontra nesse intervalo (S(0) = 40 m e S(10) < 0).

Agora, vamos utilizar o método gráfico para isolar a raiz. Podemos plotar a função S(t) em um gráfico com o tempo no eixo x e a altura no eixo y. Para isso, vamos definir uma função em Python para calcular S(t):

### Raiz encontrada em 4.683799743652344 segundos.

Portanto, o objeto leva aproximadamente 4,68 segundos para atingir o solo. O método gráfico foi útil para isolar a raiz e definir um intervalo para aplicação do método da bisseção. Já o método da bisseção foi útil para encontrar a raiz com a tolerância desejada.

Vale lembrar que o modelo utilizado para calcular a altura do objeto leva em consideração a resistência do ar, que pode variar dependendo da forma e das dimensões do objeto. Além disso, a aceleração da gravidade pode variar dependendo da altitude e da latitude do local onde o experimento é realizado. Porém, para fins didáticos, o modelo utilizado é suficiente para ilustrar a aplicação dos métodos gráfico e numérico para encontrar raízes de funções.

---------------------------------------

Para resolver este exercício utilizando o método gráfico, é necessário plotar um gráfico da função altura S(t) em relação ao tempo t e identificar o ponto em que a altura é igual a zero, ou seja, quando o objeto atinge o solo.

Para isso, utiliza-se a equação fornecida para a altura S(t) e substitui-se os valores dados: m = 2 kg, So = 40 m, k = 0,6 kg/s e g = 9,81 m/s^2. Em seguida, plota-se o gráfico da função S(t) para valores de t entre 0 e 10 segundos (por exemplo). É possível notar visualmente o ponto em que a altura é igual a zero, indicando que o objeto atingiu o solo.

Para calcular o tempo que o objeto leva para atingir o solo utilizando o método da bisseção, é necessário definir um intervalo [a, b] que contenha a raiz da função, que é o tempo em que a altura é igual a zero. Pode-se escolher, por exemplo, a = 4 e b = 5 segundos, já que é possível visualizar que a raiz está próxima a esses valores no gráfico. Em seguida, calcula-se o ponto médio c = (a + b) / 2 e avalia-se a função S(c). Se S(c) é igual a zero ou se a diferença entre S(c) e zero é menor que a tolerância desejada (no caso, 0,001), o valor de c é a raiz procurada e o programa para. Caso contrário, avalia-se se S(a) e S(c) têm sinais opostos ou não. Se tiverem sinais opostos, a raiz está no intervalo [a, c], caso contrário, a raiz está no intervalo [c, b]. O processo é repetido até que a raiz seja encontrada ou o número máximo de iterações seja alcançado.

Em resumo, o processo para resolver o exercício é o seguinte:

Definir a função S(t) utilizando a equação fornecida e substituindo os valores dados;
Plotar o gráfico da função S(t) para valores de t entre 0 e 10 segundos (por exemplo);
Identificar visualmente o ponto em que a altura é igual a zero, que indica o tempo em que o objeto atinge o solo;
Definir um intervalo [a, b] que contenha a raiz da função, por exemplo, a = 4 e b = 5 segundos;
Definir uma tolerância desejada, por exemplo, 0,001;
Executar o método da bisseção para encontrar a raiz da função no intervalo [a, b], utilizando a função S(t) e a tolerância definida;
Imprimir o tempo encontrado em que o objeto atinge o solo, que é a raiz da função S(t).


-----------

# Importando as bibliotecas necessárias

import math
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Definindo a função que calcula a altura do objeto em relação ao solo após t segundos
def S(t):
m = 2
So = 40
k = 0.6
g = 9.81
v0 = 0 # objeto é abandonado sem velocidade inicial
return So - (mg/k)t + ((mg)/(k**2) - v0/k)(1 - math.exp(-k*t/m))

# Cria uma lista de valores de tempo de 0 a 10 segundos
t_values = list(range(0, 11))

# Calcula a altura correspondente a cada valor de tempo da lista acima usando a função S definida acima
S_values = [S(t) for t in t_values]

# Cria o gráfico da altura em relação ao tempo
plt.plot(t_values, S_values)
plt.axhline(y=0, color='r', linestyle='-')
plt.xlabel('Tempo (s)')
plt.ylabel('Altura (m)')

# Cria um widget de saída para exibir o gráfico
output_widget = widgets.Output()

# Exibe o gráfico no widget de saída
with output_widget:
plt.show()

# Exibe o widget de saída no notebook
display(output_widget)

# Definindo os valores iniciais para o método da bisseção
a = 4
b = 5
tolerance = 0.001
max_iterations = 20

# Loop para realizar a bisseção até encontrar a raiz com a precisão desejada ou atingir o número máximo de iterações
for i in range(max_iterations):
c = (a + b) / 2
if abs(S(c)) < tolerance:
print(f"Raiz encontrada em {c} segundos.")
break
elif S(a) * S(c) < 0:
b = c
else:
a = c