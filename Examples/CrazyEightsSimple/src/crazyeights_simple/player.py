from enum import StrEnum
from typing import Optional, TYPE_CHECKING

from .deck import Card, Deck, RANKS, SUITS

if TYPE_CHECKING:
    from .game import CrazyEightsGame


class TurnAction(StrEnum):
    """The action a player took on their turn."""

    PLAYED_CARD = "played"
    DREW_CARD = "drawn"
    FAILED_DRAW = "draw failed"


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def __repr__(self) -> str:
        return f"Player({self.name!r})"

    def __str__(self) -> str:
        return f"{self.name}"

    def draw_card(self, deck: Deck) -> Card | None:
        card = deck.draw_card()
        if card:
            self.hand.append(card)
        return card

    def draw_n_cards(self, deck: Deck, n: int) -> None:
        for _ in range(n):
            self.draw_card(deck)

    def take_turn(self, game: "CrazyEightsGame") -> TurnAction:
        self.notify_turn(game.top_discard)

        played_card = self.try_to_play_card(game)
        if not played_card:
            drawn_card = self.draw_and_play_card(game)
            return TurnAction.DREW_CARD if drawn_card else TurnAction.FAILED_DRAW
        return TurnAction.PLAYED_CARD

    def try_to_play_card(self, game: "CrazyEightsGame") -> bool:
        card_to_play = self.pick_card_to_play(game.top_discard)
        if card_to_play is None:
            return False

        self.play_card(game, card_to_play)
        return True

    def pick_card_to_play(self, top_discard: Card) -> Card | None:
        """Pick the highest ranked playable card."""
        playable_cards = self.get_playable_cards(top_discard)
        if playable_cards:
            return max(playable_cards, key=lambda card: RANKS.index(card.rank))
        return None

    def get_playable_cards(self, top_discard: Card) -> list[Card]:
        return [card for card in self.hand if card.matches(top_discard)]

    def draw_and_play_card(self, game: "CrazyEightsGame") -> bool:
        drawn_card = self.draw_card(game.deck)
        self.notify_card_drawn(drawn_card)

        if drawn_card:
            self.try_to_play_card(game)
            return True
        return False

    def play_card(self, game: "CrazyEightsGame", card: Card) -> None:
        self.hand.remove(card)
        game.discard(card)
        self.notify_card_played(card)
        if card.rank == "8":
            card.suit = self.pick_suit()
            self.notify_suit_picked(card.suit)

    def pick_suit(self) -> str:
        """Pick the suit that the player has the most of."""
        suit_counts = {suit: 0 for suit in SUITS}
        for card in self.hand:
            suit_counts[card.suit] += 1
        return max(suit_counts, key=lambda suit: suit_counts[suit])

    def has_won(self) -> bool:
        return not self.hand

    def notify_turn(self, top_discard: "Card", **kwargs) -> None:
        print(f"\n{self.name}'s turn. Top of discard pile: {top_discard}")
        print(f"{self.name}'s hand: {short_string(self.hand)}")

        playable_cards = self.get_playable_cards(top_discard)
        if playable_cards:
            print(f"Playable cards: {short_string(playable_cards)}")

    def notify_card_drawn(self, card_drawn: Optional["Card"]) -> None:
        print("No playable card.", end=" ")
        if card_drawn:
            print(f"{self.name} draws {card_drawn}")
        else:
            print(f"{self.name} cannot draw. Deck is empty.")

    def notify_card_played(self, card_played: Card) -> None:
        print(f"{self.name} plays {card_played}")

    def notify_suit_picked(self, suit: str) -> None:
        print(f"{self.name} picks {suit} for crazy 8")


def short_string(cards: list[Card]) -> str:
    return ", ".join(str(card) for card in cards) if cards else "none"
