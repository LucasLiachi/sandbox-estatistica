import requests
import sqlite3
from peewee import SqliteDatabase, Model, CharField

# Configurações do banco de dados SQLite
db = SqliteDatabase('db/nba_teams.db')

# Definição do modelo de dados
class Team(Model):
    name = CharField()
    city = CharField()

    class Meta:
        database = db

# Inicialização do banco de dados
db.connect()
db.create_tables([Team])

# URL da API da NBA para obter detalhes dos times
api_url = 'http://stats.nba.com/stats/teamdetails'

# Requisição à API
response = requests.get(api_url)

# Verificar se a resposta foi bem-sucedida (código 200)
if response.status_code == 200:
    try:
        data = response.json()

        # Coleta de dados e inserção no banco de dados
        teams = data['league']['standard']
        for team_data in teams:
            name = team_data['fullName']
            city = team_data['city']

            # Inserindo dados no banco de dados SQLite
            Team.create(name=name, city=city)

        # Exemplo de consulta ao banco de dados
        query_result = Team.select()
        for team in query_result:
            print(f"Team: {team.name}, City: {team.city}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao processar a resposta da API: {e}")

else:
    print(f"Erro na requisição à API. Código de status: {response.status_code}")
    
    try:
        error_data = response.json()
        print(f"Detalhes do erro: {error_data}")
    except:
        print("Não foi possível obter detalhes do erro.")
        
# Fechar a conexão com o banco de dados
db.close()
