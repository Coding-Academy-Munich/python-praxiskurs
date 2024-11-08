from crazyeights.deck import Card
from crazyeights.notifier import TerminalNotifier


class InteractivePlayerNotifier(TerminalNotifier):
    """A notifier for interactive players that prints to the console."""

    def notify_card_played(self, card_played: Card) -> None:
        pass

    def notify_suit_picked(self, suit: str) -> None:
        pass
