import pytest
from src.bonus import run_tournament_demo

def test_demo_runs_without_errors():
    teams = ["Team A", "Team B", "Team C"]
    try:
        run_tournament_demo.run_demo(teams)
    except Exception as e:
        pytest.fail(f"Demo execution failed: {e}")


def run_demo(teams):
    print("Demo running for teams:", teams)
    # dummy logic za test


def test_run_tournament_demo_executes():
    # Samo provjeravamo da se funkcija izvrši bez grešaka
    run_tournament_demo.run_tournament_demo()
