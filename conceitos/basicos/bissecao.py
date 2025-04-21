import numpy as np
import matplotlib.pyplot as plt
import math

# Try to import ipywidgets for interactive features, but continue if not available
try:
    from ipywidgets import interact, interactive, fixed, interact_manual, Output
    import ipywidgets as widgets
    HAS_WIDGETS = True
except ImportError:
    HAS_WIDGETS = False

def bissecao(f, a, b, eps=1e-6):
    """
    Implementação genérica do método da bisseção.
    
    Parâmetros:
    f: função que queremos encontrar a raiz
    a, b: intervalo inicial [a,b] que contém a raiz
    eps: tolerância (epsilon) para o critério de parada
    
    Retorna:
    c: aproximação da raiz
    """
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("A função deve ter sinais opostos nos extremos do intervalo.")
    
    while abs(b-a) > eps:
        c = (a + b) / 2
        fc = f(c)
        if fc == 0:
            return c
        elif fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (a + b) / 2

# Exemplo 1: Objeto em queda com resistência do ar
def altura_objeto(t, m=2, S0=40, k=0.6, g=9.81, v0=0):
    """
    Calcula a altura de um objeto em queda com resistência do ar.
    
    Parâmetros:
    t: tempo em segundos
    m: massa do objeto (kg)
    S0: altura inicial (m)
    k: coeficiente de resistência do ar (kg/s)
    g: aceleração da gravidade (m/s²)
    v0: velocidade inicial (m/s)
    """
    return S0 - ((m*g/k)*t) + (((m*g)/(k**2))*(1 - math.exp(-k*t/m)))

def exemplo_queda():
    # Criação do gráfico
    t = np.linspace(0, 7, 100)
    S = [altura_objeto(ti) for ti in t]
    
    plt.figure(figsize=(10, 6))
    plt.plot(t, S)
    plt.axhline(y=0, color='r', linestyle='-')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Altura (m)')
    plt.title('Altura do objeto em função do tempo')
    plt.grid(True)
    
    # Encontrar o tempo de queda usando bisseção
    raiz = bissecao(altura_objeto, 4, 5, 0.001)
    print(f"O objeto atinge o solo em {raiz:.3f} segundos")
    plt.show()

# Exemplo 2: Pontuação de jogador de basquete
def pontuacao_jogador(t):
    """
    Função que modela a pontuação de um jogador de basquete em função do tempo.
    Inclui fatores como fadiga (exponencial negativa) e ritmo de jogo (senoidal).
    """
    return 100 * np.sin(np.pi * t / 10) + 1500 * np.exp(-0.1 * t) - 2000

def exemplo_basquete():
    # Criação do gráfico
    t = np.linspace(0, 30, 100)
    
    plt.figure(figsize=(10, 6))
    plt.plot(t, pontuacao_jogador(t))
    plt.axhline(y=0, color='black', linestyle='--')
    plt.xlabel('Tempo (min)')
    plt.ylabel('Pontuação')
    plt.title('Desempenho de um jogador de basquete')
    plt.grid(True)
    
    # Encontrar o momento em que o jogador atinge determinada pontuação
    try:
        raiz = bissecao(pontuacao_jogador, 10, 20, 1e-6)
        print(f"O jogador atinge a pontuação alvo em {raiz:.2f} minutos")
    except ValueError as e:
        print("Não foi possível encontrar o momento exato: ", e)
    plt.show()

# Exemplo 3: Tempo de entrega de projeto
def tempo_entrega_projeto(num_historias, taxa=0.1042):
    """
    Calcula o tempo necessário para entregar um projeto baseado no número de histórias.
    
    Parâmetros:
    num_historias: número de histórias do projeto
    taxa: taxa de conclusão de histórias por unidade de tempo
    """
    def f(x):
        return num_historias / (taxa * x) - 1
    
    try:
        tempo = bissecao(f, 100, 300, 1e-6)
        print(f"Tempo estimado para entregar {num_historias} histórias: {tempo:.2f} horas")
        return tempo
    except ValueError as e:
        print("Erro ao calcular tempo de entrega: ", e)
        return None

if __name__ == "__main__":
    print("Escolha um exemplo para executar:")
    print("1. Objeto em queda com resistência do ar")
    print("2. Pontuação de jogador de basquete")
    print("3. Tempo de entrega de projeto")
    
    opcao = input("Digite o número do exemplo (1-3): ")
    
    if opcao == "1":
        exemplo_queda()
    elif opcao == "2":
        exemplo_basquete()
    elif opcao == "3":
        num_historias = int(input("Digite o número de histórias do projeto: "))
        tempo_entrega_projeto(num_historias)