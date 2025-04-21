"""
Módulo para cálculos de probabilidade e intervalos de confiança.

Este módulo implementa funções estatísticas básicas para análise de dados,
com foco em intervalos de confiança usando a distribuição t de Student.

Author: Lucas
Date: 2025
"""

import numpy as np
from scipy.stats import t
from typing import List, Tuple, Union
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Notas dos alunos para cada professor
notas_professores = [
    [82, 64, 64, 79, 64, 76, 52, 61, 85],  # Professor 1
    [64, 88, 79, 67, 85, 100, 82],         # Professor 2
    [73, 91, 82, 85, 82, 67]               # Professor 3
]

def validar_dados(notas: List[Union[int, float]], nivel_confianca: float) -> None:
    """
    Valida os dados de entrada para o cálculo do intervalo de confiança.

    Args:
        notas (List[Union[int, float]]): Lista de notas a serem validadas
        nivel_confianca (float): Nível de confiança a ser validado

    Raises:
        ValueError: Se os dados não atenderem aos critérios de validação
    """
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia")
    
    if not all(isinstance(x, (int, float)) for x in notas):
        raise ValueError("Todas as notas devem ser números")
        
    if not 0 < nivel_confianca < 1:
        raise ValueError("Nível de confiança deve estar entre 0 e 1")

def calcular_intervalo_confianca(notas: List[Union[int, float]], 
                               nivel_confianca: float = 0.95) -> Tuple[float, float]:
    """
    Calcula o intervalo de confiança para uma média amostral usando a distribuição t de Student.

    Esta função implementa o cálculo do intervalo de confiança baseado na fórmula:
    IC = x̄ ± (t * (s / √n))
    
    Onde:
    - x̄ é a média amostral
    - t é o valor crítico da distribuição t de Student
    - s é o desvio padrão amostral
    - n é o tamanho da amostra

    Args:
        notas (List[Union[int, float]]): Lista de valores numéricos representando a amostra
        nivel_confianca (float, optional): Nível de confiança desejado. Defaults to 0.95.

    Returns:
        Tuple[float, float]: Tupla contendo o limite inferior e superior do intervalo de confiança

    Raises:
        ValueError: Se os dados de entrada não forem válidos
    """
    try:
        validar_dados(notas, nivel_confianca)
        
        media = np.mean(notas)
        desvio_padrao = np.std(notas, ddof=1)  # ddof=1 para usar n-1 (desvio amostral)
        tamanho_amostra = len(notas)
        
        t_valor = t.ppf((1 + nivel_confianca) / 2, df=tamanho_amostra - 1)
        erro_padrao = t_valor * (desvio_padrao / np.sqrt(tamanho_amostra))
        
        return media - erro_padrao, media + erro_padrao
    
    except Exception as e:
        logger.error(f"Erro ao calcular intervalo de confiança: {str(e)}")
        raise

if __name__ == "__main__":
    # Calcular e exibir os intervalos de confiança
    for i, notas in enumerate(notas_professores, 1):
        try:
            lim_inferior, lim_superior = calcular_intervalo_confianca(notas)
            logger.info(f"Professor {i}: IC = ({lim_inferior:.2f}, {lim_superior:.2f})")
        except Exception as e:
            logger.error(f"Erro ao processar notas do Professor {i}: {str(e)}")
