from bonus.tournament import Tournament, Player

def test_tournament_single_player():
    p = Player("Solo")
    t = Tournament(players=[p], tables=1, seats=1)
    t.run()
    assert t.winner == p
    assert len(p.opponents) == 0

def test_tournament_opponents_count():
    players = [Player(f"P{i}") for i in range(1, 5)]
    t = Tournament(players=players, tables=2, seats=2)
    t.run()
    for p in players:
        assert len(p.opponents) == 3  # each plays with everyone else
