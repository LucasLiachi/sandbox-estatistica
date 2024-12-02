import numpy as np
from scipy import stats
import pandas as pd
import json
from pathlib import Path

def save_results(stats_data, t_stat, p_value, filename='teste_hipotese_tstudent.json'):
    results = {
        'statistics': stats_data,
        't_statistic': float(t_stat),
        'p_value': float(p_value)
    }
    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)

def load_results(filename='teste_hipotese_tstudent.json'):
    if not Path(filename).exists():
        return None
    with open(filename, 'r') as f:
        return json.load(f)

def perform_ttest_samples(sample_a, sample_b, alpha=0.05):
    stats_data = {
        'mean_a': np.mean(sample_a),
        'mean_b': np.mean(sample_b),
        'std_a': np.std(sample_a, ddof=1),
        'std_b': np.std(sample_b, ddof=1)
    }
    t_stat, p_value = stats.ttest_ind(sample_a, sample_b)
    save_results(stats_data, t_stat, p_value)
    return stats_data, t_stat, p_value

def compare_brands(data):
    brands = data['Marca'].unique()
    significant_pairs = []
    
    for i, brand1 in enumerate(brands):
        for brand2 in brands[i+1:]:
            stats1 = data[data['Marca'] == brand1]
            stats2 = data[data['Marca'] == brand2]
            
            t_stat = (stats1['Média de Venda'].iloc[0] - stats2['Média de Venda'].iloc[0]) / \
                     np.sqrt((stats1['Desvio Padrão das Vendas'].iloc[0]**2/4) + \
                            (stats2['Desvio Padrão das Vendas'].iloc[0]**2/4))
            
            p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=6))
            
            if p_value <= 0.05:
                significant_pairs.append((brand1, brand2))
    
    results = {'significant_pairs': significant_pairs}
    save_results(results, 0, 0, 'brand_comparison.json')
    return significant_pairs

def main():
    sample_a = np.array([14, 16, 15, 17, 16, 18, 15, 17, 16, 15])
    sample_b = np.array([18, 20, 19, 21, 20, 22, 19, 21, 20, 19])
    
    stats_data, t_stat, p_value = perform_ttest_samples(sample_a, sample_b)
    print(f"T-test results: t={t_stat:.2f}, p={p_value:.4f}")
    
    # Save and recover results example
    previous_results = load_results()
    if previous_results:
        print("Previous results found:")
        print(json.dumps(previous_results, indent=2))

if __name__ == "__main__":
    main()

