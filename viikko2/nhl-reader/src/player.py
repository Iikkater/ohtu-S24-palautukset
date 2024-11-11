class Player:
    def __init__(self, data):
        self.name = data.get('name')
        self.nationality = data.get('nationality')
        self.assists = data.get('assists')
        self.goals = data.get('goals')
        self.team = data.get('team')
        self.games = data.get('games')
        self.id = data.get('id')
    
    def __str__(self):
        return f"{self.name} team {self.team} goals {self.goals} assists {self.assists}"
