from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table

def main():
    print("NHL statistics by nationality\n")
    input_year = input("Select season [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/]: ")

    while True:
        input_nationality = input("\nSelect nationality [AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR]: ")

        url = f"https://studies.cs.helsinki.fi/nhlstats/{input_year}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(input_nationality)

        console = Console()
        table = Table(title=f"Top scorers of {input_nationality} season {input_year}")

        table.add_column("name", justify="left", style="cyan", no_wrap=True)
        table.add_column("team", justify="left", style="magenta")
        table.add_column("goals", justify="right", style="green")
        table.add_column("assists", justify="right", style="green")
        table.add_column("points", justify="right", style="green")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

        console.print(table)
        print("")

if __name__ == "__main__":
    main()
