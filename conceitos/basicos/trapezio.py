import math
import numpy as np

# =====================================
# Definição das funções de integração
# =====================================

def f(t):
    """
    Função de exemplo para calcular a integral: sin(π*t²/2)
    
    Args:
        t (float): Valor de entrada
        
    Returns:
        float: Valor da função no ponto t
    """
    return math.sin(math.pi * t**2/2)

def trapezoidal_rule_simple(f, a, b, n):
    """
    Implementação da regra do trapézio simples.
    
    Args:
        f (function): A função a ser integrada
        a (float): Limite inferior da integração
        b (float): Limite superior da integração
        n (int): Número de subintervalos
    
    Returns:
        float: Aproximação da integral definida
    """
    h = (b - a) / n
    sum_value = (f(a) + f(b)) / 2
    for i in range(1, n):
        x = a + i * h
        sum_value += f(x)
    return h * sum_value

def trapezoidal_rule_composite(f, a, b, n):
    """
    Implementação da regra do trapézio composta usando numpy para vetorização.
    
    Args:
        f (function): A função a ser integrada
        a (float): Limite inferior da integração
        b (float): Limite superior da integração
        n (int): Número de subintervalos
    
    Returns:
        float: Aproximação da integral definida
    """
    # Cria um array com os pontos de avaliação
    x = np.linspace(a, b, n+1)
    # Avalia a função em todos os pontos
    y = np.array([f(xi) for xi in x])
    
    # Aplica a regra do trapézio
    area = (b - a) / (2 * n) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return area

def calculate_distance_from_velocity(times, velocities):
    """
    Calcula a distância percorrida a partir de dados de tempo e velocidade
    usando a regra do trapézio.
    
    Args:
        times (list): Lista de tempos em segundos
        velocities (list): Lista de velocidades em km/h
    
    Returns:
        float: Distância calculada em metros
    """
    if len(times) != len(velocities):
        raise ValueError("Os arrays de tempo e velocidade devem ter o mesmo tamanho")
    
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

# =====================================
# Exemplos de uso
# =====================================

if __name__ == "__main__":
    # Exemplo 1: Cálculo da integral de f(t) = sin(π*t²/2)
    a = 0
    b = 2 - math.sqrt(2)
    
    # Usando a regra do trapézio simples
    integral_simple = trapezoidal_rule_simple(f, a, b, 1)
    print(f"Integral usando a regra do trapézio simples: {integral_simple:.6f}")
    
    # Usando a regra do trapézio composta com diferentes números de trapézios
    for n in [3, 5, 10, 20, 60]:
        integral_composite = trapezoidal_rule_composite(f, a, b, n)
        print(f"Integral usando a regra do trapézio composta com {n} trapézios: {integral_composite:.10f}")
    
    # Exemplo 2: Cálculo de distância a partir de velocidades
    t = [0, 120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200]  # tempos em segundos
    v = [20, 22, 23, 25, 30, 31, 32, 40, 45, 50, 65]  # velocidades em km/h
    
    distancia = calculate_distance_from_velocity(t, v)
    print(f"\nAproximação da distância percorrida: {distancia:.0f} metros")

