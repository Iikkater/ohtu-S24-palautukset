from player import Player

class PlayerStats:
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nationality: str):
        players = []

        for player_dict in self.players.get_players():
            player = Player(player_dict)
            if player.nationality == nationality:
                players.append(player)

        players = sorted(players,
                     key=lambda player: player.points,
                     reverse=True)
        
        return players