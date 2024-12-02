import numpy as np
import pandas as pd

def calculate_anova(data_groups):
    # Calculate total mean and observations
    all_data = [item for group in data_groups.values() for item in group]
    total_mean = np.mean(all_data)
    
    # Calculate sums of squares
    sqt = np.sum((all_data - total_mean)**2)
    
    sqd = sum(np.sum((group - np.mean(group))**2) 
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
    
    result = calculate_anova(data)
    print("Tabela ANOVA:")
    print(result)
