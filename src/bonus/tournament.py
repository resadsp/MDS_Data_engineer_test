import random
from itertools import combinations

class Player:
    def __init__(self, name: str):
        self.name = name
        self.wins = 0
        self.opponents = set()

    def __repr__(self):
        return f"Player({self.name}, wins={self.wins})"

class Table:
    def __init__(self, table_id: int, max_players: int):
        self.table_id = table_id
        self.max_players = max_players
        self.players = []

    def add_players(self, players):
        if len(players) > self.max_players:
            raise ValueError("Too many players for the table")
        self.players = players

    def play_game(self):
        winner = random.choice(self.players)
        winner.wins += 1
        for p in self.players:
            p.opponents.update({pl.name for pl in self.players if pl != p})
        return winner

class Tournament:
    def __init__(self, players, tables: int, seats: int):
        self.players = players
        self.tables = tables
        self.seats = seats
        self.winner = None

    def run(self):
        # Round-robin: svi igraju protiv svakog
        for p1, p2 in combinations(self.players, 2):
            p1.opponents.add(p2.name)
            p2.opponents.add(p1.name)
            p1.wins += 1
        self.winner = max(self.players, key=lambda p: p.wins)
        return self


def round_robin_schedule(players):
    """Round-robin schedule: vraća listu listi parova po rundi"""
    n = len(players)
    rounds = []
    for i in range(n-1):
        round_pairs = []
        for j in range(n // 2):
            p1 = players[j]
            p2 = players[n - 1 - j]
            round_pairs.append((p1, p2))
        players = [players[0]] + [players[-1]] + players[1:-1]
        rounds.append(round_pairs)
    return rounds


def test_round_robin_schedule_full():
    teams = ["A", "B", "C"]
    sched = tournament.round_robin_schedule(teams)
    # Očekujemo listu parova, npr. ('A', 'B')
    assert all(isinstance(pair, tuple) and len(pair) == 2 for pair in sched)
