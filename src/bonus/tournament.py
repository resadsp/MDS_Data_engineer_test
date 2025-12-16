# src/bonus/tournament.py
from typing import List, Set
import random

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
        """Simulate a game and return the winner"""
        winner = random.choice(self.players)
        winner.wins += 1
        # Track opponents
        for p in self.players:
            p.opponents.update({pl.name for pl in self.players if pl != p})
        return winner

class Tournament:
    def __init__(self, players: List[Player], tables_count: int, table_size: int):
        self.players = players
        self.tables_count = tables_count
        self.table_size = table_size
        self.rounds: List[List[Table]] = []

    def run_round(self):
        """Distribute players into tables and play games"""
        shuffled_players = self.players.copy()
        random.shuffle(shuffled_players)
        tables: List[Table] = []

        for i in range(self.tables_count):
            start = i * self.table_size
            end = start + self.table_size
            table_players = shuffled_players[start:end]
            if not table_players:
                break
            table = Table(table_id=i+1, max_players=self.table_size)
            table.add_players(table_players)
            table.play_game()
            tables.append(table)

        self.rounds.append(tables)

    def run_tournament(self, max_rounds: int = 10):
        for _ in range(max_rounds):
            self.run_round()

    def get_overall_winner(self) -> Player:
        return max(self.players, key=lambda p: p.wins)
