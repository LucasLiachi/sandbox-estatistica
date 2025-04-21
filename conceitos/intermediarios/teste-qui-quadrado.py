import numpy as np
from scipy import stats
from typing import List, Dict, Union
import sys

def validate_input(observed: List[float], min_sample_size: int = 30, min_category_size: int = 5) -> bool:
    """
    Valida os dados de entrada do teste qui-quadrado.
    
    Args:
        observed: Lista de frequências observadas
        min_sample_size: Tamanho mínimo total da amostra
        min_category_size: Tamanho mínimo por categoria
        
    Returns:
        bool: True se os dados são válidos, False caso contrário
    """
    if any(freq < 0 for freq in observed):
        print("Erro: Todas as frequências devem ser não-negativas")
        return False
        
    total_sample = sum(observed)
    if total_sample < min_sample_size:
        print(f"Erro: Tamanho total da amostra ({total_sample}) é menor que o mínimo requerido ({min_sample_size})")
        return False
        
    expected = total_sample / len(observed)
    if expected < min_category_size:
        print(f"Erro: Frequência esperada por categoria ({expected:.2f}) é menor que o mínimo requerido ({min_category_size})")
        return False
        
    return True

def chi_square_test(observed: List[float], alpha: float = 0.05) -> Dict[str, Union[float, str]]:
    """
    Realiza o teste qui-quadrado para aderência à distribuição uniforme.
    
    Args:
        observed: Lista de frequências observadas
        alpha: Nível de significância (padrão 0.05)
    
    Returns:
        Dict contendo os resultados do teste:
            - Estatística X² calculada
            - Valor crítico
            - Valor-p
            - Graus de liberdade
            - Decisão (Rejeitar ou Aceitar H₀)
    """
    observed = np.array(observed)
    n_categories = len(observed)
    expected = np.full(n_categories, sum(observed)/n_categories)
    
    chi2_stat, p_value = stats.chisquare(f_obs=observed, f_exp=expected)
    df = n_categories - 1
    critical_value = stats.chi2.ppf(1 - alpha, df)
    
    results = {
        'Estatística X²': chi2_stat,
        'Valor crítico': critical_value,
        'Valor-p': p_value,
        'Graus de liberdade': df,
        'Decisão': 'Rejeitar H₀' if p_value < alpha else 'Aceitar H₀'
    }
    
    return results

def print_results(results: Dict[str, Union[float, str]]) -> None:
    """
    Imprime os resultados do teste de forma formatada.
    
    Args:
        results: Dicionário com os resultados do teste
    """
    print("\nResultados do Teste Qui-Quadrado para Aderência:")
    print("-" * 50)
    for key, value in results.items():
        if isinstance(value, float):
            print(f"{key}: {value:.4f}")
        else:
            print(f"{key}: {value}")
    print("-" * 50)

def main():
    """Interface principal do programa."""
    print("Teste de Qui-Quadrado para Aderência à Distribuição Uniforme")
    print("=" * 60)
    print("\nInsira as frequências observadas separadas por vírgula (ex: 25,15,20,10)")
    
    try:
        observed = list(map(float, input("Frequências observadas: ").split(',')))
        alpha = float(input("Nível de significância (padrão 0.05): ") or 0.05)
        
        if not validate_input(observed):
            sys.exit(1)
            
        results = chi_square_test(observed, alpha)
        print_results(results)
        
    except ValueError as e:
        print(f"Erro: Entrada inválida. Certifique-se de inserir apenas números separados por vírgula.")
        sys.exit(1)

if __name__ == "__main__":
    main()