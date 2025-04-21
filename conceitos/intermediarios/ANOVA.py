"""
Módulo para Análise de Variância (ANOVA).

Este módulo implementa o teste estatístico ANOVA (Analysis of Variance) 
para comparar médias entre diferentes grupos.

Author: Lucas
Date: 2025
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Union
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_data_groups(data_groups: Dict[str, List[float]]) -> None:
    """
    Valida os dados de entrada para a análise ANOVA.

    Args:
        data_groups: Dicionário com os grupos de dados a serem analisados

    Raises:
        ValueError: Se os dados não atenderem aos critérios de validação
    """
    if not isinstance(data_groups, dict):
        raise ValueError("Os dados devem ser fornecidos como um dicionário")
    
    if len(data_groups) < 2:
        raise ValueError("ANOVA requer pelo menos 2 grupos para comparação")
    
    for group_name, group_data in data_groups.items():
        if not group_data:
            raise ValueError(f"Grupo '{group_name}' está vazio")
        if not all(isinstance(x, (int, float)) for x in group_data):
            raise ValueError(f"Todos os valores no grupo '{group_name}' devem ser numéricos")

def calculate_anova(data_groups: Dict[str, List[float]]) -> pd.DataFrame:
    """
    Realiza a Análise de Variância (ANOVA) para comparar médias entre grupos.

    Esta função implementa ANOVA de um fator, calculando:
    - Soma de Quadrados Total (SQT): Σ(x - média_total)²
    - Soma de Quadrados Entre grupos (SQE): Σ(ni * (média_grupo - média_total)²)
    - Soma de Quadrados Dentro dos grupos (SQD): Σ(x - média_grupo)²
    - Quadrados Médios (QM)
    - Valor F

    Args:
        data_groups: Dicionário onde as chaves são os nomes dos grupos e os valores
                    são listas com as observações de cada grupo

    Returns:
        DataFrame com os resultados da ANOVA, incluindo fontes de variação,
        somas de quadrados, graus de liberdade, quadrados médios e valor F

    Raises:
        ValueError: Se os dados de entrada não forem válidos
    """
    validate_data_groups(data_groups)
    
    # Calculate total mean and observations
    all_data = np.array([item for group in data_groups.values() for item in group])
    total_mean = np.mean(all_data)
    
    # Calculate sums of squares
    sqt = np.sum((all_data - total_mean)**2)
    
    sqd = sum(np.sum((np.array(group) - np.mean(group))**2) 
             for group in data_groups.values())
    
    sqe = sum(len(group) * (np.mean(group) - total_mean)**2 
             for group in data_groups.values())
    
    # Degrees of freedom
    df_between = len(data_groups) - 1
    df_within = len(all_data) - len(data_groups)
    
    # Mean squares
    qme = sqe / df_between
    qmd = sqd / df_within
    
    # F value
    f_value = qme / qmd
    
    return pd.DataFrame({
        'Fonte de Variação': ['Entre Grupos', 'Dentro dos Grupos', 'Total'],
        'Soma de Quadrados (SQ)': [sqe, sqd, sqt],
        'Graus de Liberdade (df)': [df_between, df_within, len(all_data) - 1],
        'Quadrados Médios (QM)': [qme, qmd, '-'],
        'Valor F': [f_value, '-', '-']
    })

if __name__ == "__main__":
    # Exemplo de uso com dados de notas por nível de escolaridade
    data = {
        'fundamental': [30.85, 30.34, 24.90, 31.36, 30.14, 30.69, 23.91, 24.07, 25.96, 25.47, 
                       33.17, 30.39, 33.49, 27.78, 30.25, 23.73, 27.63, 26.38, 25.24, 26.25, 
                       24.28, 31.48, 29.59, 25.97, 31.53, 37.86, 31.44, 28.54, 32.49, 34.11, 
                       28.98, 3.58],
        'medio': [31.01, 25.82, 22.59, 29.66, 26.36, 32.50, 26.27, 26.79, 22.67, 32.11, 
                 26.08, 21.49, 25.29, 26.82],
        'superior': [21.67, 20.39, 28.80, 25.78, 27.88, 25.87, 20.01, 24.83, 21.76, 31.07, 
                    24.81, 3.78]
    }
    
    try:
        result = calculate_anova(data)
        logger.info("\nTabela ANOVA:")
        logger.info("\n" + str(result))
