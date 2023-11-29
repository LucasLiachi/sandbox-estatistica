from requests import get

BASE_URL = "http://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

def get_links():
    response = get(BASE_URL+ALL_JSON).json()
    return response["links"]

def get_currentScoreboard():
    response = get(BASE_URL+get_links()["currentScoreboard"]).json()
    games = response.keys("games")

    for game in games:
        print(game.keys())

print(get_currentScoreboard())
