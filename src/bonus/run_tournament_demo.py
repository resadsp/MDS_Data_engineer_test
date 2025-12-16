# src/bonus/run_tournament_demo.py
from bonus.tournament import Player, Tournament

def main():
    players = [Player(f"P{i+1}") for i in range(16)]
    tournament = Tournament(players, tables_count=4, table_size=4)

    tournament.run_tournament(max_rounds=5)

    winner = tournament.get_overall_winner()
    print(f"Overall winner: {winner}")

    print("\nPlayers and their opponents:")
    for p in players:
        print(f"{p.name}: wins={p.wins}, opponents={p.opponents}")

if __name__ == "__main__":
    main()
