"""
Módulo para cálculos de probabilidade e intervalos de confiança.

Este módulo implementa funções estatísticas básicas para análise de dados,
incluindo cálculos de probabilidade, intervalos de confiança e estatísticas descritivas.

Author: Lucas
Date: 2025
"""

import numpy as np
from scipy import stats
from typing import List, Tuple, Union, Dict, Optional
import logging
import matplotlib.pyplot as plt
import seaborn as sns

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Dados de exemplo 
NOTAS_PROFESSORES = [
    [82, 64, 64, 79, 64, 76, 52, 61, 85],  # Professor 1
    [64, 88, 79, 67, 85, 100, 82],         # Professor 2
    [73, 91, 82, 85, 82, 67]               # Professor 3
]

def validar_dados(dados: List[Union[int, float]], nivel_confianca: float = 0.95) -> None:
    """
    Valida os dados de entrada para cálculos estatísticos.

    Args:
        dados (List[Union[int, float]]): Lista de valores numéricos
        nivel_confianca (float): Nível de confiança (entre 0 e 1)

    Raises:
        ValueError: Se os dados não atenderem aos critérios de validação
    """
    if not dados:
        raise ValueError("A lista de dados não pode estar vazia")
    
    if not all(isinstance(x, (int, float)) for x in dados):
        raise ValueError("Todos os valores devem ser números")
        
    if not 0 < nivel_confianca < 1:
        raise ValueError("Nível de confiança deve estar entre 0 e 1")

def calcular_intervalo_confianca(dados: List[Union[int, float]], 
                               nivel_confianca: float = 0.95) -> Tuple[float, float]:
    """
    Calcula o intervalo de confiança para uma média amostral usando a distribuição t de Student.

    Esta função implementa o cálculo do intervalo de confiança baseado na fórmula:
    IC = x̄ ± (t * (s / √n))
    
    Args:
        dados (List[Union[int, float]]): Lista de valores numéricos representando a amostra
        nivel_confianca (float, optional): Nível de confiança desejado. Defaults to 0.95.

    Returns:
        Tuple[float, float]: Tupla contendo o limite inferior e superior do intervalo de confiança

    Raises:
        ValueError: Se os dados de entrada não forem válidos
    """
    try:
        validar_dados(dados, nivel_confianca)
        
        media = np.mean(dados)
        desvio_padrao = np.std(dados, ddof=1)  # ddof=1 para usar n-1 (desvio amostral)
        tamanho_amostra = len(dados)
        
        t_valor = stats.t.ppf((1 + nivel_confianca) / 2, df=tamanho_amostra - 1)
        erro_padrao = t_valor * (desvio_padrao / np.sqrt(tamanho_amostra))
        
        return media - erro_padrao, media + erro_padrao
    
    except Exception as e:
        logger.error(f"Erro ao calcular intervalo de confiança: {str(e)}")
        raise

def calcular_probabilidade_evento(casos_favoraveis: int, casos_possiveis: int) -> float:
    """
    Calcula a probabilidade de um evento baseado na definição clássica de Laplace.
    
    Args:
        casos_favoraveis (int): Número de casos favoráveis ao evento
        casos_possiveis (int): Número total de casos possíveis
        
    Returns:
        float: Probabilidade do evento (entre 0 e 1)
        
    Raises:
        ValueError: Se os parâmetros forem inválidos
    """
    if casos_possiveis <= 0:
        raise ValueError("O número de casos possíveis deve ser maior que zero")
    
    if casos_favoraveis < 0 or casos_favoraveis > casos_possiveis:
        raise ValueError("O número de casos favoráveis deve estar entre 0 e o número de casos possíveis")
    
    return casos_favoraveis / casos_possiveis

def calcular_probabilidade_normal(x: float, 
                                media: float = 0, 
                                desvio_padrao: float = 1, 
                                cauda: str = 'inferior') -> float:
    """
    Calcula a probabilidade de uma variável aleatória normal.
    
    Args:
        x (float): Valor para calcular a probabilidade
        media (float): Média da distribuição normal. Defaults to 0.
        desvio_padrao (float): Desvio padrão da distribuição normal. Defaults to 1.
        cauda (str): Tipo de probabilidade a calcular: 'inferior' (P(X ≤ x)), 
                    'superior' (P(X > x)) ou 'entre' (requer parâmetro adicional). Defaults to 'inferior'.
        
    Returns:
        float: Probabilidade calculada
        
    Raises:
        ValueError: Se os parâmetros forem inválidos
    """
    if desvio_padrao <= 0:
        raise ValueError("O desvio padrão deve ser maior que zero")
    
    if cauda not in ['inferior', 'superior']:
        raise ValueError("O parâmetro 'cauda' deve ser 'inferior' ou 'superior'")
    
    if cauda == 'inferior':
        return stats.norm.cdf(x, loc=media, scale=desvio_padrao)
    else:  # cauda superior
        return 1 - stats.norm.cdf(x, loc=media, scale=desvio_padrao)

