from bonus.tournament import Player, Tournament

def main():
    players = [Player(f"P{i+1}") for i in range(16)]
    tournament = Tournament(players, tables=4, seats=4)
    tournament.run()
    winner = tournament.winner
    print(f"Overall winner: {winner}")

    print("\nPlayers and their opponents:")
    for p in players:
        print(f"{p.name}: wins={p.wins}, opponents={p.opponents}")

def run_tournament_demo(team_names):
    players = [Player(name) for name in team_names]
    t = Tournament(players, tables=2, seats=2)
    t.run()
    return t.winner

# Ako funkcija u stvarnom kodu zove run_tournament umesto run_demo
def test_demo_runs_without_errors():
    teams = ["Team A", "Team B", "Team C"]
    try:
        run_tournament_demo.run_tournament(teams)  # Ispravljeno ime funkcije
    except Exception as e:
        pytest.fail(f"Demo execution failed: {e}")


def test_run_tournament_demo_executes():
    teams = ["Team A", "Team B", "Team C"]
    try:
        run_tournament_demo.run_tournament_demo(teams)  # Prosleđujemo timove
    except Exception as e:
        pytest.fail(f"Demo execution failed: {e}")


if __name__ == "__main__":
    main()
