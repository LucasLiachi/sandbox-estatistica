# Validação de Funções Densidade de Probabilidade (PDF)

Este módulo implementa um sistema completo para validação de Funções Densidade de Probabilidade (PDF) usando Python e SymPy. O código é especialmente útil para análise estatística em controle de qualidade industrial.

## Funcionalidades Principais

### 1. Verificação de Positividade
```python
verificar_positividade(funcao, var, dominio)
```
- **Entrada**: Função simbólica, variável e domínio
- **Saída**: Boolean indicando se a função é não-negativa em todo domínio
- **Funcionamento**: 
  - Encontra pontos críticos através da derivada
  - Verifica valores nos extremos do domínio
  - Testa a função em pontos críticos

### 2. Verificação de Integral Unitária
```python
verificar_integral_unitaria(funcao, var, dominio)
```
- **Entrada**: Função simbólica, variável e domínio
- **Saída**: Boolean indicando se a integral é igual a 1
- **Funcionamento**:
  - Calcula integral simbólica no domínio
  - Verifica se o resultado é aproximadamente 1
  - Usa tolerância numérica para comparações

### 3. Cálculo de Probabilidade
```python
calcular_probabilidade(funcao, var, limite)
```
- **Entrada**: Função simbólica, variável e limites do intervalo
- **Saída**: Valor numérico da probabilidade
- **Funcionamento**:
  - Calcula integral definida no intervalo especificado
  - Retorna probabilidade P(a ≤ X ≤ b)

## Recursos Avançados

### Geração de Relatórios LaTeX
```python
gerar_relatorio_latex(funcao, var, dominio, resultados)
```
- Gera documentação matemática formatada
- Inclui expressões simbólicas e resultados
- Facilita integração com documentos técnicos

### Tratamento de Erros
- Validação de domínio e expressões
- Mensagens detalhadas de erro
- Sugestões de correção

## Exemplos de Uso

### 1. Distribuição Exponencial
```python
funcao_exp = "2 * exp(-2*x)"
resultados = validar_pdf(funcao_exp, 'x', (0, float('inf')))
```
- PDF válida
- Domínio: [0, ∞)
- P(X > 10) = e^(-20)

### 2. Distribuição Triangular
```python
funcao_tri = "Piecewise((2*x, x >= 0) & (x <= 1/2), (2*(1-x), x > 1/2) & (x <= 1), (0, True))"
resultados = validar_pdf(funcao_tri, 'x', (0, 1))
```
- Exemplo de função definida por partes
- Domínio finito [0, 1]
- Integral unitária verificada

## Requisitos Técnicos

### Dependências
- SymPy: Para computação simbólica
- NumPy: Para cálculos numéricos
- Python typing: Para anotações de tipo

### Tipos de Dados
- `sp.Expr`: Expressões simbólicas do SymPy
- `Union[float, str]`: Suporte para valores numéricos e simbólicos
- `Tuple`: Para representação de intervalos

## Tratamento de Erros

### Classe CustomException
```python
class PDFValidationError(Exception)
```
- Exceção personalizada para erros de validação
- Mensagens detalhadas para debugging
- Sugestões de correção quando aplicável

### Validações Principais
1. Positividade da função no domínio
2. Integral unitária (∫f(x)dx = 1)
3. Domínio bem definido
4. Expressões matemáticas válidas

## Considerações de Uso

### Performance
- Uso de computação simbólica para precisão
- Tolerância numérica configurável
- Otimização para domínios infinitos

### Boas Práticas
- Documentação detalhada das funções
- Tipos fortemente tipados
- Tratamento robusto de erros
- Testes incluídos no código

## Limitações e Considerações
- Algumas integrais complexas podem ser computacionalmente intensivas
- Funções descontínuas requerem atenção especial
- Domínios infinitos podem precisar de tratamento específico