import sqlite3
import pandas as pd
from nba_api.stats.static import teams

# Função para criar uma tabela e inserir dados no banco de dados SQLite
def criar_e_inserir_no_banco_de_dados(data, tabela, conexao):
    df = pd.DataFrame(data)
    df.to_sql(tabela, conexao, if_exists='replace', index=False)

# Criar conexão com o banco de dados SQLite
conexao = sqlite3.connect('db/nba.db')

# Obter dados de todas as equipes da NBA
all_teams = teams.get_teams()

# Inserir dados das equipes na tabela 'nba_teams' no banco de dados
criar_e_inserir_no_banco_de_dados(all_teams, 'nba_teams', conexao)

# Fechar a conexão com o banco de dados
conexao.close()