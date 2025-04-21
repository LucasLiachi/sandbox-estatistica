# Sistema de Análise Estatística Integrada

Este projeto implementa um sistema de análise estatística com interface de linha de comando (CLI) que integra três importantes ferramentas estatísticas:
1. Teste Qui-quadrado
2. Simulação de Cadeias de Markov
3. Análise de Teoria das Filas (M/M/1 e M/M/c)

## Contextualização do Problema

Em análises estatísticas, frequentemente precisamos:
- Verificar se distribuições observadas se ajustam a distribuições esperadas (Teste Qui-quadrado)
- Simular processos que evoluem no tempo com probabilidades de transição (Cadeias de Markov)
- Analisar sistemas de filas para otimizar recursos e tempos de espera (Teoria das Filas)

Este sistema unifica estas três ferramentas em uma única interface, facilitando análises estatísticas complexas.

## Funcionalidades Implementadas

### 1. Teste Qui-quadrado
- **Entrada**: Frequências observadas e (opcionalmente) frequências esperadas
- **Saída**: 
  - Estatística qui-quadrado
  - Valor-p
  - Valor crítico (α=0.05)
  - Graus de liberdade
  - Decisão sobre a hipótese nula

### 2. Simulação de Cadeias de Markov
- **Entrada**: 
  - Matriz de transição
  - Número de estados
  - Número de passos para simulação
- **Saída**:
  - Probabilidades finais dos estados
  - Visualização gráfica da evolução dos estados (opcional)

### 3. Análise de Filas (M/M/1 e M/M/c)
- **Entrada**:
  - Taxa de chegada (λ)
  - Taxa de serviço (μ)
  - Número de servidores (c)
- **Saída**:
  - Utilização do sistema (ρ)
  - Número médio de clientes no sistema (L)
  - Número médio de clientes na fila (Lq)
  - Tempo médio no sistema (W)
  - Tempo médio de espera na fila (Wq)

## Validações e Tratamento de Erros

O sistema inclui validações robustas para:
1. Entrada de dados numéricos
2. Matrizes de transição (soma das linhas = 1)
3. Estabilidade do sistema de filas (ρ < 1)
4. Dimensões e tipos de dados compatíveis

## Como Usar

### Requisitos
```
numpy
scipy
matplotlib (opcional, para visualizações)
```

### Execução
```bash
python projeto-integrado.py
```

### Exemplos de Uso

1. **Teste Qui-quadrado**
```
Observado: [16, 18, 16, 14, 12, 12]
Esperado: [15, 15, 15, 15, 15, 15]
```

2. **Cadeia de Markov**
```
Matriz 2x2:
0.7 0.3
0.4 0.6
```

3. **Análise de Fila**
```
λ = 2 (taxa de chegada)
μ = 3 (taxa de serviço)
c = 1 (servidor único)
```

## Benefícios e Aplicações

1. **Teste Qui-quadrado**
   - Análise de adequação de ajuste
   - Testes de independência
   - Validação de distribuições

2. **Cadeias de Markov**
   - Previsão de comportamento de sistemas
   - Análise de processos estocásticos
   - Modelagem de transições de estado

3. **Teoria das Filas**
   - Dimensionamento de recursos
   - Otimização de atendimento
   - Análise de gargalos

## Limitações e Considerações

- O sistema assume distribuições específicas para cada análise
- A visualização da cadeia de Markov requer matplotlib
- Para sistemas M/M/c com c > 1, algumas aproximações são utilizadas
- O desempenho é otimizado para matrizes de até 100x100

## Testes e Validação

O sistema inclui uma suite de testes integrada (opção 4 no menu) que verifica:
- Funcionamento do teste qui-quadrado
- Simulação de cadeia de Markov simples
- Cálculos de métricas de fila

## Futuras Melhorias

1. Adição de mais testes estatísticos
2. Suporte a outros modelos de fila
3. Visualizações mais detalhadas
4. Exportação de resultados
5. Interface gráfica