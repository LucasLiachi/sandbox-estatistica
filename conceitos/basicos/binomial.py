"""
Módulo para cálculos de distribuição binomial.

Este módulo implementa funções para calcular probabilidades da distribuição
binomial, incluindo probabilidades pontuais e cumulativas, além de métodos
para visualização gráfica da distribuição.

Fórmula da Distribuição Binomial:
P(X = k) = C(n,k) * p^k * (1-p)^(n-k)

Onde:
- n é o número de tentativas
- k é o número de sucessos
- p é a probabilidade de sucesso em cada tentativa
- C(n,k) é o coeficiente binomial

Author: Lucas
Date: 2025
"""

import math
from typing import Union, List, Dict, Optional, Tuple
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DistribuicaoBinomial:
    """
    Implementa cálculos e visualizações para a distribuição binomial.
    
    Attributes:
        n (int): Número de tentativas
        p (float): Probabilidade de sucesso em cada tentativa
    """
    
    def __init__(self, n: int, p: float):
        """
        Inicializa a distribuição binomial.

        Args:
            n: Número de tentativas
            p: Probabilidade de sucesso em cada tentativa
        """
        self._validar_parametros(n, p)
        self.n = n
        self.p = p
        # Calcular estatísticas
        self.media, self.variancia = self._calcular_estatisticas()
    
    @staticmethod
    def _validar_parametros(n: int, p: float) -> None:
        """
        Valida os parâmetros da distribuição binomial.

        Args:
            n: Número de tentativas
            p: Probabilidade de sucesso

        Raises:
            TypeError: Se n não for inteiro
            ValueError: Se os parâmetros não forem válidos
        """
        if not isinstance(n, int):
            raise TypeError("n deve ser um número inteiro")
        if n < 0:
            raise ValueError("n deve ser não negativo")
        if not 0 <= p <= 1:
            raise ValueError("p deve estar entre 0 e 1")

    def _calcular_estatisticas(self) -> Tuple[float, float]:
        """
        Calcula média e variância da distribuição.

        Returns:
            Tupla com média e variância
        """
        media = self.n * self.p
        variancia = self.n * self.p * (1 - self.p)
        return media, variancia

    def calcular_coeficiente_binomial(self, k: int) -> int:
        """
        Calcula o coeficiente binomial C(n,k).
        
        Args:
            k: Número de sucessos

        Returns:
            Coeficiente binomial C(n,k)
            
        Raises:
            ValueError: Se k for maior que n
        """
        if k > self.n:
            raise ValueError("k não pode ser maior que n")
        return math.comb(self.n, k)

    def pmf(self, k: int) -> float:
        """
        Calcula a função massa de probabilidade P(X = k).
        
        Args:
            k: Número de sucessos

        Returns:
            Probabilidade de exatamente k sucessos
        """
        return binom.pmf(k, self.n, self.p)

    def pmf_manual(self, k: int) -> float:
        """
        Calcula manualmente a função massa de probabilidade P(X = k).
        
        Args:
            k: Número de sucessos

        Returns:
            Probabilidade de exatamente k sucessos
        """
        coef = self.calcular_coeficiente_binomial(k)
        return coef * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k: int) -> float:
        """
        Calcula a função de distribuição acumulada P(X ≤ k).
        
        Args:
            k: Número de sucessos

        Returns:
            Probabilidade acumulada até k sucessos
        """
        return binom.cdf(k, self.n, self.p)

    def sf(self, k: int) -> float:
        """
        Calcula a função de sobrevivência P(X > k).
        
        Args:
            k: Número de sucessos

        Returns:
            Probabilidade de mais que k sucessos
        """
        return 1 - self.cdf(k)

    def plotar_distribuicao(self, titulo: Optional[str] = None) -> None:
        """
        Plota a distribuição de probabilidade.
        
        Args:
            titulo: Título opcional para o gráfico
        """
        k = np.arange(0, self.n + 1)
        prob = binom.pmf(k, self.n, self.p)
        
        plt.figure(figsize=(10, 6))
        plt.bar(k, prob, alpha=0.8, color='b', label=f'n={self.n}, p={self.p}')
        plt.title(titulo or f'Distribuição Binomial (n={self.n}, p={self.p})')
        plt.xlabel('Número de Sucessos (k)')
        plt.ylabel('Probabilidade')
        plt.grid(True, alpha=0.3)
        plt.xticks(k)
        plt.legend()
        plt.show()

    def calcular_tabela_probabilidades(self) -> Dict[int, float]:
        """
        Calcula uma tabela de probabilidades para todos os valores possíveis de k.
        
        Returns:
            Dicionário com as probabilidades para cada valor de k
        """
        return {k: self.pmf(k) for k in range(self.n + 1)}

    def resumo(self) -> None:
        """Imprime um resumo das estatísticas da distribuição."""
        print(f"Distribuição Binomial com n={self.n}, p={self.p}")
        print(f"Média (μ): {self.media}")
        print(f"Variância (σ²): {self.variancia}")
        print(f"Desvio Padrão (σ): {np.sqrt(self.variancia)}")
        print("\nTabela de probabilidades:")
        print("k\tP(X=k)")
        for k in range(self.n + 1):
            print(f"{k}\t{self.pmf(k):.4f}")


