from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playergamelog
from python.shared.methods import save_as_parquet
from nba_api.stats.library.parameters import SeasonAll


class GetPlayerStats:
    def __init__(self):
        self.get_all_teams()
        self.players_list = self.get_all_players()
        self.game_logs = self.get_game_logs(self.players_list)

    def get_all_teams(self):
        all_teams = teams.get_teams()
        save_as_parquet(all_teams, 'allTeams')
        return all_teams

    def get_all_players(self):
        all_players = players.get_players()
        save_as_parquet(all_players, 'allPlayers')
        return all_players

    def get_game_logs(self, player_list):
        all_game_logs = []
        for player in player_list:
            try:
                player_game_logs = playergamelog.PlayerGameLog(player_id=player['id'], season=SeasonAll.all)
                player_game_logs_dict = player_game_logs.get_dict()
                formatted_player_game_logs = self.format_game_logs(player_game_logs_dict)
                all_game_logs.extend(formatted_player_game_logs)
            except Exception as e:
                print(str(e))
        save_as_parquet(all_game_logs, 'allGameLogs')
        return all_game_logs

    def format_game_logs(self, game_log_dict):
        formatted_logs = []
        headers = game_log_dict['resultSets'][0]['headers']
        row_set = game_log_dict['resultSets'][0]['rowSet']

        for row in row_set:
            formatted_row = {}
            for i in range(len(headers)):
                formatted_row[headers[i]] = row[i]
            formatted_logs.append(formatted_row)

        return formatted_logs


if __name__ == '__main__':
    ratings = GetPlayerStats()
