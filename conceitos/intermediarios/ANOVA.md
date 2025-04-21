
# Análise de Variância (ANOVA)

## Descrição
A Análise de Variância (ANOVA) é um teste estatístico que compara as médias de diferentes grupos para determinar se há diferenças significativas entre eles.

## Estrutura do Código

### Componentes Principais
1. **Entrada de Dados**
   - Três grupos: fundamental, médio e superior
   - Dados armazenados em um dicionário para fácil acesso

2. **Cálculos Principais**
   - Soma de Quadrados Total (SQT)
   - Soma de Quadrados Entre grupos (SQE)
   - Soma de Quadrados Dentro dos grupos (SQD)
   - Quadrados Médios (QM)
   - Valor F

### Fórmulas Utilizadas
- SQT = Σ(x - média_total)²
- SQE = Σ(ni * (média_grupo - média_total)²)
- SQD = Σ(x - média_grupo)²
- QME = SQE / gl_entre
- QMD = SQD / gl_dentro
- F = QME / QMD

## Interpretação
- O valor F indica se há diferenças significativas entre os grupos
- Quanto maior o valor F, maior a evidência de diferença entre os grupos