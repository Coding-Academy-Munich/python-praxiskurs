from abc import ABC, abstractmethod
from enum import StrEnum
from typing import TYPE_CHECKING, Optional

from crazyeights.deck import Card, Deck
from crazyeights.notifier import Notifier

if TYPE_CHECKING:
    from crazyeights.game import CrazyEightsGame


class TurnAction(StrEnum):
    """The action a player took on their turn."""

    PLAYED_CARD = "played"
    DREW_CARD = "drawn"
    FAILED_DRAW = "draw failed"


class Player(ABC):
    def __init__(
        self, name: str, notifier: Notifier, hand: Optional[list["Card"]] = None
    ):
        self.name = name
        self.hand = [] if hand is None else hand
        self.notifier = notifier

    def __repr__(self) -> str:
        return f"Player({self.name!r}, {self.hand!r})"

    def __str__(self) -> str:
        return f"{self.name} ({', '.join(str(c) for c in self.hand)})"

    @property
    def hand_string(self) -> str:
        """Return a string representation of the player's hand."""
        return ", ".join(card.shorthand for card in self.hand)

    def draw_card(self, deck: Deck) -> Card | None:
        """Draw a card from the deck and add it to the player's hand.

        Returns the card drawn, or None if the deck is empty."""
        card = deck.draw_card()
        if card:
            self.hand.append(card)
        return card

    def draw_n_cards(self, deck: Deck, n: int) -> None:
        """Draw n cards from the deck and add them to the player's hand."""
        for _ in range(n):
            self.draw_card(deck)

    def get_playable_cards(self, top_discard: Card) -> list[Card]:
        """Return a list of cards that can be played on the given discard.

        If the player has no playable cards, an empty list is returned."""
        return [card for card in self.hand if card.matches(top_discard)]

    @abstractmethod
    def pick_card_to_play(self, top_discard: Card) -> Card | None:
        """Pick a card to play from the given list of playable cards.

        Returns the card the player wants to play, or None if the player cannot play
        any of the cards."""
        ...

    @abstractmethod
    def pick_suit(self) -> str:
        """Pick a suit after playing an 8."""
        ...

    def get_eight(self) -> Card | None:
        """Returns an 8 (of any suit) if the player has one in their hand.

        Returns None if the player does not have an 8 in their hand."""
        for card in self.hand:
            if card.rank == "8":
                return card
        return None

    def all_eights(self) -> list[Card]:
        """Returns all 8s in the player's hand."""
        return [card for card in self.hand if card.rank == "8"]

    def try_to_play_card(self, game: "CrazyEightsGame") -> bool:
        """Try to play a card from the player's hand.

        Returns True if a card was played, False otherwise."""

        card_to_play = self.pick_card_to_play(game.top_discard)
        if card_to_play is None:
            return False

        self.play_card(game, card_to_play)
        return True

    def draw_and_play_card(self, game: "CrazyEightsGame") -> bool:
        """Draw a card from the deck and play it if possible.

        Returns True if a card could be drawn, False otherwise."""
        drawn_card = self.draw_card(game.deck)
        self.notifier.notify_card_drawn(drawn_card)

        if drawn_card:
            self.try_to_play_card(game)
            return True
        return False

    def play_card(self, game: "CrazyEightsGame", card: Card) -> None:
        """Removes the given card from the player's hand.

        Raises a ValueError if the card is not in the player's hand."""
        self.hand.remove(card)
        game.discard(card)
        self.notifier.notify_card_played(card)
        if card.rank == "8":
            card.suit = self.pick_suit()
            self.notifier.notify_suit_picked(card.suit)

    def take_turn(self, game: "CrazyEightsGame") -> TurnAction:
        self.notifier.notify_turn(game.top_discard)

        played_card = self.try_to_play_card(game)
        if not played_card:
            drawn_card = self.draw_and_play_card(game)
            return TurnAction.DREW_CARD if drawn_card else TurnAction.FAILED_DRAW
        return TurnAction.PLAYED_CARD

    def has_won(self) -> bool:
        """Returns True if the player has no cards left in their hand."""
        return not self.hand