def calcular_probabilidade_entre(a: float, b: float, 
                                media: float = 0, 
                                desvio_padrao: float = 1) -> float:
    """
    Calcula a probabilidade de uma variável aleatória normal estar entre dois valores.
    
    Args:
        a (float): Limite inferior do intervalo
        b (float): Limite superior do intervalo
        media (float): Média da distribuição normal. Defaults to 0.
        desvio_padrao (float): Desvio padrão da distribuição normal. Defaults to 1.
        
    Returns:
        float: Probabilidade de a ≤ X ≤ b
        
    Raises:
        ValueError: Se os parâmetros forem inválidos
    """
    if a > b:
        raise ValueError("O limite inferior 'a' deve ser menor ou igual ao limite superior 'b'")
        
    if desvio_padrao <= 0:
        raise ValueError("O desvio padrão deve ser maior que zero")
    
    # P(a ≤ X ≤ b) = P(X ≤ b) - P(X < a)
    return stats.norm.cdf(b, loc=media, scale=desvio_padrao) - stats.norm.cdf(a, loc=media, scale=desvio_padrao)

def calcular_estatisticas_descritivas(dados: List[Union[int, float]]) -> Dict[str, float]:
    """
    Calcula estatísticas descritivas básicas para um conjunto de dados.
    
    Args:
        dados (List[Union[int, float]]): Lista de valores numéricos
        
    Returns:
        Dict[str, float]: Dicionário com estatísticas descritivas
    """
    validar_dados(dados)
    
    return {
        'média': np.mean(dados),
        'mediana': np.median(dados),
        'desvio_padrão': np.std(dados, ddof=1),
        'variância': np.var(dados, ddof=1),
        'mínimo': np.min(dados),
        'máximo': np.max(dados),
        'amplitude': np.max(dados) - np.min(dados),
        'tamanho_amostra': len(dados),
        'primeiro_quartil': np.percentile(dados, 25),
        'terceiro_quartil': np.percentile(dados, 75),
        'intervalo_interquartil': np.percentile(dados, 75) - np.percentile(dados, 25)
    }

def visualizar_distribuicao_com_ic(dados: List[Union[int, float]], 
                                  nivel_confianca: float = 0.95, 
                                  titulo: str = 'Distribuição com Intervalo de Confiança',
                                  exibir: bool = True) -> Optional[plt.Figure]:
    """
    Cria uma visualização da distribuição dos dados com intervalo de confiança.
    
    Args:
        dados (List[Union[int, float]]): Lista de valores numéricos
        nivel_confianca (float): Nível de confiança para o intervalo. Defaults to 0.95.
        titulo (str): Título do gráfico. Defaults to 'Distribuição com Intervalo de Confiança'.
        exibir (bool): Se True, exibe o gráfico; se False, retorna a figura. Defaults to True.
        
    Returns:
        Optional[plt.Figure]: Objeto figura se exibir=False, None caso contrário
    """
    validar_dados(dados, nivel_confianca)
    
    ic_inf, ic_sup = calcular_intervalo_confianca(dados, nivel_confianca)
    media = np.mean(dados)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(dados, kde=True, bins='auto', ax=ax)
    ax.axvline(media, color='red', linestyle='--', label='Média')
    ax.axvline(ic_inf, color='green', linestyle=':', label=f'IC Inferior ({nivel_confianca*100:.0f}%)')
    ax.axvline(ic_sup, color='green', linestyle=':', label=f'IC Superior ({nivel_confianca*100:.0f}%)')
    ax.set_title(titulo)
    ax.set_xlabel('Valores')
    ax.set_ylabel('Frequência')
    ax.legend()
    
    # Adicionar anotação com os valores
    texto = f"Média: {media:.2f}\nIC {nivel_confianca*100:.0f}%: ({ic_inf:.2f}, {ic_sup:.2f})"
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.05, 0.95, texto, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=props)
    
    if exibir:
        plt.show()
        return None
    else:
        return fig

