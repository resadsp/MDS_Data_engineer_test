# tests/test_bonus.py
import pytest
from src.bonus.tournament import Player, Tournament

def test_tournament_runs():
    players = [Player(f"P{i+1}") for i in range(8)]
    tournament = Tournament(players, tables_count=2, table_size=4)
    tournament.run_tournament(max_rounds=3)

    winner = tournament.get_overall_winner()
    assert isinstance(winner, Player)
    assert winner.wins > 0
