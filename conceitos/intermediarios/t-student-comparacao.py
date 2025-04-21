import argparse
import numpy as np
from scipy import stats

def calculate_t_test(mean1, std1, n1, mean2, std2, n2, alpha=0.05):
    """
    Executa teste t para duas amostras independentes com verificação de variâncias
    
    Parâmetros:
        mean1, mean2: médias dos grupos
        std1, std2: desvios padrão dos grupos
        n1, n2: tamanhos das amostras
        alpha: nível de significância (padrão 0.05)
    
    Retorna:
        Dicionário com resultados do teste e decisão
    """
    # Validação dos dados de entrada
    if n1 < 5 or n2 < 5:
        raise ValueError("Tamanho mínimo das amostras deve ser 5")
    if std1 <= 0 or std2 <= 0:
        raise ValueError("Desvios padrão devem ser positivos")
    if not 0 < alpha < 1:
        raise ValueError("Nível de significância deve estar entre 0 e 1")
    
    # Verificação de variâncias usando teste de Levene
    _, p_levene = stats.levene(
        np.random.normal(loc=mean1, scale=std1, size=n1),
        np.random.normal(loc=mean2, scale=std2, size=n2)
    )
    
    # Seleção do teste baseado na homogeneidade das variâncias
    equal_var = p_levene > alpha
    
    # Cálculo do teste t
    t_stat, p_value = stats.ttest_ind_from_stats(
        mean1, std1, n1,
        mean2, std2, n2,
        equal_var=equal_var
    )
    
    # Cálculo dos graus de liberdade
    if equal_var:
        # Fórmula para variâncias iguais (Student)
        df = n1 + n2 - 2
    else:
        # Fórmula para variâncias diferentes (Welch)
        df = (std1**2/n1 + std2**2/n2)**2 / ((std1**2/n1)**2/(n1-1) + (std2**2/n2)**2/(n2-1))
    
    # Valor crítico bilateral
    critical_value = stats.t.ppf(1 - alpha/2, df)
    
    return {
        't_statistic': t_stat,
        'p_value': p_value,
        'degrees_of_freedom': df,
        'critical_value': critical_value,
        'equal_variances': equal_var,
        'decision': 'Rejeitar H₀' if abs(t_stat) > critical_value else 'Aceitar H₀'
    }

def format_results(results):
    """Formata os resultados do teste para exibição"""
    print("\nResultados do Teste t:")
    print("-" * 50)
    print(f"Estatística t: {results['t_statistic']:.4f}")
    print(f"Valor-p: {results['p_value']:.4f}")
    print(f"Graus de liberdade: {results['degrees_of_freedom']:.2f}")
    print(f"Valor crítico (bilateral): {results['critical_value']:.4f}")
    print(f"Variâncias iguais: {'Sim' if results['equal_variances'] else 'Não'}")
    print(f"Decisão: {results['decision']}")
    print("-" * 50)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Teste t para duas amostras independentes')
    parser.add_argument('--mean1', type=float, required=True, help='Média do grupo 1')
    parser.add_argument('--std1', type=float, required=True, help='Desvio padrão do grupo 1')
    parser.add_argument('--n1', type=int, required=True, help='Tamanho da amostra do grupo 1')
    parser.add_argument('--mean2', type=float, required=True, help='Média do grupo 2')
    parser.add_argument('--std2', type=float, required=True, help='Desvio padrão do grupo 2')
    parser.add_argument('--n2', type=int, required=True, help='Tamanho da amostra do grupo 2')
    parser.add_argument('--alpha', type=float, default=0.05, help='Nível de significância (padrão: 0.05)')
    
    args = parser.parse_args()
    
    try:
        results = calculate_t_test(
            args.mean1, args.std1, args.n1,
            args.mean2, args.std2, args.n2,
            args.alpha
        )
        format_results(results)
    except ValueError as e:
        print(f"\nErro: {e}")
        exit(1)