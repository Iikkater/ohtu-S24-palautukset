import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
    
class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_konstruktori_alustaa_pelaajat(self):

        self.assertEqual(len(self.stats._players), 5)

    def test_search_palauttaa_pelaajan(self):

        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_ei_loyda_pelaajaa(self):

        player = self.stats.search("Koivu")
        self.assertIsNone(player)

    def test_team_palauttaa_oikeat_pelaajat(self):

        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Kurri")
        self.assertEqual(players[2].name, "Gretzky")

    def test_top_palauttaa_oikein(self):
            
        players = self.stats.top(3)
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")