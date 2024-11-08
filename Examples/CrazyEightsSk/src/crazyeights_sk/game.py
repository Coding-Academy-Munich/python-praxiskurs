from .deck import Deck
from .player import Player


class CrazyEightsGame:
    def __init__(self, players):
        self.deck: Deck = Deck()
        self.players: list[Player] = players
        self.deal_cards()

    def __repr__(self):
        return f"CrazyEightsGame({self.players!r})"

    def __str__(self):
        result = f"Crazy Eights with {len(self.players)} players:\n"
        for player in self.players:
            result += f"  {player}\n"
        return result

    def deal_cards(self):
        for player in self.players:
            player.draw_n_cards(self.deck, 7)
