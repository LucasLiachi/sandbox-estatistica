import numpy as np
import matplotlib.pyplot as plt
import math

# Try to import ipywidgets for interactive features, but continue if not available
try:
    from ipywidgets import interact, interactive, fixed, interact_manual
    import ipywidgets as widgets
    HAS_WIDGETS = True
except ImportError:
    HAS_WIDGETS = False

def bissecao(f, a, b, eps=1e-6, max_iter=100):
    """
    Implementação genérica do método da bisseção.
    
    Parâmetros:
    f: função que queremos encontrar a raiz
    a, b: intervalo inicial [a,b] que contém a raiz
    eps: tolerância (epsilon) para o critério de parada
    max_iter: número máximo de iterações
    
    Retorna:
    c: aproximação da raiz
    iteracoes: número de iterações realizadas
    historico: lista com o histórico dos valores de c e f(c)
    """
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("A função deve ter sinais opostos nos extremos do intervalo.")
    
    # Inicializar histórico de iterações
    historico = []
    
    iteracao = 0
    while abs(b-a) > eps and iteracao < max_iter:
        c = (a + b) / 2
        fc = f(c)
        
        # Registrar iteração atual
        historico.append({'iteracao': iteracao, 'a': a, 'b': b, 'c': c, 'f(c)': fc})
        
        if abs(fc) < eps:
            return c, iteracao, historico
        elif fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
        iteracao += 1
    
    # Ponto médio do intervalo final como aproximação da raiz
    c = (a + b) / 2
    return c, iteracao, historico

def visualizar_bissecao(f, a, b, eps=1e-6, max_iter=20):
    """
    Visualiza graficamente o processo de convergência do método da bisseção.
    
    Parâmetros:
    f: função que queremos encontrar a raiz
    a, b: intervalo inicial [a,b]
    eps: tolerância para o critério de parada
    max_iter: número máximo de iterações a mostrar
    """
    try:
        # Executar o método da bisseção
        raiz, iteracoes, historico = bissecao(f, a, b, eps, max_iter)
        
        # Criar pontos para o gráfico da função
        x = np.linspace(a - 0.5, b + 0.5, 1000)
        y = [f(xi) for xi in x]
        
        # Configurar gráfico
        plt.figure(figsize=(12, 8))
        plt.plot(x, y, 'b-', label='f(x)')
        plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        plt.grid(True, alpha=0.3)
        
        # Mostrar pontos do histórico
        for i, ponto in enumerate(historico):
            if i == len(historico) - 1:  # último ponto
                plt.plot([ponto['a'], ponto['b']], [f(ponto['a']), f(ponto['b'])], 'ro-', linewidth=2)
                plt.plot(ponto['c'], f(ponto['c']), 'go', markersize=8)
            else:
                plt.plot([ponto['a'], ponto['b']], [f(ponto['a']), f(ponto['b'])], 'ro-', alpha=0.3)
                plt.plot(ponto['c'], f(ponto['c']), 'go', alpha=0.5)
        
        # Adicionar raiz encontrada
        plt.plot(raiz, 0, 'r*', markersize=12, label=f'Raiz ≈ {raiz:.6f}')
        
        plt.title(f'Método da Bisseção - Convergência em {iteracoes} iterações')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.show()
        
        # Mostrar tabela de convergência
        print("\nHistórico de iterações:")
        print("-" * 70)
        print(f"{'Iteração':^10}|{'a':^15}|{'c':^15}|{'b':^15}|{'f(c)':^15}")
        print("-" * 70)
        for ponto in historico:
            print(f"{ponto['iteracao']:^10}|{ponto['a']:^15.6f}|{ponto['c']:^15.6f}|{ponto['b']:^15.6f}|{ponto['f(c)']:^15.6e}")
        print("-" * 70)
        print(f"Raiz encontrada: {raiz:.10f} (após {iteracoes} iterações)")
        
        return raiz, iteracoes
        
    except ValueError as e:
        print(f"Erro: {e}")
        return None, 0

# Exemplo 1: Função polinomial simples
def polinomio_exemplo(x):
    """Função polinomial de exemplo: f(x) = x³ - x - 2"""
    return x**3 - x - 2

# Exemplo 2: Objeto em queda com resistência do ar
def altura_objeto(t, m=2, S0=40, k=0.6, g=9.81):
    """
    Calcula a altura de um objeto em queda com resistência do ar.
    
    Parâmetros:
    t: tempo em segundos
    m: massa do objeto (kg)
    S0: altura inicial (m)
    k: coeficiente de resistência do ar (kg/s)
    g: aceleração da gravidade (m/s²)
    """
    return S0 - ((m*g/k)*t) + (((m*g)/(k**2))*(1 - math.exp(-k*t/m)))

def exemplo_queda(visualizar=True):
    """Exemplo do objeto em queda com resistência do ar."""
    # Criação do gráfico
    t = np.linspace(0, 7, 100)
    S = [altura_objeto(ti) for ti in t]
    
    if visualizar:
        plt.figure(figsize=(10, 6))
        plt.plot(t, S)
        plt.axhline(y=0, color='r', linestyle='-')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Altura (m)')
        plt.title('Altura do objeto em função do tempo')
        plt.grid(True)
        plt.show()
    
    # Encontrar o tempo de queda usando bisseção
    raiz, iteracoes = visualizar_bissecao(altura_objeto, 3, 5, 1e-6, 15)
    if raiz:
        print(f"O objeto atinge o solo em {raiz:.3f} segundos")
    return raiz

