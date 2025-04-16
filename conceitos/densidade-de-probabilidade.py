import sympy as sp
import numpy as np
from typing import Tuple, Union, Dict
from sympy.printing import latex


class PDFValidationError(Exception):
    """Custom exception for PDF validation errors"""
    pass


def verificar_positividade(funcao: sp.Expr, var: str, dominio: Tuple[Union[float, str], Union[float, str]]) -> bool:
    """
    Verifica se a função é não-negativa em todo o domínio.
    
    Args:
        funcao: Expressão simbólica da função
        var: Nome da variável
        dominio: Tupla (min, max) do domínio
        
    Returns:
        bool: True se a função é não-negativa em todo domínio
        
    Raises:
        PDFValidationError: Se a função for negativa em algum ponto
    """
    x = sp.Symbol(var, real=True)
    
    try:
        # Verifica os pontos críticos (derivada = 0)
        derivada = sp.diff(funcao, x)
        pontos_criticos = sp.solve(derivada, x)
        
        # Adiciona extremos do domínio aos pontos de verificação
        pontos_teste = pontos_criticos + [dominio[0], dominio[1]]
        
        # Testa a função em cada ponto
        for ponto in pontos_teste:
            # Convert numeric types to sympy numbers
            if isinstance(ponto, (int, float)):
                ponto = sp.Number(ponto)
            
            # Verifica se o ponto está no domínio
            if (isinstance(ponto, sp.Number) or ponto.is_real) and dominio[0] <= ponto <= dominio[1]:
                valor = funcao.subs(x, ponto)
                # Convert numeric result to sympy number if needed
                if isinstance(valor, (int, float)):
                    valor = sp.Number(valor)
                if (isinstance(valor, sp.Number) or valor.is_real) and valor < 0:
                    raise PDFValidationError(f"Função é negativa em x = {ponto}")
        
        return True
        
    except Exception as e:
        raise PDFValidationError(f"Erro ao verificar positividade: {str(e)}")


def verificar_integral_unitaria(funcao: sp.Expr, var: str, dominio: Tuple[Union[float, str], Union[float, str]], 
                              tolerancia: float = 1e-10) -> bool:
    """
    Verifica se a integral da função no domínio é igual a 1.
    
    Args:
        funcao: Expressão simbólica da função
        var: Nome da variável
        dominio: Tupla (min, max) do domínio
        tolerancia: Tolerância numérica para comparação com 1
        
    Returns:
        bool: True se a integral é aproximadamente 1
        
    Raises:
        PDFValidationError: Se a integral não for aproximadamente 1
    """
    x = sp.Symbol(var, real=True)
    
    try:
        integral = sp.integrate(funcao, (x, dominio[0], dominio[1]))
        valor_numerico = float(integral.evalf())
        
        if abs(valor_numerico - 1) > tolerancia:
            msg = f"Integral da função = {valor_numerico}, deve ser 1"
            raise PDFValidationError(msg)
        
        return True
        
    except Exception as e:
        raise PDFValidationError(f"Erro ao calcular integral: {str(e)}")


def calcular_probabilidade(funcao: sp.Expr, var: str, limite: Tuple[Union[float, str], Union[float, str]]) -> float:
    """
    Calcula a probabilidade P(a ≤ X ≤ b) para a PDF dada.
    
    Args:
        funcao: Expressão simbólica da função
        var: Nome da variável
        limite: Tupla (a, b) dos limites de integração
        
    Returns:
        float: Probabilidade calculada
    """
    x = sp.Symbol(var, real=True)
    
    try:
        prob = sp.integrate(funcao, (x, limite[0], limite[1]))
        return float(prob.evalf())
        
    except Exception as e:
        raise PDFValidationError(f"Erro ao calcular probabilidade: {str(e)}")


def gerar_relatorio_latex(funcao: sp.Expr, var: str, dominio: Tuple[Union[float, str], Union[float, str]], 
                         resultados: Dict) -> str:
    """
    Gera um relatório LaTeX com os resultados da validação.
    
    Args:
        funcao: Expressão simbólica da função
        var: Nome da variável
        dominio: Tupla (min, max) do domínio
        resultados: Dicionário com resultados das verificações
        
    Returns:
        str: Relatório formatado em LaTeX
    """
    x = sp.Symbol(var, real=True)
    relatorio = [
        "\\begin{document}",
        "\\section{Relatório de Validação de PDF}",
        f"\\subsection{{Função Analisada}}",
        f"f({var}) = {latex(funcao)}",
        f"\\subsection{{Domínio}}",
        f"[{latex(dominio[0])}, {latex(dominio[1])}]",
    ]
    
    for chave, valor in resultados.items():
        relatorio.append(f"\\subsection{{{chave}}}")
        relatorio.append(f"{latex(valor)}")
    
    relatorio.append("\\end{document}")
    return "\n".join(relatorio)


def validar_pdf(funcao_str: str, var: str, dominio: Tuple[Union[float, str], Union[float, str]]) -> Dict:
    """
    Função principal que realiza todas as validações da PDF.
    
    Args:
        funcao_str: String representando a função
        var: Nome da variável
        dominio: Tupla (min, max) do domínio
        
    Returns:
        Dict: Resultados das validações e cálculos
    """
    try:
        x = sp.Symbol(var, real=True)
        funcao = sp.sympify(funcao_str)
        
        resultados = {}
        
        # Validação da positividade
        if verificar_positividade(funcao, var, dominio):
            resultados['Positividade'] = "Função é não-negativa em todo domínio"
            
        # Validação da integral unitária
        if verificar_integral_unitaria(funcao, var, dominio):
            resultados['Integral'] = "Integral igual a 1 no domínio"
            
        # Exemplo de cálculo de probabilidade
        p_maior_que = calcular_probabilidade(funcao, var, (2, float('inf')))
        resultados['P(X > 2)'] = p_maior_que
        
        # Gera relatório LaTeX
        relatorio = gerar_relatorio_latex(funcao, var, dominio, resultados)
        resultados['relatorio_latex'] = relatorio
        
        return resultados
        
    except Exception as e:
        raise PDFValidationError(f"Erro na validação da PDF: {str(e)}")


# Exemplo de uso
if __name__ == "__main__":
    # Exemplo 1: Distribuição exponencial
    try:
        funcao_exp = "2 * exp(-2*x)"
        resultados = validar_pdf(funcao_exp, 'x', (0, float('inf')))
        print("Validação bem sucedida para distribuição exponencial:")
        for k, v in resultados.items():
            if k != 'relatorio_latex':
                print(f"{k}: {v}")
    except PDFValidationError as e:
        print(f"Erro na validação: {str(e)}")
    
    # Exemplo 2: Distribuição triangular
    try:
        # Corrigindo a definição da função triangular usando operadores SymPy
        funcao_tri = "Piecewise((2*x, (x >= 0) & (x <= 1/2)), (2*(1-x), (x > 1/2) & (x <= 1)), (0, True))"
        resultados = validar_pdf(funcao_tri, 'x', (0, 1))
        print("\nValidação bem sucedida para distribuição triangular:")
        for k, v in resultados.items():
            if k != 'relatorio_latex':
                print(f"{k}: {v}")
    except PDFValidationError as e:
        print(f"Erro na validação: {str(e)}")