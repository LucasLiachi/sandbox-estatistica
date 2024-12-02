import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.static import teams
import os

# Definir diretório base usando caminho absoluto
BASE_DIR = os.path.join(os.getcwd(), 'Analises', 'histograma-times-NBA')
os.makedirs(BASE_DIR, exist_ok=True)
print(f"Diretório de trabalho: {BASE_DIR}")  # Debug

# Função para criar uma tabela e inserir dados no banco de dados SQLite
def criar_e_inserir_no_banco_de_dados(data, tabela, conexao):
    df = pd.DataFrame(data)
    df.to_sql(tabela, conexao, if_exists='replace', index=False)

# Criar conexão com o banco de dados SQLite
conexao = sqlite3.connect(os.path.join(BASE_DIR, 'nba_teams.db'))

# Obter dados de todas as equipes da NBA
all_teams = teams.get_teams()

# Inserir dados das equipes na tabela 'nba_teams' no banco de dados
criar_e_inserir_no_banco_de_dados(all_teams, 'nba_teams', conexao)

# Criar DataFrame com os dados das equipes
df = pd.DataFrame(all_teams)

# Análise por estado
state_counts = df['state'].value_counts().sort_values(ascending=True)

# Criar gráfico de barras horizontal (melhor visualização)
plt.figure(figsize=(10, 8))
plt.barh(state_counts.index, state_counts.values, color='#1f77b4')
plt.title('Distribuição de Times da NBA por Estado', pad=20)
plt.xlabel('Número de Times')
plt.ylabel('Estado')

# Adicionar valores nas barras
for i, v in enumerate(state_counts.values):
    plt.text(v, i, f' {v}', va='center')

# Remover linhas de grade e ajustar margens
plt.grid(False)
plt.margins(x=0.2)

plt.tight_layout()

# Salvar o gráfico
output_path = os.path.join(BASE_DIR, 'distribuicao_times_nba.png')
print(f"Salvando gráfico em: {output_path}")
plt.savefig(output_path, dpi=300, bbox_inches='tight', format='png')
plt.show()

# Fechar a conexão com o banco de dados
conexao.close()