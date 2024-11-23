import sqlite3
import pandas as pd
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

# Função para criar uma tabela e inserir dados no banco de dados SQLite
def criar_e_inserir_no_banco_de_dados(data, tabela, conexao):
    df = pd.DataFrame(data)
    df.to_sql(tabela, conexao, if_exists='append', index=False)

# Criar conexão com o banco de dados SQLite
conexao = sqlite3.connect('nba_players.db')

# Obter dados de todos os jogadores ativos na NBA
all_players = players.get_active_players()
# Inserir informações básicas dos jogadores na tabela 'nba_players'
criar_e_inserir_no_banco_de_dados(all_players, 'nba_players', conexao, modo='replace')
# Iterar sobre todos os jogadores para obter estatísticas detalhadas
for player in all_players:
    career = playercareerstats.PlayerCareerStats(player_id=player['id'])
    dados_jogador = career.get_data_frames()[0]
    # Inserir estatísticas detalhadas dos jogadores na tabela 'nba_players_stats'
    criar_e_inserir_no_banco_de_dados(dados_jogador, 'nba_players_stats', conexao)

# Fechar a conexão com o banco de dados
conexao.close()