"""
Análise de Regressão Linear Simples para Estudo de Umidade
Objetivo: Avaliar a relação entre a umidade do local de produção e a umidade do material,
utilizando um modelo de regressão linear simples com nível de significância α = 5%.

Hipóteses:
H0: β1 = 0 (não há relação linear entre as variáveis)
H1: β1 ≠ 0 (existe relação linear entre as variáveis)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.stattools import durbin_watson
from statsmodels.graphics.gofplots import ProbPlot

def load_data():
    """
    Carrega os dados de umidade do local e do material.
    
    Variáveis:
    - umidade_local (X): variável independente/explicativa
    - umidade_material (Y): variável dependente/resposta
    
    Dados coletados: 10 observações pareadas
    """
    umidade_local = np.array([46, 53, 37, 42, 34, 29, 60, 44, 41, 48])
    umidade_material = np.array([12, 14, 11, 13, 10, 8, 17, 12, 10, 15])
    
    # Criar DataFrame para facilitar a análise
    df = pd.DataFrame({
        'umidade_local': umidade_local,
        'umidade_material': umidade_material
    })
    
    return df

def exploratory_analysis(df):
    """
    Realiza análise exploratória dos dados para verificar:
    1. Estatísticas descritivas básicas
    2. Correlação linear entre as variáveis (coeficiente de Pearson)
    3. Visualização da relação através de gráfico de dispersão
    
    A análise exploratória é crucial para identificar padrões,
    potenciais outliers e a natureza da relação entre as variáveis.
    """
    # Estatísticas descritivas
    print("Estatísticas descritivas:")
    print(df.describe())
    
    # Coeficiente de correlação de Pearson
    correlation = df['umidade_local'].corr(df['umidade_material'])
    print(f"\nCoeficiente de correlação de Pearson: {correlation:.4f}")
    
    # Visualização dos dados
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='umidade_local', y='umidade_material', data=df)
    plt.title('Relação entre Umidade do Local e Umidade do Material')
    plt.xlabel('Umidade do Local (%)')
    plt.ylabel('Umidade do Material (%)')
    plt.grid(True, alpha=0.3)
    plt.savefig('scatter_plot.png')
    plt.close()
    
    return correlation

def fit_regression_model(df):
    """
    Ajusta o modelo de regressão linear simples Y = β0 + β1X + ε
    
    Onde:
    - Y: Umidade do material (variável resposta)
    - X: Umidade do local (variável explicativa)
    - β0: Intercepto
    - β1: Coeficiente angular
    - ε: Erro aleatório
    
    Utilizando o método dos Mínimos Quadrados Ordinários (MQO)
    com nível de significância α = 5%
    """
    # Preparar variáveis
    X = df['umidade_local']
    y = df['umidade_material']
    
    # Adicionar constante para o intercepto
    X_with_const = sm.add_constant(X)
    
    # Ajustar o modelo
    model = sm.OLS(y, X_with_const).fit()
    
    # Imprimir resumo do modelo
    print("\nResumo do modelo de regressão:")
    print(model.summary())
    
    return model

def test_model_assumptions(model, df):
    """
    Verifica os pressupostos do modelo de regressão linear:
    
    1. Normalidade dos resíduos (Teste Shapiro-Wilk)
       H0: resíduos seguem distribuição normal
       H1: resíduos não seguem distribuição normal
    
    2. Homocedasticidade (Teste Breusch-Pagan)
       H0: variância dos resíduos é constante
       H1: variância dos resíduos não é constante
    
    3. Independência dos resíduos (Teste Durbin-Watson)
       Valores próximos a 2 indicam independência
       
    4. Linearidade (análise gráfica dos resíduos)

    Todos os testes são realizados com α = 5%
    """
    # Obter resíduos
    residuals = model.resid
    fitted_values = model.fittedvalues
    
    # Teste de normalidade dos resíduos (Shapiro-Wilk)
    shapiro_test = stats.shapiro(residuals)
    print(f"\nTeste de Shapiro-Wilk para normalidade dos resíduos:")
    print(f"Estatística W: {shapiro_test[0]:.4f}, Valor-p: {shapiro_test[1]:.4f}")
    
    # Teste de homocedasticidade (Breusch-Pagan)
    bp_test = het_breuschpagan(residuals, model.model.exog)
    print(f"\nTeste de Breusch-Pagan para homocedasticidade:")
    print(f"Estatística LM: {bp_test[0]:.4f}, Valor-p: {bp_test[1]:.4f}")
    
    # Teste de independência dos resíduos (Durbin-Watson)
    dw_stat = durbin_watson(residuals)
    print(f"\nEstatística de Durbin-Watson: {dw_stat:.4f}")
    
    # Gráficos de diagnóstico
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Resíduos vs. Valores ajustados
    axes[0, 0].scatter(fitted_values, residuals)
    axes[0, 0].axhline(y=0, color='r', linestyle='-')
    axes[0, 0].set_xlabel('Valores Ajustados')
    axes[0, 0].set_ylabel('Resíduos')
    axes[0, 0].set_title('Resíduos vs. Valores Ajustados')
    
    # Histograma dos resíduos
    axes[0, 1].hist(residuals, bins=5, edgecolor='black')
    axes[0, 1].set_xlabel('Resíduos')
    axes[0, 1].set_ylabel('Frequência')
    axes[0, 1].set_title('Histograma dos Resíduos')
    
    # Q-Q plot
    QQ = ProbPlot(residuals)
    QQ.qqplot(line='45', ax=axes[1, 0])
    axes[1, 0].set_title('Q-Q Plot dos Resíduos')
    
    # Resíduos vs. Variável independente
    axes[1, 1].scatter(df['umidade_local'], residuals)
    axes[1, 1].axhline(y=0, color='r', linestyle='-')
    axes[1, 1].set_xlabel('Umidade do Local')
    axes[1, 1].set_ylabel('Resíduos')
    axes[1, 1].set_title('Resíduos vs. Umidade do Local')
    
    plt.tight_layout()
    plt.savefig('diagnostic_plots.png')
    plt.close()

def interpret_results(model, correlation):
    """
    Interpreta os resultados do modelo de regressão considerando α = 5%:
    
    1. Equação ajustada do modelo
    2. Coeficiente de determinação (R²)
    3. Teste F para significância global do modelo
       H0: β1 = 0 (modelo não é significativo)
       H1: β1 ≠ 0 (modelo é significativo)
    4. Interpretação dos coeficientes
    5. Análise da força da correlação
    
    Critérios de decisão:
    - Rejeita-se H0 se valor-p < 0.05
    - R² > 0.6 indica bom ajuste do modelo
    """
    # Extrair coeficientes
    intercept = model.params[0]
    slope = model.params[1]
    
    # Extrair estatísticas do modelo
    r_squared = model.rsquared
    r_squared_adj = model.rsquared_adj
    f_stat = model.fvalue
    f_pvalue = model.f_pvalue
    
    # Criar interpretação
    print("\n" + "="*50)
    print("INTERPRETAÇÃO DOS RESULTADOS")
    print("="*50)
    
    print(f"\nEquação do modelo ajustado:")
    print(f"Umidade no Material = {intercept:.4f} + {slope:.4f} × Umidade no Local")
    
    print(f"\nCoeficiente de determinação (R²): {r_squared:.4f}")
    print(f"Isso indica que {r_squared*100:.2f}% da variabilidade na umidade do material")
    print(f"pode ser explicada pela umidade no local de produção.")
    
    print(f"\nSignificância global do modelo (Teste F):")
    print(f"Estatística F: {f_stat:.4f}, Valor-p: {f_pvalue:.8f}")
    
    if f_pvalue < 0.05:
        print("Como o valor-p é menor que 0.05, o modelo é estatisticamente significativo.")
    else:
        print("Como o valor-p é maior que 0.05, o modelo não é estatisticamente significativo.")
    
    print(f"\nInterpretação do coeficiente angular:")
    print(f"Para cada aumento de 1 unidade percentual na umidade do local de produção,")
    print(f"espera-se um aumento médio de {slope:.4f} unidades percentuais na umidade do material.")
    
    print(f"\nForça da relação:")
    print(f"O coeficiente de correlação de Pearson é {correlation:.4f}, indicando uma")
    
    if abs(correlation) > 0.7:
        print("forte correlação entre as variáveis.")
    elif abs(correlation) > 0.3:
        print("correlação moderada entre as variáveis.")
    else:
        print("correlação fraca entre as variáveis.")
    
    # Conclusão sobre a permanência dos indicadores
    print("\nCONCLUSÃO:")
    if r_squared > 0.6 and f_pvalue < 0.05:
        print("Recomenda-se manter ambos os indicadores na cartela de medidas de controle,")
        print("pois demonstram uma relação consistente e estatisticamente significativa.")
    else:
        print("A relação entre os indicadores não é suficientemente forte ou significativa.")
        print("Recomenda-se revisão dos indicadores ou coleta de mais dados.")

def plot_regression_line(df, model):
    """
    Visualiza o modelo ajustado:
    1. Dados observados
    2. Linha de regressão estimada
    3. Equação do modelo com R²
    
    Esta visualização permite avaliar graficamente a qualidade
    do ajuste e identificar possíveis pontos influentes.
    """
    # Criar valores para a linha de regressão
    x_range = np.linspace(df['umidade_local'].min() - 5, df['umidade_local'].max() + 5, 100)
    X_pred = sm.add_constant(x_range)
    y_pred = model.predict(X_pred)
    
    # Plotar dados e linha de regressão
    plt.figure(figsize=(10, 6))
    plt.scatter(df['umidade_local'], df['umidade_material'], color='blue', label='Dados observados')
    plt.plot(x_range, y_pred, color='red', label='Linha de regressão')
    
    # Adicionar equação da reta ao gráfico
    intercept = model.params[0]
    slope = model.params[1]
    r_squared = model.rsquared
    equation = f'y = {intercept:.4f} + {slope:.4f}x\nR² = {r_squared:.4f}'
    plt.annotate(equation, xy=(0.05, 0.9), xycoords='axes fraction', 
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
    
    plt.title('Modelo de Regressão Linear: Umidade do Local vs. Umidade do Material')
    plt.xlabel('Umidade do Local (%)')
    plt.ylabel('Umidade do Material (%)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.savefig('regression_line.png')
    plt.close()

def main():
    """
    Executa a análise completa de regressão linear seguindo
    o processo estatístico com α = 5%:
    
    1. Carregamento e exploração dos dados
    2. Ajuste do modelo
    3. Verificação dos pressupostos
    4. Interpretação dos resultados
    5. Visualização do modelo ajustado
    """
    print("ANÁLISE DE REGRESSÃO LINEAR: ESTUDO DE UMIDADE")
    print("="*50)
    
    # Carregar dados
    df = load_data()
    print("Dados carregados com sucesso!\n")
    
    # Análise exploratória
    correlation = exploratory_analysis(df)
    
    # Ajustar modelo de regressão
    model = fit_regression_model(df)
    
    # Testar pressupostos do modelo
    test_model_assumptions(model, df)
    
    # Plotar linha de regressão
    plot_regression_line(df, model)
    
    # Interpretar resultados
    interpret_results(model, correlation)
    
    print("\nAnálise concluída! Os gráficos foram salvos nos arquivos:")
    print("- scatter_plot.png")
    print("- diagnostic_plots.png")
    print("- regression_line.png")

if __name__ == "__main__":
    main()
