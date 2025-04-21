"""
Módulo para cálculos de distribuição binomial.

Este módulo implementa funções para calcular probabilidades da distribuição
binomial, incluindo probabilidades pontuais e cumulativas.

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
from typing import Union, List, Dict, Optional
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Exemplos predefinidos
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
    
    @staticmethod
    def _validar_parametros(n: int, p: float) -> None:
        """
        Valida os parâmetros da distribuição binomial.

        Args:
            n: Número de tentativas
            p: Probabilidade de sucesso

        Raises:
            ValueError: Se os parâmetros não forem válidos
        """
        if not isinstance(n, int):
            raise TypeError("n deve ser um número inteiro")
        if n < 0:
            raise ValueError("n deve ser não negativo")
        if not 0 <= p <= 1:
            raise ValueError("p deve estar entre 0 e 1")

    def calcular_coeficiente_binomial(self, k: int) -> int:
        """Calcula o coeficiente binomial C(n,k)."""
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
        plt.legend()
        plt.show()

def calcular_probabilidade_binomial(n: int, k: int, p: float) -> float:
    """Wrapper para cálculo de probabilidade binomial pontual."""
    dist = DistribuicaoBinomial(n, p)
    return dist.pmf(k)

def formatar_resultado(valor: float, decimais: int = 4) -> str:
    """Formata o resultado com o número especificado de casas decimais."""
    return f"{valor:.{decimais}f}"

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
        
        logger.info(f"\n{exemplo['descricao']}:")
        logger.info(f"P(X={k}) = {formatar_resultado(prob)}")
        logger.info(f"P(X≤{k}) = {formatar_resultado(prob_acum)}")
        logger.info(f"Porcentagem (pontual): {prob*100:.2f}%")
        
        # Plotar distribuição
        dist.plotar_distribuicao(exemplo['descricao'])
        
    except Exception as e:
        logger.error(f"Erro ao executar exemplo: {str(e)}")

if __name__ == "__main__":
    try:
        # Executa todos os exemplos
        exemplos = [
            EXEMPLO_1, EXEMPLO_2, EXEMPLO_3,
            EXEMPLO_CONTROLE_QUALIDADE,
            EXEMPLO_CONTROLE_QUALIDADE_ZERO_DEFEITOS
        ]
        
        for exemplo in exemplos:
            executar_exemplo(exemplo)
            
    except Exception as e:
        logger.error(f"Erro na execução: {str(e)}")