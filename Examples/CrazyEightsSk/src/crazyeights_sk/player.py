from typing import Optional

from .deck import Card, Deck


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def __repr__(self) -> str:
        return f"Player({self.name!r})"

    def __str__(self) -> str:
        return f"{self.name} ({', '.join(str(c) for c in self.hand)})"

    def draw_n_cards(self, deck: "Deck", n: int) -> None:
        for _ in range(n):
            self.draw_card(deck)

    def draw_card(self, deck: "Deck") -> Optional["Card"]:
        card = deck.draw_card()
        if card:
            self.hand.append(card)
        return card