# Método de Newton para encontrar raízes
def newton(f, df, x0, tol=1e-6, max_iter=100):
    """
    Implementa o método de Newton para encontrar a raiz de uma função.
    
    Args:
        f: A função cuja raiz queremos encontrar
        df: A derivada da função f
        x0: Aproximação inicial
        tol: Tolerância de convergência
        max_iter: Número máximo de iterações
    
    Returns:
        A raiz da função
    """
    xn = x0  # Define a aproximação inicial
    for i in range(max_iter):
        fxn = f(xn)
        dfxn = df(xn)
        
        if abs(dfxn) < 1e-10:
            raise ValueError("Derivada muito próxima de zero. O método pode não convergir.")
            
        xn1 = xn - fxn/dfxn  # Fórmula de Newton-Raphson
        
        if abs(xn1 - xn) < tol:  # Verifica se a tolerância foi atingida
            return xn1
            
        xn = xn1  # Atualiza para a nova aproximação
    
    # Se chegou aqui, atingiu o número máximo de iterações
    raise ValueError(f"O método não convergiu após {max_iter} iterações.")


def calcular_probabilidade_binomial(n: int, k: int, p: float) -> float:
    """
    Wrapper para cálculo de probabilidade binomial pontual.
    
    Args:
        n: Número de tentativas
        k: Número de sucessos
        p: Probabilidade de sucesso em cada tentativa
    
    Returns:
        Probabilidade binomial P(X = k)
    """
    dist = DistribuicaoBinomial(n, p)
    return dist.pmf(k)


def formatar_resultado(valor: float, decimais: int = 4) -> str:
    """
    Formata o resultado com o número especificado de casas decimais.
    
    Args:
        valor: Valor a ser formatado
        decimais: Número de casas decimais
    
    Returns:
        String formatada
    """
    return f"{valor:.{decimais}f}"


def analisar_distribuicao_binomial(n: int = 5, p: float = 0.5):
    """
    Analisa e plota uma distribuição binomial para os parâmetros dados.
    
    Args:
        n: Número de tentativas
        p: Probabilidade de sucesso em cada tentativa
    """
    dist = DistribuicaoBinomial(n, p)
    
    # Imprimir resumo
    dist.resumo()
    
    # Plotar distribuição
    dist.plotar_distribuicao()


# Exemplos predefinidos
EXEMPLOS = [
    {
        "n": 5,
        "k": 3,
        "p": 0.5,
        "descricao": "Exemplo básico com moeda justa (p=1/2)"
    },
    {
        "n": 10,
        "k": 5,
        "p": 0.5,
        "descricao": "Lançamento de moeda justa 10 vezes"
    },
    {
        "n": 6,
        "k": 3,
        "p": 0.25,
        "descricao": "Eventos com probabilidade de 1/4"
    },
    {
        "n": 6,
        "k": 2,
        "p": 0.1,
        "descricao": "Controle de qualidade - Probabilidade de 2 peças defeituosas em 6"
    },
    {
        "n": 10,
        "k": 0,
        "p": 0.05,
        "descricao": "Controle de qualidade - Probabilidade de nenhuma peça defeituosa em 10"
    },
]


def executar_exemplo(exemplo: dict) -> None:
    """
    Executa um exemplo de cálculo de probabilidade binomial.
    
    Args:
        exemplo: Dicionário com parâmetros do exemplo
    """
    try:
        n, k, p = exemplo["n"], exemplo["k"], exemplo["p"]
        dist = DistribuicaoBinomial(n, p)
        
        prob = dist.pmf(k)
        prob_acum = dist.cdf(k)
        
        print(f"\n{exemplo['descricao']}:")
        print(f"P(X={k}) = {formatar_resultado(prob)}")
        print(f"P(X≤{k}) = {formatar_resultado(prob_acum)}")
        print(f"P(X>{k}) = {formatar_resultado(dist.sf(k))}")
        print(f"Porcentagem (pontual): {prob*100:.2f}%")
        
        # Plotar distribuição
        dist.plotar_distribuicao(exemplo['descricao'])
        
    except Exception as e:
        print(f"Erro ao executar exemplo: {str(e)}")


if __name__ == "__main__":
    try:
        # Executa todos os exemplos
        for exemplo in EXEMPLOS:
            executar_exemplo(exemplo)
            
    except Exception as e:
        print(f"Erro na execução: {str(e)}")