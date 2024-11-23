# **Exercício Analítico de Média: Dados dos Jogadores da NBA**

## **1. Fase de Planejamento da Pesquisa**

### **Definição de Objetivos**

O objetivo principal deste projeto é analisar o desempenho dos jogadores ativos da NBA com base em suas estatísticas de carreira. A análise busca identificar padrões, tendências e insights que possam ser úteis para equipes, treinadores e analistas esportivos. Para este modelo se busca analisar:

- Como a eficiência nos arremessos de 3 pontos varia entre diferentes faixas etárias?

### **Planejamento do Estudo**

- **Tipo de estudo**: Estudo descritivo e exploratório, utilizando dados históricos das estatísticas dos jogadores.
- **Fontes de dados**: API oficial da NBA (`nba_api`), que fornece informações detalhadas sobre os jogadores.
- **Ferramentas utilizadas**: Python (bibliotecas como `pandas`, `numpy`, `matplotlib`) e SQLite para armazenamento.

### **Determinação das Variáveis**

As variáveis principais a serem analisadas incluem:

- **Dados demográficos**: Idade, altura, peso, posição.
- **Arremessos de 3 pontos**: Arremessos de 3 pontos convertidos (FG3M), arremessos de 3 pontos tentados (FG3A), porcentagem de acertos de 3 pontos (FG3_PCT).

### **Determinação do Tamanho da Amostra**

A amostra será composta por todos os jogadores ativos na NBA disponíveis na API no momento da coleta. Dependendo da análise, os dados podem ser filtrados por posição, idade ou outras características.

## **2. Fase de Coleta de Dados**

### **Descrição**

Os dados serão coletados diretamente da API oficial da NBA usando a biblioteca `nba_api`. O processo inclui:

1. Obter a lista completa de jogadores ativos.
2. Coletar estatísticas detalhadas de carreira para cada jogador.
3. Armazenar os dados em um banco SQLite para facilitar consultas e análises futuras.

#### Código para Coleta e Armazenamento:

>[Arquivo .py com o código de criação e coleta de dados na tabela SQLite](/Analises/01-medias/medias_coleta_NBA.py)


## **3. Fase de Análise Estatística**

### **Definição do Tipo de Estudo**

O estudo será descritivo e exploratório:

- Análise descritiva para sumarizar as variáveis principais (médias, medianas, desvios padrão).
- Visualizações gráficas para identificar padrões (distribuições, correlações).
- Estudos comparativos entre grupos (ex.: posições ou faixas etárias).

### **Estimação de Parâmetros Populacionais**

#### Análise de Arremessos de 3 Pontos:

>[Arquivo .py para análise de dados](/Analises/01-medias/medias_coleta_NBA.py)

### **Uso de Testes Estatísticos**



## **4. Fase de Interpretação dos Resultados e Conclusões**

### **Interpretação dos Resultados**

Os resultados obtidos serão interpretados à luz das perguntas definidas nos objetivos. Por exemplo:

- Há homogeneidade dos arremessos de 3 pontos varia significativamente entre diferentes faixas etárias, com jogadores mais experientes mostrando maior consistência?

### **Conclusões e Recomendações**

Com base nos resultados:

- ->31 anos: 0.2772
- 28-31 anos: 0.3310
- 23-27 anos: 0.3587
- < 23 anos: 0.4079

1. Recomendar áreas específicas para desenvolvimento ou treinamento, como foco no aprimoramento da consistência de arremessos de 3 pontos para jogadores mais jovens[1].
2. Sugerir estratégias de rotação de jogadores baseadas na eficiência por faixa etária.

### **Visualização dos Resultados**

![homogeneidade_fg3](/Analises/01-medias/homogeneidade_fg3.png)
Este gráfico fornece uma compreensão visual rápida das tendências e padrões identificados nos dados.

### Análise da Eficiência nos Arremessos de 3 Pontos por Faixa Etária

#### Tendência Observada

Os dados revelam uma tendência interessante na eficiência dos arremessos de 3 pontos em relação à idade dos jogadores da NBA:

1. Jogadores mais jovens (< 23 anos): 0.4079
2. Jogadores entre 23-27 anos: 0.3587
3. Jogadores entre 28-31 anos: 0.3310
4. Jogadores mais velhos (> 31 anos): 0.2772

#### Interpretação dos Resultados

1. **Declínio com a Idade**: Observa-se uma clara tendência de diminuição na eficiência dos arremessos de 3 pontos à medida que a idade dos jogadores aumenta[2].

2. **Pico de Eficiência**: Os jogadores mais jovens (abaixo de 23 anos) apresentam a maior eficiência, com uma taxa de acerto de aproximadamente 40,79%[2].

3. **Queda Gradual**: Há uma redução gradual na eficiência conforme as faixas etárias avançam, com uma queda mais acentuada após os 31 anos[2].

4. **Experiência vs. Condição Física**: Estes dados sugerem que, apesar da experiência acumulada, fatores como condição física e agilidade, mais presentes em jogadores mais jovens, podem ter um impacto significativo na eficiência dos arremessos de longa distância[2].

### Implicações Práticas

#### Para Treinadores e Equipes

1. **Desenvolvimento de Jovens Talentos**: Investir no treinamento e desenvolvimento de jogadores jovens para maximizar seu potencial nos arremessos de 3 pontos[2].

2. **Estratégias de Jogo**: Adaptar as estratégias de jogo para aproveitar a maior eficiência dos jogadores mais jovens em arremessos de 3 pontos, especialmente em momentos críticos[2].

3. **Programas de Condicionamento**: Implementar programas de condicionamento físico específicos para jogadores mais velhos, visando manter sua eficiência nos arremessos de longa distância[2].

#### Para Jogadores

1. **Foco no Aprimoramento**: Jogadores mais jovens devem focar em manter e melhorar sua eficiência, enquanto jogadores mais velhos podem precisar adaptar seu jogo ou trabalhar mais intensamente para manter níveis competitivos de eficiência[2].

2. **Adaptação de Estilo de Jogo**: Jogadores mais velhos podem considerar ajustar seu estilo de jogo para compensar a diminuição na eficiência dos arremessos de 3 pontos[2].

### Considerações Finais

Esta análise fornece insights valiosos sobre como a idade afeta a eficiência nos arremessos de 3 pontos na NBA. No entanto, é importante notar que outros fatores, como posição de jogo, histórico de lesões e estilo de jogo individual, também podem influenciar esses resultados. Estudos adicionais considerando essas variáveis poderiam fornecer uma compreensão ainda mais completa deste aspecto do jogo[2].
