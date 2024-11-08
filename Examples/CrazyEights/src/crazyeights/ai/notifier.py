from crazyeights.deck import Card
from crazyeights.notifier import TerminalNotifier


class ComputerPlayerNotifier(TerminalNotifier):
    """A notifier for automated players that prints to the console."""

    def notify_card_played(self, card_played: Card) -> None:
        print(f"{self.player.name} plays {card_played.shorthand}")

    def notify_suit_picked(self, suit: str) -> None:
        print(f"{self.player.name} picks {suit} for crazy 8")
