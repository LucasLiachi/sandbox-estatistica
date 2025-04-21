import numpy as np
import matplotlib.pyplot as plt

def arredondar_digitos_significativos(valor, digitos_significativos):
    """
    Arredonda um número para um determinado número de dígitos significativos.
    
    Args:
        valor: O número a ser arredondado
        digitos_significativos: Número de dígitos significativos a manter
        
    Returns:
        O valor arredondado
    """
    if valor == 0:
        return 0
    
    # Calcula o expoente necessário para manter o número de dígitos significativos
    expoente = np.floor(np.log10(np.abs(valor))) + 1 - digitos_significativos
    
    # Arredonda o valor exato para o número de dígitos significativos
    return np.around(valor / (10 ** expoente)) * (10 ** expoente)

def calcular_erro_arredondamento(valor_exato, valor_arredondado):
    """
    Calcula diferentes métricas de erro de arredondamento.
    
    Args:
        valor_exato: O valor original
        valor_arredondado: O valor após arredondamento
        
    Returns:
        Um dicionário com os diferentes tipos de erro
    """
    if valor_exato == 0:
        return {
            "erro_absoluto": np.abs(valor_arredondado),
            "erro_relativo": float('inf') if valor_arredondado != 0 else 0,
            "erro_percentual": float('inf') if valor_arredondado != 0 else 0
        }
    
    erro_absoluto = np.abs(valor_exato - valor_arredondado)
    erro_relativo = erro_absoluto / np.abs(valor_exato)
    erro_percentual = erro_relativo * 100
    
    return {
        "erro_absoluto": erro_absoluto,
        "erro_relativo": erro_relativo,
        "erro_percentual": erro_percentual
    }

def visualizar_erro_arredondamento(valor, digitos_range, salvar_grafico=False, nome_arquivo=None):
    """
    Visualiza como o erro de arredondamento varia com o número de dígitos significativos.
    
    Args:
        valor: O valor original a ser arredondado
        digitos_range: Range de dígitos significativos a testar
        salvar_grafico: Se True, salva o gráfico em um arquivo
        nome_arquivo: Nome do arquivo para salvar o gráfico (se salvar_grafico=True)
    """
    erros_percentuais = []
    valores_arredondados = []
    
    for digitos in digitos_range:
        valor_arredondado = arredondar_digitos_significativos(valor, digitos)
        erro = calcular_erro_arredondamento(valor, valor_arredondado)
        erros_percentuais.append(erro['erro_percentual'])
        valores_arredondados.append(valor_arredondado)
    
    # Plotar o gráfico de erro
    plt.figure(figsize=(10, 6))
    plt.plot(digitos_range, erros_percentuais, marker='o', linestyle='-', color='blue')
    plt.xlabel('Número de Dígitos Significativos')
    plt.ylabel('Erro Percentual (%)')
    plt.title(f'Erro de Arredondamento para o Valor {valor}')
    plt.grid(True)
    plt.yscale('log')  # Escala logarítmica para melhor visualização
    
    if salvar_grafico and nome_arquivo:
        plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
    
    plt.show()
    
    # Tabela de valores
    print("Tabela de Valores:")
    print("-" * 60)
    print(f"{'Dígitos':^10} | {'Valor Arredondado':^20} | {'Erro Percentual (%)':^15}")
    print("-" * 60)
    
    for i, digitos in enumerate(digitos_range):
        print(f"{digitos:^10} | {valores_arredondados[i]:^20} | {erros_percentuais[i]:^15.6f}")
    
    return valores_arredondados, erros_percentuais

def demonstrar_propagacao_erro(valor_inicial, numero_iteracoes, precisoes, operacao=None):
    """
    Demonstra como o erro de arredondamento se propaga em um cálculo iterativo.
    
    Args:
        valor_inicial: Valor inicial para o cálculo
        numero_iteracoes: Número de iterações a realizar
        precisoes: Lista de precisões (dígitos significativos) a testar
        operacao: Função que realiza a operação matemática em cada iteração. 
                  Se None, usa a operação padrão (x^2/10)
    """
    if operacao is None:
        operacao = lambda x: (x ** 2) / 10
    
    resultados = {}
    for precisao in precisoes:
        valor = valor_inicial
        valores = [valor]
        
        for _ in range(numero_iteracoes):
            # Cálculo exato
            valor_exato = operacao(valor)
            
            # Cálculo com arredondamento
            valor = arredondar_digitos_significativos(valor_exato, precisao)
            valores.append(valor)
        
        resultados[precisao] = valores
    
    # Visualizar os resultados
    plt.figure(figsize=(12, 6))
    
    for precisao, valores in resultados.items():
        plt.plot(range(len(valores)), valores, marker='o', label=f'{precisao} dígitos')
    
    plt.xlabel('Iteração')
    plt.ylabel('Valor')
    plt.title('Propagação do Erro de Arredondamento em Cálculos Iterativos')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return resultados

# Exemplos de uso

if __name__ == "__main__":
    # Exemplo 1: Arredondar 124678 para 4 dígitos significativos
    valor1 = 124678
    valor1_arredondado = arredondar_digitos_significativos(valor1, 4)
    print(f"Exemplo 1: {valor1} arredondado para 4 dígitos significativos = {valor1_arredondado}")
    
    # Calcular o erro de arredondamento para o exemplo 1
    erro1 = calcular_erro_arredondamento(valor1, valor1_arredondado)
    print(f"Erro absoluto: {erro1['erro_absoluto']}")
    print(f"Erro relativo: {erro1['erro_relativo']:.6f}")
    print(f"Erro percentual: {erro1['erro_percentual']:.6f}%")
    
    # Exemplo 2: Arredondar 346.635 para 4 dígitos significativos
    valor2 = 346.635
    digitos_significativos = 4
    valor2_arredondado = arredondar_digitos_significativos(valor2, digitos_significativos)
    
    # Calcular o erro de arredondamento para o exemplo 2
    erro2 = calcular_erro_arredondamento(valor2, valor2_arredondado)
    print(f"\nErro absoluto: {erro2['erro_absoluto']}")
    print(f"Erro relativo: {erro2['erro_relativo']:.6f}")
    print(f"Erro percentual: {erro2['erro_percentual']:.6f}%")
