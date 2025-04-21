def interpolar_lagrange(x_interp, x, y):
    """
    Retorna o valor interpolado usando a Interpolação de Lagrange.

    Argumentos:
    x_interp (float): o valor x para o qual o valor y é estimado.
    x (list): uma lista de valores x conhecidos.
    y (list): uma lista de valores y conhecidos correspondentes a x.

    Retorna:
    float: o valor interpolado correspondente a x_interp.
    """
    n = len(x)
    if n != len(y):
        raise ValueError("x e y devem ter o mesmo comprimento.")

    result = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_interp - x[j]) / (x[i] - x[j])
        result += term

    return result

# Dados conhecidos
temperatura = [20, 25, 30, 35]
calor_especifico = [0.99907, 0.99852, 0.99826, 0.99818]

# Estimando o calor específico em uma temperatura de 28 graus Celsius
temperatura_interp = 27.5
calor_especifico_interp = interpolar_lagrange(temperatura_interp, temperatura, calor_especifico)

print(f"O calor específico estimado para {temperatura_interp} graus Celsius é: {calor_especifico_interp}")
