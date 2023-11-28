import numpy as np

# declaração das variáveis
valor_exato = 346.635
digitos_significativos = 4

# calcula o expoente necessário para manter o número de dígitos significativos
expoente = np.floor(np.log10(np.abs(valor_exato))) + 1 - digitos_significativos

# arredonda o valor exato para o número de dígitos significativos
valor_arredondado = np.around(valor_exato / (10 ** expoente)) * (10 ** expoente)

# calcula a diferença entre o valor exato e o valor arredondado
diferenca = valor_exato - valor_arredondado

# calcula o erro de arredondamento percentual
erro_percentual = np.abs(diferenca / valor_exato) * 100

# exibe o resultado na tela
print(f"O erro de arredondamento percentual é de {erro_percentual:.6f}%.")
