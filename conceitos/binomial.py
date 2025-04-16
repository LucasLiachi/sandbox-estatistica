import math
from typing import Union

# Variáveis globais para os exemplos
EXEMPLO_1 = {
    "n": 5,
    "k": 3,
    "p": 0.5,
    "descricao": "Exemplo básico com p=1/2"
}

EXEMPLO_2 = {
    "n": 10,
    "k": 5,
    "p": 0.5,
    "descricao": "Teste adicional com p=1/2"
}

EXEMPLO_3 = {
    "n": 6,
    "k": 3,
    "p": 0.25,  # 1/4
    "descricao": "Probabilidade de olhos verdes"
}

EXEMPLO_CONTROLE_QUALIDADE = {
    "n": 6,
    "k": 2,
    "p": 0.1,  # 10% de chance de defeito por peça
    "descricao": "Controle de qualidade industrial - Probabilidade de 2 peças defeituosas em 6"
}

EXEMPLO_CONTROLE_QUALIDADE_ZERO_DEFEITOS = {
    "n": 10,
    "k": 0,
    "p": 0.05,  # 5% de chance de defeito por peça
    "descricao": "Controle de qualidade - Probabilidade de nenhuma peça defeituosa em 10"
}

def calcular_coeficiente_binomial(n: int, k: int) -> int:
    """
    Calcula o coeficiente binomial C(n,k) = n!/(k!(n-k)!)
    
    Args:
        n (int): número total de elementos
        k (int): número de elementos a serem escolhidos
        
    Returns:
        int: coeficiente binomial C(n,k)
        
    Raises:
        ValueError: se k > n ou se n ou k forem negativos
        TypeError: se n ou k não forem inteiros
    """
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("n e k devem ser números inteiros")
    
    if n < 0 or k < 0:
        raise ValueError("n e k devem ser não negativos")
        
    if k > n:
        raise ValueError("k não pode ser maior que n")
    
    return math.floor(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))

def calcular_probabilidade_binomial(n: int, k: int, p: float) -> float:
    """
    Calcula a probabilidade binomial P(X=k) para n tentativas com probabilidade p
    
    Args:
        n (int): número total de tentativas
        k (int): número de sucessos desejados
        p (float): probabilidade de sucesso em cada tentativa
        
    Returns:
        float: probabilidade de obter exatamente k sucessos em n tentativas
        
    Raises:
        ValueError: se p não estiver entre 0 e 1, ou outras condições inválidas
    """
    if not 0 <= p <= 1:
        raise ValueError("p deve estar entre 0 e 1")
    
    coef = calcular_coeficiente_binomial(n, k)
    prob = coef * (p ** k) * ((1 - p) ** (n - k))
    return prob

def formatar_resultado(valor: float, decimais: int = 4) -> str:
    """
    Formata o resultado com o número especificado de casas decimais
    
    Args:
        valor (float): valor a ser formatado
        decimais (int): número de casas decimais (padrão 4)
        
    Returns:
        str: valor formatado com o número especificado de casas decimais
    """
    return f"{valor:.{decimais}f}"

def executar_exemplo(exemplo: dict) -> None:
    """
    Executa um exemplo de cálculo de probabilidade binomial
    
    Args:
        exemplo (dict): dicionário contendo os parâmetros do exemplo
    """
    n, k, p = exemplo["n"], exemplo["k"], exemplo["p"]
    prob = calcular_probabilidade_binomial(n, k, p)
    resultado = formatar_resultado(prob)
    
    print(f"\n{exemplo['descricao']}:")
    print(f"P(X={k}) = {resultado}")
    print(f"Porcentagem: {float(resultado)*100:.2f}%")

if __name__ == "__main__":
    try:
        # Executa todos os exemplos
        for exemplo in [EXEMPLO_1, EXEMPLO_2, EXEMPLO_3, EXEMPLO_CONTROLE_QUALIDADE, EXEMPLO_CONTROLE_QUALIDADE_ZERO_DEFEITOS]:
            executar_exemplo(exemplo)
            
    except (ValueError, TypeError) as e:
        print(f"Erro: {str(e)}")