class TennisGame:
    scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.get_tied_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.get_endgame_score()
        else:
            return self.get_regular_score()

    def get_tied_score(self):
        if self.player1_score < 3:
            return f"{self.scores[self.player1_score]}-All"
        else:
            return "Deuce"

    def get_endgame_score(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def get_regular_score(self):
        return f"{self.scores[self.player1_score]}-{self.scores[self.player2_score]}"
