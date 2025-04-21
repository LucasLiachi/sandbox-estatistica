# sandbox-estatistica

Bem-vindo ao repositório de estudos em estatística! Este projeto centraliza materiais, análises, códigos, bancos de dados e documentação para estudos e aplicações práticas em estatística, econometria e ciência de dados.

---

## 1. Objetivo do Projeto

Organizar e compartilhar materiais de estudo, implementações, tutoriais e projetos práticos em estatística, cobrindo desde conceitos fundamentais até aplicações avançadas, sempre respeitando as fontes dos dados e adaptando-os aos objetivos de cada análise.

---

## 2. Estrutura do Repositório

O repositório está organizado em:

### 2.1 Diretório Principal
- **README.md**: Este arquivo, com visão geral, instruções e sumário dos materiais.
- **requirements.txt**: Lista de dependências Python necessárias para executar os códigos do projeto.
- **.gitignore**: Configurações para ignorar arquivos e diretórios no controle de versão.
- **revisar.md**: Documentação com itens a serem revisados.

### 2.2 Diretório de Conceitos
- **conceitos/**  
  Dividido em três níveis de complexidade:
  - **basicos/**: Probabilidade, distribuições, métodos numéricos fundamentais, densidade de probabilidade, erro de arredondamento, regra do trapézio, etc.
  - **intermediarios/**: ANOVA, distribuição de Poisson, estimação de parâmetros, testes de hipótese, regressão linear, interpolação de Lagrange, integral, estudos de coorte, etc.
  - **avancados/**: Álgebra linear, álgebra matricial, econometria, inferência causal, regressão linear múltipla, iteração linear, etc.
  - Cada subpasta contém arquivos `.md` (teoria), `.py` (implementação), `.ipynb` (notebooks) e arquivos de teste.

#### 2.2.1 Conceitos Básicos de Estatística

Esta seção contém os conceitos fundamentais de estatística, incluindo:

- Classificação de Variáveis
- Probabilidade Básica
- Distribuição Binomial
- Densidade de Probabilidade

**Pré-requisitos**
- Matemática básica
- Noções de conjuntos

**Como usar**
Cada conceito possui sua própria documentação em formato markdown (.md) e implementação em Python (.py) quando aplicável.

**Estrutura**
- `classificacao-da-variavel.md`: Tipos de variáveis estatísticas
- `Probabilidade.md/.py`: Fundamentos de probabilidade
- `binomial.py`: Implementação da distribuição binomial
- `densidade-de-probabilidade.md/.py`: Conceitos de densidade de probabilidade

#### 2.2.2 Conceitos Intermediários de Estatística

Esta seção contém conceitos de nível intermediário, incluindo:

- Testes de Hipóteses (t-Student)
- Análise de Variância (ANOVA)
- Regressão Linear Simples
- Distribuição de Poisson
- Estimação de Parâmetros

**Pré-requisitos**
- Conceitos básicos de estatística
- Probabilidade
- Cálculo básico

**Como usar**
Cada conceito contém:
- Documentação teórica (.md)
- Implementação prática (.py)
- Exemplos de aplicação
- Visualizações quando aplicável

**Estrutura**
- `regressao_linear.md/.py`: Análise de regressão linear simples
- `teste_hipotese_tstudent.md/.py`: Testes de hipóteses usando distribuição t-Student
- `ANOVA.md/.py`: Análise de Variância
- `distribuicao-de-Poisson.md/.py`: Distribuição de Poisson e aplicações
- `estimacao-de-parametros.md`: Teoria de estimação de parâmetros

#### 2.2.3 Conceitos Avançados de Estatística

Esta seção abrange tópicos avançados de estatística e suas aplicações:

- Álgebra Linear e Matricial
- Regressão Linear Múltipla
- Econometria
- Inferência Causal

**Pré-requisitos**
- Conceitos intermediários de estatística
- Álgebra linear básica
- Cálculo multivariável
- Programação em Python

**Como usar**
Cada tópico inclui:
- Fundamentação teórica (.md)
- Implementações complexas (.py)
- Exemplos práticos
- Visualizações e diagramas

**Estrutura**
- `algebra_linear.md/.py`: Conceitos e aplicações de álgebra linear
- `algebra-matricial.md/.py`: Operações matriciais e suas aplicações
- `regressao-linear-multipla.md/.py`: Análise de regressão multivariada
- `Inferencia-causal.md`: Métodos de inferência causal
- Documentação sobre econometria e suas aplicações

### 2.3 Diretório de Projetos
- **projetos/**  
  Projetos práticos e estudos de caso, como:
  - Análise de aluguel
  - Análise de regressão em fábrica
  - Regressão linear BCB
  - Análise NBA
  - Análise de síndrome gripal no SUS
  - Simulação de filas
  - Outros projetos específicos

#### 2.3.1 Estudos de Caso

Esta seção contém estudos de caso práticos usando dados reais:

**Casos Disponíveis**

**Análises Esportivas (NBA)**
- Histogramas de times da NBA
- Análise de desempenho de jogadores
- Teste de homogeneidade para arremessos de 3 pontos

**Análises de Saúde**
- Síndrome gripal em dados do SUS
- Análise de filas hospitalares
- Simulações de atendimento

**Análises Governamentais**
- Média de gastos de deputados
- Análise de renda familiar
- Projetos de econometria aplicada

**Metodologia**
Cada estudo de caso deve conter:
- Contextualização do problema
- Metodologia estatística aplicada
- Código fonte comentado
- Visualizações
- Conclusões e recomendações práticas

**Estrutura dos Projetos**
1. Arquivo de documentação (.md)
2. Scripts de análise (.py)
3. Dados utilizados (quando públicos)
4. Visualizações geradas

#### 2.3.2 Análises Estatísticas

Esta seção contém análises estatísticas completas de diversos conjuntos de dados:

**Projetos Disponíveis**

**Análise de Aluguéis**
- Análise de preços e fatores que influenciam valores de aluguel
- Implementação de modelos de regressão
- Visualizações e conclusões

**Análise de Regressão em Ambiente Fabril**
- Estudo de umidade e variáveis de controle
- Análise de correlação entre fatores industriais

**Análise BCB - Regressão Linear**
- Análise de dados do Banco Central
- Modelagem econométrica
- Séries temporais financeiras

**Como Contribuir**
1. Use o template disponível em `projetos/templates`
2. Documente claramente metodologia e fontes de dados
3. Inclua visualizações relevantes
4. Forneça conclusões e interpretações práticas

---

## 3. Arquivos Especiais

### 3.1 Requirements.txt

O arquivo `requirements.txt` contém todas as dependências Python necessárias para executar os códigos e notebooks deste projeto:

```
numpy>=1.21.0     # Operações numéricas e álgebra matricial
scipy>=1.7.0      # Funções estatísticas e otimização
pandas>=1.3.0     # Manipulação e análise de dados
matplotlib>=3.4.0 # Visualização de dados
seaborn>=0.11.0   # Visualizações estatísticas avançadas
jupyter>=1.0.0    # Para executar os notebooks
pytest>=6.2.0     # Para executar os testes unitários
```

Para instalar todas as dependências, execute:
```bash
pip install -r requirements.txt
```

### 3.2 .gitignore

O arquivo `.gitignore` configura quais arquivos e diretórios devem ser ignorados pelo sistema de controle de versão Git. Isso inclui:

- Arquivos compilados Python (`__pycache__/`, `*.pyc`)
- Ambientes virtuais (`venv/`, `.env`)
- Arquivos de cache (`__pycache__/`, `.ipynb_checkpoints`)
- Arquivos de build e distribuição
- Arquivos temporários e logs
- Arquivos específicos de IDE/editores

Este arquivo é importante para manter o repositório limpo, incluindo apenas código fonte e documentação relevantes, sem arquivos temporários ou específicos do ambiente local.

---

## 4. Materiais e Conteúdo

O repositório cobre:

- Conceitos fundamentais de estatística, probabilidade e álgebra linear
- Métodos numéricos (bisseção, Newton, trapézio, interpolação)
- Distribuições estatísticas (binomial, Poisson, densidade de probabilidade)
- Testes de hipótese (t-Student, qui-quadrado, ANOVA)
- Regressão linear simples e múltipla
- Econometria e inferência causal
- Exercícios práticos e implementações em Python
- Tutoriais em Jupyter Notebook para aprendizado interativo
- Projetos aplicados com dados reais ou simulados

---

## 5. Como Utilizar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sandbox-estatistica.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Explore os diretórios:
   - `/conceitos/`: Material teórico, implementações e exercícios
   - `/projetos/`: Estudos de caso e aplicações práticas
4. Execute notebooks interativos:
   ```bash
   jupyter notebook
   ```
5. Execute testes para verificar implementações:
   ```bash
   pytest
   ```

---

## 6. Contribuições

Contribuições são bem-vindas! Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie um branch para sua feature (`git checkout -b feature/nova-analise`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova análise'`)
4. Push para o branch (`git push origin feature/nova-analise`)
5. Abra um Pull Request

Certifique-se de seguir as convenções de código e documentação existentes.

---

## 7. Licença

Este projeto está sob a licença MIT.

---

## 8. Referências e Notas Finais

- Referências bibliográficas e técnicas estão ao longo dos arquivos `.md`.
- Os dados utilizados são tratados e adaptados para fins educacionais.
- Para dúvidas ou sugestões, abra uma issue ou entre em contato.

---
