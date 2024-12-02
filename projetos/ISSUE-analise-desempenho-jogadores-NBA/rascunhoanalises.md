# **Exercício Analítico de Média: Dados dos Jogadores da NBA**

## **1. Fase de Planejamento da Pesquisa**

### **Definição de Objetivos**

O objetivo principal deste projeto é analisar o desempenho dos jogadores ativos da NBA com base em suas estatísticas de carreira. A análise busca identificar padrões, tendências e insights que possam ser úteis para equipes, treinadores e analistas esportivos. Exemplos de perguntas a serem respondidas:

- Quais jogadores têm o maior impacto em 3 pontos, assistências e rebotes?
- Como o desempenho varia entre diferentes posições ou idades?
- Existe correlação entre minutos jogados e eficiência geral?
- Como a eficiência nos arremessos de 3 pontos varia entre diferentes faixas etárias?

### **Planejamento do Estudo**

- **Tipo de estudo**: Estudo descritivo e exploratório, utilizando dados históricos das estatísticas dos jogadores.
- **Fontes de dados**: API oficial da NBA (`nba_api`), que fornece informações detalhadas sobre os jogadores.
- **Ferramentas utilizadas**: Python (bibliotecas como `pandas`, `numpy`, `matplotlib`, `seaborn`), SQLite para armazenamento, e Jupyter Notebook para visualização.

### **Determinação das Variáveis**

As variáveis principais a serem analisadas incluem:

- **Desempenho individual**: Pontos por jogo (PTS), assistências (AST), rebotes (REB), eficiência (PER).
- **Dados demográficos**: Idade, altura, peso, posição.
- **Participação em jogos**: Minutos jogados (MIN), jogos disputados (GP).
- **Eficiência ofensiva e defensiva**: Taxa de aproveitamento de arremessos (FG%), roubos de bola (STL), tocos (BLK).
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

```python
import sqlite3
import pandas as pd
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

def criar_e_inserir_no_banco_de_dados(data, tabela, conexao):
    df = pd.DataFrame(data)
    df.to_sql(tabela, conexao, if_exists='append', index=False)

conexao = sqlite3.connect('nba_players.db')

all_players = players.get_active_players()
criar_e_inserir_no_banco_de_dados(all_players, 'nba_players', conexao, modo='replace')

for player in all_players:
    career = playercareerstats.PlayerCareerStats(player_id=player['id'])
    dados_jogador = career.get_data_frames()[0]
    criar_e_inserir_no_banco_de_dados(dados_jogador, 'nba_players_stats', conexao)

conexao.close()
```

## **3. Fase de Análise Estatística**

### **Definição do Tipo de Estudo**

O estudo será descritivo e exploratório:

- Análise descritiva para sumarizar as variáveis principais (médias, medianas, desvios padrão).
- Visualizações gráficas para identificar padrões (distribuições, correlações).
- Estudos comparativos entre grupos (ex.: posições ou faixas etárias).

### **Estimação de Parâmetros Populacionais**

Exemplo de análises:

- Média de pontos por jogo entre todas as posições.
- Proporção média de minutos jogados em relação ao total possível.
- Desvio padrão das taxas de aproveitamento ofensivo.
- Homogeneidade dos arremessos de 3 pontos por grupo etário.

#### Exemplo de Análise Geral:

```python
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conexao = sqlite3.connect('nba_players.db')

players_stats = pd.read_sql("SELECT * FROM nba_players_stats", conexao)

print(players_stats[['PTS', 'AST', 'REB']].describe())

sns.boxplot(x='POSITION', y='PTS', data=players_stats)
plt.title("Distribuição dos Pontos por Posição")
plt.show()

conexao.close()
```

#### Exemplo de Análise de Arremessos de 3 Pontos:

```python
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

conexao = sqlite3.connect('Analises/01-medias/medias_NBA_players.db')

query = """
SELECT PLAYER_ID, PLAYER_AGE, FG3M, FG3A
FROM nba_players_stats
WHERE FG3A > 0
"""

df = pd.read_sql_query(query, conexao)

df['FG3_PCT'] = df['FG3M'] / df['FG3A']

df['AGE_GROUP'] = pd.cut(
    df['PLAYER_AGE'], 
    bins=[0, 23, 27, 31, 100],
    labels=['< 23 anos', '23-27 anos', '28-31 anos', '> 31 anos']
)

def desvio_relativo_medio(grupo):
    desvios = grupo.std()
    medias = grupo.mean()
    return desvios / medias

resultados = (
    df.groupby('AGE_GROUP', observed=True)['FG3_PCT']
    .apply(desvio_relativo_medio)
    .sort_values()
)

conexao.close()

print("Homogeneidade dos arremessos de 3 pontos por grupo etário:")
for grupo, valor in resultados.items():
    print(f"{grupo}: {valor:.4f}")

plt.figure(figsize=(10, 6))
resultados.plot(kind='bar')
plt.title('Homogeneidade dos Arremessos de 3 Pontos por Grupo Etário')
plt.xlabel('Grupo Etário')
plt.ylabel('Desvio Relativo Médio')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('Analises/01-medias/homogeneidade_fg3.png')
print("O gráfico foi salvo como 'homogeneidade_fg3.png'.")
```

### **Uso de Testes Estatísticos**

Aplicação de testes estatísticos para validar hipóteses:

- Teste t para comparar médias entre grupos (ex.: armadores vs pivôs).
- Análise de variância (ANOVA) para verificar diferenças significativas entre múltiplos grupos.
- Correlação entre variáveis como minutos jogados e eficiência.

#### Exemplo:

```python
from scipy.stats import ttest_ind

pg_pts = players_stats[players_stats['POSITION'] == 'PG']['PTS']
c_pts = players_stats[players_stats['POSITION'] == 'C']['PTS']

t_stat, p_value = ttest_ind(pg_pts, c_pts)
print(f"Teste t: t-stat={t_stat}, p-value={p_value}")
```

## **4. Fase de Interpretação dos Resultados e Conclusões**

### **Interpretação dos Resultados**

Os resultados obtidos serão interpretados à luz das perguntas definidas nos objetivos. Por exemplo:

- Jogadores da posição X apresentam maior média de pontos devido à sua participação ofensiva mais ativa.
- Existe uma correlação moderada entre minutos jogados e eficiência geral.
- A homogeneidade dos arremessos de 3 pontos varia significativamente entre diferentes faixas etárias, com jogadores mais experientes mostrando maior consistência[1].

### **Conclusões e Recomendações**

Com base nos resultados:

1. Identificar os melhores desempenhos individuais ou coletivos.
2. Fornecer insights para melhorar estratégias em quadra ou na gestão das equipes.
3. Recomendar áreas específicas para desenvolvimento ou treinamento, como foco no aprimoramento da consistência de arremessos de 3 pontos para jogadores mais jovens[1].
4. Sugerir estratégias de rotação de jogadores baseadas na eficiência por faixa etária.

### **Visualização dos Resultados**

A análise inclui a criação de gráficos para melhor visualização dos dados, como o gráfico de barras mostrando a homogeneidade dos arremessos de 3 pontos por grupo etário[1]. Esses gráficos podem ser utilizados para apresentações e relatórios, fornecendo uma compreensão visual rápida das tendências e padrões identificados nos dados.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/14005329/310dcd59-1ba2-497e-9dd0-10e3e66fdce3/medias_about_me.md