def simular_lancamentos_dado(n_lancamentos: int = 1000, n_faces: int = 6, seed: Optional[int] = None) -> List[int]:
    """
    Simula múltiplos lançamentos de um dado.
    
    Args:
        n_lancamentos (int): Número de lançamentos a simular. Defaults to 1000.
        n_faces (int): Número de faces do dado. Defaults to 6.
        seed (Optional[int]): Semente para o gerador de números aleatórios. Defaults to None.
        
    Returns:
        List[int]: Lista com os resultados dos lançamentos
    """
    if seed is not None:
        np.random.seed(seed)
        
    return list(np.random.randint(1, n_faces + 1, n_lancamentos))

def simular_intervalos_confianca(media_populacional: float,
                               desvio_populacional: float,
                               tamanho_amostra: int,
                               num_amostras: int,
                               nivel_confianca: float = 0.95,
                               seed: Optional[int] = None) -> Tuple[List[Tuple[float, float]], List[bool]]:
    """
    Simula múltiplas amostras e calcula intervalos de confiança para demonstrar
    empiricamente a interpretação do intervalo de confiança.
    
    Args:
        media_populacional (float): Média da população
        desvio_populacional (float): Desvio padrão da população
        tamanho_amostra (int): Tamanho de cada amostra
        num_amostras (int): Número de amostras a coletar
        nivel_confianca (float): Nível de confiança para intervalos. Defaults to 0.95.
        seed (Optional[int]): Semente para o gerador de números aleatórios. Defaults to None.
        
    Returns:
        Tuple[List[Tuple[float, float]], List[bool]]: Tupla contendo:
            - Lista de intervalos de confiança (limite inferior, limite superior)
            - Lista de indicadores se o intervalo contém a média populacional
    """
    if seed is not None:
        np.random.seed(seed)
    
    intervalos = []
    contem_media = []
    
    for _ in range(num_amostras):
        # Coletar uma amostra da população
        amostra = np.random.normal(media_populacional, desvio_populacional, tamanho_amostra)
        
        # Calcular intervalo de confiança para esta amostra
        ic_inf, ic_sup = calcular_intervalo_confianca(amostra, nivel_confianca)
        
        # Verificar se o intervalo contém a média populacional verdadeira
        contem = ic_inf <= media_populacional <= ic_sup
        
        intervalos.append((ic_inf, ic_sup))
        contem_media.append(contem)
    
    return intervalos, contem_media

def calcular_z_valor(nivel_confianca: float) -> float:
    """
    Calcula o valor Z para um determinado nível de confiança.
    
    Args:
        nivel_confianca (float): Nível de confiança (entre 0 e 1)
        
    Returns:
        float: Valor Z correspondente
        
    Raises:
        ValueError: Se o nível de confiança for inválido
    """
    if not 0 < nivel_confianca < 1:
        raise ValueError("Nível de confiança deve estar entre 0 e 1")
    
    return stats.norm.ppf((1 + nivel_confianca) / 2)

if __name__ == "__main__":
    # Demonstração de uso do módulo
    for i, notas in enumerate(NOTAS_PROFESSORES, 1):
        try:
            lim_inferior, lim_superior = calcular_intervalo_confianca(notas)
            logger.info(f"Professor {i}: IC = ({lim_inferior:.2f}, {lim_superior:.2f})")
            
            estatisticas = calcular_estatisticas_descritivas(notas)
            logger.info(f"Professor {i}: Estatísticas = {estatisticas}")
        except Exception as e:
            logger.error(f"Erro ao processar notas do Professor {i}: {str(e)}")
            
    # Demonstrar cálculos de probabilidade normal
    # Probabilidade de X < 0 em uma normal padrão
    prob = calcular_probabilidade_normal(0)
    logger.info(f"P(Z < 0) = {prob:.4f}")  # Deve ser 0.5
    
    # Probabilidade de estar dentro de 1 desvio padrão
    prob = calcular_probabilidade_entre(-1, 1)
    logger.info(f"P(-1 < Z < 1) = {prob:.4f}")  # Deve ser aproximadamente 0.6827
    
    # Probabilidade de estar dentro de 2 desvios padrão
    prob = calcular_probabilidade_entre(-2, 2)
    logger.info(f"P(-2 < Z < 2) = {prob:.4f}")  # Deve ser aproximadamente 0.9545