## Regra do Trapézio: Conceito e Implementação

A Regra do Trapézio é um método de integração numérica utilizado para aproximar integrais definidas. Sua fórmula matemática é dada por:

$$ \int_{a}^{b} f(x)dx \approx \frac{h}{2}[f(a) + 2f(x_1) + 2f(x_2) + ... + 2f(x_{n-1}) + f(b)] $$

Onde:
- h = (b-a)/n (largura de cada subintervalo)
- n é o número de subintervalos
- [a,b] é o intervalo de integração

### Fundamento Matemático

A Regra do Trapézio baseia-se na aproximação da função por segmentos lineares, formando trapézios. Para cada subintervalo [x_i, x_{i+1}], a área é calculada como:

$$ A_i = \frac{h}{2}[f(x_i) + f(x_{i+1})] $$

A soma de todas essas áreas fornece a aproximação da integral:

$$ \int_{a}^{b} f(x)dx \approx \sum_{i=0}^{n-1} A_i $$

### Implementação em Python

Podemos implementar a Regra do Trapézio de duas formas:

#### 1. Regra do Trapézio Simples

```python
def trapezoidal_rule_simple(f, a, b, n):
    h = (b - a) / n
    sum_value = (f(a) + f(b)) / 2
    for i in range(1, n):
        x = a + i * h
        sum_value += f(x)
    return h * sum_value
```

#### 2. Regra do Trapézio Composta

```python
def trapezoidal_rule_composite(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = np.array([f(xi) for xi in x])
    
    area = (b - a) / (2 * n) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return area
```

## Análise de Erro

O erro na Regra do Trapézio é proporcional à segunda derivada da função e ao quadrado do tamanho do subintervalo:

$$ \text{Erro} \approx -\frac{(b-a)^3}{12n^2} f''(\xi) $$

Onde $\xi$ é algum ponto no intervalo [a,b]. Este resultado mostra que:

1. O erro decresce com o quadrado do número de subintervalos (ordem O(h²))
2. Funções com grandes valores absolutos para a segunda derivada terão maior erro

## Características da Regra do Trapézio

- A precisão aumenta com o número de subintervalos (n)
- É mais eficiente para funções suaves
- O erro diminui quadraticamente com o tamanho do intervalo
- É computacionalmente mais eficiente que métodos de ordem superior para funções que são caras de avaliar

## Exemplo Prático: Cálculo de Distância

Vamos usar a Regra do Trapézio para calcular a distância percorrida a partir de medições de velocidade:

```python
def calculate_distance_from_velocity(times, velocities):
    n = len(times) - 1  # número de intervalos
    areas = []
    
    for i in range(n):
        v1, v2 = velocities[i], velocities[i+1]  # velocidades nos pontos
        t1, t2 = times[i], times[i+1]  # tempos nos pontos
        area = (v1 + v2) * (t2 - t1) / 2  # área do trapézio
        areas.append(area)
    
    # Convertendo para metros (km/h * s * 1000/3600 = m)
    distance = sum(areas) * 1000/3600
    return distance
```

### Exemplo de Aplicação:

```python
t = [0, 120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200]  # segundos
v = [20, 22, 23, 25, 30, 31, 32, 40, 45, 50, 65]  # km/h

distancia = calculate_distance_from_velocity(t, v)
print(f"Aproximação da distância percorrida: {distancia:.0f} metros")
```

**Notas sobre o exemplo:**
- Utiliza velocidades em km/h e tempos em segundos
- A conversão final (1000/3600) transforma km·h para m·s
- O resultado representa a distância total em metros

## Comparação com Outros Métodos

A Regra do Trapézio é um método de segunda ordem (O(h²)). Outros métodos de integração numérica incluem:

1. **Regra do Retângulo (Método do Ponto Médio)** - Ordem O(h²)
2. **Regra de Simpson** - Ordem O(h⁴)
3. **Quadratura de Gauss** - Ordem O(h²ⁿ) para n pontos

Para funções suaves, a Regra de Simpson geralmente fornece melhores resultados que a Regra do Trapézio com o mesmo número de avaliações da função.
