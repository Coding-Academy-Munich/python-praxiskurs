from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from crazyeights.deck import Card
    from crazyeights.player import Player


class Notifier(ABC):
    """Interface for notifying players of game events."""

    def __init__(self, player: "Player"):
        self.player = player

    @abstractmethod
    def notify(self, message: str) -> None:
        """Notify the player of the given message."""
        ...

    @abstractmethod
    def notify_turn(self, top_discard: "Card") -> None:
        """Notify the player that it is their turn."""
        ...

    @abstractmethod
    def notify_card_played(self, card_played: "Card") -> None:
        """Notify the player that a card was played."""
        ...

    @abstractmethod
    def notify_card_drawn(self, card_drawn: "Card") -> None:
        """Notify the player that a card was drawn."""
        ...

    @abstractmethod
    def notify_suit_picked(self, suit: str) -> None:
        """Notify the player that a suit was picked."""
        ...


class TerminalNotifier(Notifier, ABC):
    """Superclass for notifiers that print to the terminal."""

    def notify(self, message: str) -> None:
        print(message)

    def notify_turn(self, top_discard: "Card", **kwargs) -> None:
        from crazyeights.deck import short_string

        print(
            f"\n{self.player.name}'s turn. Top of discard pile: {top_discard.shorthand}"
        )
        print(f"{self.player.name}'s hand: {short_string(self.player.hand)}")

        playable_cards = self.player.get_playable_cards(top_discard)
        if playable_cards:
            print(f"Playable cards: {short_string(playable_cards)}")

    def notify_card_drawn(self, card_drawn: Optional["Card"]) -> None:
        print("No playable card.", end=" ")
        if card_drawn:
            print(f"{self.player.name} draws {card_drawn.shorthand}")
        else:
            print(f"{self.player.name} cannot draw. Deck is empty.")
