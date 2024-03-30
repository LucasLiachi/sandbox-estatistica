# https://pypi.org/project/nba_api/

import sqlite3
import pandas as pd
from nba_api.stats.endpoints import playercareerstats

# Função para criar uma tabela e inserir dados no banco de dados SQLite
def criar_e_inserir_no_banco_de_dados(data, tabela, conexao):
    df = pd.DataFrame(data)
    df.to_sql(tabela, conexao, if_exists='replace', index=False)

# Criar conexão com o banco de dados SQLite
conexao = sqlite3.connect('db/nba_players_base.db')

# Obter dados da carreira do jogador Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203999')
dados_jogador = career.get_data_frames()[0]

# Inserir dados do jogador na tabela 'nikola_jokic' no banco de dados
criar_e_inserir_no_banco_de_dados(dados_jogador, 'nikola_jokic', conexao)

# Fechar a conexão com o banco de dados
conexao.close()