# Álgebra Linear Aplicada

## 1. Introdução à Álgebra Linear
A álgebra linear é fundamental em diversas áreas, especialmente em estatística e física. Este documento aborda duas aplicações principais:
- Regressão Linear via Álgebra Matricial
- Análise Vetorial em Física (Cálculo de Trabalho)

## 2. Regressão Linear via Álgebra Matricial

### 2.1 Fundamentos Teóricos
A regressão linear pode ser calculada utilizando álgebra matricial através da fórmula:

$$\hat{\beta} = (X'X)^{-1}X'Y$$

Onde:
- X: Matriz de design (com coluna de 1's para o intercepto)
- Y: Vetor de respostas
- β: Vetor de coeficientes (β0: intercepto, β1: coeficiente angular)

### 2.2 Avaliação do Modelo
O coeficiente de determinação (R²) é calculado por:
- R² = 1 - (SS_res / SS_tot)
- SS_res: soma dos quadrados dos resíduos
- SS_tot: soma total dos quadrados

## 3. Análise Vetorial - Exemplo Prático de Física

### 3.1 Cálculo do Trabalho
O trabalho realizado por uma força é definido pela equação:

$$W = F \cdot d$$

Onde:
- W: trabalho
- F: força
- d: deslocamento

### 3.2 Exemplo Prático: Sistema de Forças
Considere uma caixa de 50 kg sujeita a seis forças diferentes:
- F1 = 20N (horizontal direita)
- F2 = 20N (30° acima da horizontal direita)
- F3 = 30N (vertical para cima)
- F4 = 5N (30° acima da horizontal esquerda)
- F5 = 10N (horizontal esquerda)
- F6 = 15N (vertical para baixo)

![Sistema de Forças](algebra_linear.png)

### 3.3 Resolução Passo a Passo

1. **Decomposição das Forças F2 e F4**:
   - F2x = 20N × cos(30°) = 17,32N
   - F2y = 20N × sen(30°) = 10N
   - F4x = 5N × cos(30°) = 4,33N
   - F4y = 5N × sen(30°) = 2,5N

2. **Somatório das Forças**:
   - Eixo X = F1 + F2x - F4x - F5 = 23N
   - Eixo Y = F3 + F2y + F4y - F6 = 27,5N

3. **Força Resultante**:
   - Fr = √(23N)² + (27,5N)² = 35,85N

4. **Ângulo da Força Resultante**:
   - θ = arctan(27,5/23) = 48°

5. **Cálculo do Trabalho Final**:
   - W = Fr × d × cos(θ)
   - W = 35,85N × 10m × cos(48°)
   - W = 239,71 Joules

## 4. Conclusão
Este documento demonstra a versatilidade da álgebra linear em diferentes contextos:
- Na estatística, através da regressão linear matricial
- Na física, através da análise vetorial para cálculo de trabalho

A implementação computacional destes conceitos está disponível no arquivo `algebra_linear_unified.py`.