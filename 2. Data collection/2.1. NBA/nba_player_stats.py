import sqlite3
import pandas as pd
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

# Função para criar uma tabela e inserir dados no banco de dados SQLite
def criar_e_inserir_no_banco_de_dados(data, tabela, conexao):
    df = pd.DataFrame(data)
    df.to_sql(tabela, conexao, if_exists='append', index=False)

# Criar conexão com o banco de dados SQLite
conexao = sqlite3.connect('3. Database/3.1. NBA/nba_players.db')

# Obter dados de todas os jogadores ativos na NBA
all_players = players.get_active_players()

# Iterar sobre todos os jogadores
for player in all_players:
    career = playercareerstats.PlayerCareerStats(player_id=player['id'])
    dados_jogador = career.get_data_frames()[0]
    
    # Inserir dados do jogador na tabela correspondente no banco de dados
    criar_e_inserir_no_banco_de_dados(dados_jogador, 'nba_players_stats', conexao)

# Fechar a conexão com o banco de dados
conexao.close()
