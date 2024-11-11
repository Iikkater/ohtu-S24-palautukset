class Player:
    def __init__(self, data):
        self.name = data.get('name')
        self.nationality = data.get('nationality')
        self.assists = data.get('assists')
        self.goals = data.get('goals')
        self.points = self.goals + self.assists
        self.team = data.get('team')
        self.games = data.get('games')
        self.id = data.get('id')
    
    def __str__(self):
        return f"{self.name:20} {self.team:3} {self.goals:3} + {self.assists:<3} = {self.points:<3}"
