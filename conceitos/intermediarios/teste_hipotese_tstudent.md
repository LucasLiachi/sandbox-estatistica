# Guia de Implementação do Teste T de Student

## Visão Geral
O teste t de Student é usado para análise estatística de amostras independentes e comparações entre marcas.

## Fundamentos Estatísticos

### Hipótese Nula
- Base para comparação
- Controle de erros Tipo I
- Facilitação da interpretação

### Etapas do Teste
1. **Formulação da Hipótese**
   - H0: μ1 = μ2
   - H1: μ1 ≠ μ2

2. **Dados Necessários**
   - Tamanhos (n1, n2)
   - Médias (x̄1, x̄2)
   - Desvios padrão (s1, s2)
   - Nível de significância (α = 0.05)

## Implementação

### Funções Principais

1. **perform_ttest_samples(amostra_a, amostra_b, alfa=0.05)**
   - Realiza teste t entre duas amostras independentes
   - Calcula estatísticas básicas (médias, desvios padrão)
   - Retorna estatísticas, estatística t e valor-p
   - Nível de significância padrão: 0.05

2. **compare_brands(dados)**
   - Compara múltiplas marcas par a par
   - Utiliza médias e desvios padrão para comparação
   - Identifica diferenças estatisticamente significativas
   - Retorna pares de marcas com diferenças significativas

### Armazenamento de Dados

Resultados são armazenados em formato JSON:
- `ttest_results.json`: Armazena estatísticas e resultados do teste t
- `brand_comparison.json`: Armazena comparações significativas entre marcas

### Exemplo de Uso

#### 1. Teste T para Amostras Independentes

```python
# Importar bibliotecas necessárias
import numpy as np
from scipy import stats

# Criar amostras de exemplo
amostra_a = np.array([23, 25, 21, 24, 22])
amostra_b = np.array([19, 20, 18, 21, 20])

# Realizar teste t
resultado = perform_ttest_samples(amostra_a, amostra_b)
print(f"Estatística t: {resultado['t_stat']:.4f}")
print(f"Valor p: {resultado['p_value']:.4f}")
```

#### 2. Comparação entre Marcas

```python
# Dados de exemplo para marcas
dados_marcas = {
    'Marca_A': {'media': 24.5, 'desvio': 2.1, 'n': 30},
    'Marca_B': {'media': 22.3, 'desvio': 1.8, 'n': 30},
    'Marca_C': {'media': 23.7, 'desvio': 1.9, 'n': 30}
}

# Realizar comparações
resultados = compare_brands(dados_marcas)
print("Diferenças significativas encontradas:")
for comp in resultados:
    print(f"{comp['marca1']} vs {comp['marca2']}: p={comp['p_value']:.4f}")
```

### Interpretação dos Resultados

- **Valor-p < α**: Rejeita-se a hipótese nula
- **Valor-p ≥ α**: Não se rejeita a hipótese nula
- Considerar sempre o contexto prático dos resultados
