import pytest
from src.bonus import tournament

def test_round_robin_schedule_basic():
    teams = ["A", "B", "C", "D"]
    sched = tournament.round_robin_schedule(teams)
    assert len(sched) == len(teams) - 1
    for round_ in sched:
        flattened = [t for match in round_ for t in match]
        assert sorted(flattened) == sorted(teams)