# Exemplo 3: Pontuação de jogador de basquete
def pontuacao_jogador(t):
    """
    Função que modela a pontuação de um jogador de basquete em função do tempo.
    Inclui fatores como fadiga (exponencial negativa) e ritmo de jogo (senoidal).
    """
    return 100 * np.sin(np.pi * t / 10) + 1500 * np.exp(-0.1 * t) - 2000

def exemplo_basquete(visualizar=True):
    """Exemplo da pontuação de jogador de basquete."""
    # Criação do gráfico
    t = np.linspace(0, 30, 100)
    pontuacao = [pontuacao_jogador(ti) for ti in t]
    
    if visualizar:
        plt.figure(figsize=(10, 6))
        plt.plot(t, pontuacao)
        plt.axhline(y=0, color='black', linestyle='--')
        plt.xlabel('Tempo (min)')
        plt.ylabel('Pontuação')
        plt.title('Desempenho de um jogador de basquete')
        plt.grid(True)
        plt.show()
    
    # Encontrar o momento em que o jogador atinge determinada pontuação
    try:
        raiz, iteracoes = visualizar_bissecao(pontuacao_jogador, 10, 20, 1e-6, 15)
        if raiz:
            print(f"O jogador atinge a pontuação alvo em {raiz:.2f} minutos")
        return raiz
    except ValueError as e:
        print("Não foi possível encontrar o momento exato: ", e)
        return None

# Exemplo 4: Tempo de entrega de projeto
def tempo_entrega_projeto(num_historias, taxa_base=3, dias_trabalho=5, horas_dia=8, fator_eficiencia=0.6):
    """
    Calcula o tempo necessário para entregar um projeto baseado no número de histórias.
    
    Parâmetros:
    num_historias: número de histórias do projeto
    taxa_base: histórias por semana (valor base)
    dias_trabalho: dias de trabalho por semana
    horas_dia: horas de trabalho por dia
    fator_eficiencia: fator de eficiência da equipe (0 a 1)
    """
    # Taxa em histórias por hora
    taxa_hora = (taxa_base / dias_trabalho / horas_dia) * fator_eficiencia
    
    # Função que representa a diferença entre o tempo estimado e o tempo alvo
    def f(horas):
        return num_historias - taxa_hora * horas
    
    # Encontrar o tempo em horas usando bisseção
    # Estimamos intervalo inicial: entre 10 horas e 1000 horas
    try:
        horas_estimadas, _ = visualizar_bissecao(f, 10, 1000, 0.1, 20)
        if horas_estimadas:
            # Converter para dias e semanas para melhor compreensão
            dias_estimados = horas_estimadas / horas_dia
            semanas_estimadas = dias_estimados / dias_trabalho
            
            print(f"\nTempo estimado para entregar {num_historias} histórias:")
            print(f"Horas: {horas_estimadas:.1f}")
            print(f"Dias úteis: {dias_estimados:.1f}")
            print(f"Semanas: {semanas_estimadas:.1f}")
            
            return horas_estimadas
    except ValueError as e:
        print("Erro ao calcular tempo de entrega: ", e)
        return None

# Interface da linha de comando
if __name__ == "__main__":
    print("=" * 50)
    print("MÉTODO DA BISSEÇÃO - EXEMPLOS DE APLICAÇÃO")
    print("=" * 50)
    print("\nEscolha um exemplo para executar:")
    print("1. Encontrar raiz de função polinomial (x³ - x - 2)")
    print("2. Objeto em queda com resistência do ar")
    print("3. Pontuação de jogador de basquete")
    print("4. Tempo de entrega de projeto")
    print("5. Experimentar com função personalizada")
    print("=" * 50)
    
    try:
        opcao = int(input("\nDigite o número do exemplo (1-5): "))
        
        if opcao == 1:
            visualizar_bissecao(polinomio_exemplo, 1, 2, 1e-6, 10)
            
        elif opcao == 2:
            exemplo_queda()
            
        elif opcao == 3:
            exemplo_basquete()
            
        elif opcao == 4:
            num_historias = int(input("Digite o número de histórias do projeto: "))
            fator_eficiencia = float(input("Digite o fator de eficiência da equipe (0.1 a 1.0): "))
            tempo_entrega_projeto(num_historias, fator_eficiencia=fator_eficiencia)
            
        elif opcao == 5:
            print("\nVamos criar uma função personalizada.")
            print("Por exemplo, para a função 2x² + 3x - 5, você digitaria: 2*x**2 + 3*x - 5")
            
            expr = input("\nDigite a expressão da função (use 'x' como variável): ")
            
            # Criar uma função a partir da expressão
            def funcao_personalizada(x):
                return eval(expr)
            
            a = float(input("Digite o valor de a para o intervalo [a,b]: "))
            b = float(input("Digite o valor de b para o intervalo [a,b]: "))
            
            visualizar_bissecao(funcao_personalizada, a, b, 1e-6, 15)
            
        else:
            print("Opção inválida. Por favor, escolha um número entre 1 e 5.")
    
    except ValueError as e:
        print(f"Erro: {e}")
        print("Por favor, digite um número válido para a opção.")
    except Exception as e:
        print(f"Erro inesperado: {e}")