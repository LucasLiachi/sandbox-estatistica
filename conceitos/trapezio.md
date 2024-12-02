## Regra do Trapézio: Conceito e Implementação

A Regra do Trapézio é um método de integração numérica utilizado para aproximar integrais definidas. Sua fórmula matemática é dada por:

$$ \int_{a}^{b} f(x)dx \approx \frac{h}{2}[f(a) + 2f(x_1) + 2f(x_2) + ... + 2f(x_{n-1}) + f(b)] $$

Onde:
- h = (b-a)/n (largura de cada subintervalo)
- n é o número de subintervalos
- [a,b] é o intervalo de integração

### Implementação em Python

Podemos implementar a Regra do Trapézio de duas formas:

1. **Regra do Trapézio Simples**

```python
def trapezoidal_rule_simple(a, b, n):
    h = (b - a) / n
    sum = (f(a) + f(b)) / 2
    for i in range(1, n):
        x = a + i * h
        sum += f(x)
    return h * sum
```

2. **Regra do Trapézio Composta**

A implementação é similar à regra simples, mas é aplicada com diferentes valores de n para melhorar a precisão.

## Características da Regra do Trapézio

- A precisão aumenta com o número de subintervalos (n)
- É mais eficiente para funções suaves
- O erro diminui quadraticamente com o tamanho do intervalo

## Exemplo Prático: Cálculo de Distância

Vamos usar a Regra do Trapézio para calcular a distância percorrida a partir de medições de velocidade:

```python
t = [0, 120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200]  # segundos
v = [20, 22, 23, 25, 30, 31, 32, 40, 45, 50, 65]  # km/h

n = len(t) - 1
h = (t[-1] - t[0]) / n
areas = []

for i in range(n):
    v1, v2 = v[i], v[i+1]
    t1, t2 = t[i], t[i+1]
    area = (v1 + v2) * (t2 - t1) / 2
    areas.append(area)

distancia = sum(areas) * 1000/3600  # conversão para metros
print(f"Aproximação da distância percorrida: {distancia:.0f} metros")
```

**Notas sobre o exemplo:**
- Utiliza velocidades em km/h e tempos em segundos
- A conversão final (1000/3600) transforma km/h para m/s
- O resultado representa a distância total em metros
