from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP

class TeamDetails(Endpoint):
    # ... (the rest of the class implementation as provided in the original code)

    # Function to get team details for a list of team IDs
    def get_team_details_for_ids(team_ids):
        team_details_list = []

        for team_id in team_ids:
            team_details = TeamDetails(team_id)
            team_details_list.append(team_details)

        return team_details_list

# Example usage
if __name__ == "__main__":
    # Replace with actual team IDs
    team_ids = [1610612759, 1610612744, 1610612761, 1610612755]

    # Get team details for the list of team IDs
    team_details_list = TeamDetails.get_team_details_for_ids(team_ids)

    # Display team information
    for team_details in team_details_list:
        print("Team Background for Team ID", team_details.parameters["TeamID"])
        print("Team Name:", team_details.team_background.get_dict()["NICKNAME"])
        print("City:", team_details.team_background.get_dict()["CITY"])
        print("Arena:", team_details.team_background.get_dict()["ARENA"])
        print("------------------------------")
