import numpy as np
from sklearn.linear_model import LinearRegression

def encontrar_intercepto_y(posse_bola, pontos, x0=1):
    """
    Usa o método de Newton para encontrar a interceptação com o eixo y da equação
    da regressão linear, que é o ponto onde x=0.
    
    Args:
        posse_bola (list): Lista com os percentuais de posse de bola dos jogos.
        pontos (list): Lista com a pontuação dos jogos.
        x0 (float): Valor inicial para a busca da raiz.
    
    Returns:
        float: Valor da interceptação com o eixo y.
    """
    # Calcula a inclinação da reta usando a regressão linear
    modelo = LinearRegression().fit(np.array(posse_bola).reshape(-1, 1), np.array(pontos))
    inclinacao = modelo.coef_[0]

    # Define a função que representa a equação da reta
    def f(x):
        return inclinacao*x + modelo.intercept_

    # Define a derivada da função que representa a equação da reta
    def df(x):
        return inclinacao

    # Usa o método de Newton para encontrar a raiz da equação da reta
    x_novo = x0
    x_anterior = x0 + 1
    while abs(x_novo - x_anterior) > 1e-6:
        x_anterior = x_novo
        x_novo = x_anterior - f(x_anterior) / df(x_anterior)

    # Retorna a interceptação com o eixo y (valor de y quando x=0)
    return f(0)

def encontrar_intercepto_y(posse_bola, pontos, x0=1):
    """
    Usa o método de Newton para encontrar a interceptação com o eixo y da equação
    da regressão linear, que é o ponto onde x=0.
    
    Args:
        posse_bola (list): Lista com os percentuais de posse de bola dos jogos.
        pontos (list): Lista com a pontuação dos jogos.
        x0 (float): Valor inicial para a busca da raiz.
    
    Returns:
        float: Valor da interceptação com o eixo y.
    """
    # Calcula a inclinação da reta usando a regressão linear
    modelo = LinearRegression().fit(np.array(posse_bola).reshape(-1, 1), np.array(pontos))
    inclinacao = modelo.coef_[0]

    # Define a função que representa a equação da reta
    def f(x):
        return inclinacao*x + modelo.intercept_

    # Define a derivada da função que representa a equação da reta
    def df(x):
        return inclinacao

    # Usa o método de Newton para encontrar a raiz da equação da reta
    x_novo = x0
    x_anterior = x0 + 1
    while abs(x_novo - x_anterior) > 1e-6:
        x_anterior = x_novo
        x_novo = x_anterior - f(x_anterior) / df(x_anterior)

    # Retorna a interceptação com o eixo y (valor de y quando x=0)
    return f(0)

