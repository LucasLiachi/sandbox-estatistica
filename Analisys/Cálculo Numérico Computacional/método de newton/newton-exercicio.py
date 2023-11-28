# Função que implementa o método de Newton para encontrar a raiz de uma função f(x)
def newton(f, df, x0, tol):
    xn = x0  # Define a aproximação inicial como x0
    while True:  # Repete o processo até encontrar a raiz com a tolerância desejada
        fxn = f(xn)  # Calcula o valor de f(xn)
        dfxn = df(xn)  # Calcula o valor da derivada de f(xn)
        xn1 = xn - fxn/dfxn  # Calcula a nova aproximação utilizando a fórmula de Newton-Raphson
        if abs(xn1 - xn) < tol:  # Verifica se a tolerância foi atingida
            return xn1  # Retorna a raiz encontrada
        xn = xn1  # Atualiza a aproximação anterior com a nova aproximação encontrada

# Define a função f(x) = x^3 - 4x - 9
def f(x):
    return x**3 - 4*x - 9

# Define a derivada de f(x)
def df(x):
    return 3*x**2 - 4

# Define a aproximação inicial
x0 = 2.5

# Define a tolerância desejada
tol = 1e-2

# Encontra a raiz da função f(x) utilizando o método de Newton com a aproximação inicial x0 e a tolerância tol
raiz = newton(f, df, x0, tol)

# Imprime a raiz encontrada
print(raiz)
