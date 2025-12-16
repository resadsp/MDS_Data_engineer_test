import random
from typing import List, Set
from itertools import combinations

class Player:
    def __init__(self, name: str):
        self.name = name
        self.wins = 0
        self.opponents: Set[str] = set()

    def __repr__(self):
        return f"Player({self.name}, wins={self.wins})"

class Table:
    def __init__(self, table_id: int, max_players: int):
        self.table_id = table_id
        self.max_players = max_players
        self.players: List[Player] = []

    def add_players(self, players: List[Player]):
        if len(players) > self.max_players:
            raise ValueError("Too many players for the table")
        self.players = players

    def play_game(self) -> Player:
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
        for p1, p2 in combinations(self.players, 2):
            p1.opponents.add(p2.name)
            p2.opponents.add(p1.name)
            p1.wins += 1
        self.winner = max(self.players, key=lambda p: p.wins)
        return self
