from abc import ABC

from crazyeights.ai.notifier import ComputerPlayerNotifier
from crazyeights.deck import Card, RANKS, SUITS
from crazyeights.player import Player


class ComputerPlayer(Player, ABC):
    """A superclass for automated players."""

    def __init__(self, name):
        notifier = ComputerPlayerNotifier(self)
        super().__init__(name, notifier)

    def pick_suit(self) -> str:
        """Pick the suit that the player has the most of."""
        suit_counts = {suit: 0 for suit in SUITS}
        for card in self.hand:
            suit_counts[card.suit] += 1
        return max(suit_counts, key=lambda suit: suit_counts[suit])


class GreedyPlayer(ComputerPlayer):
    """An automated player that always plays the highest ranked card."""

    def pick_card_to_play(self, top_discard: Card) -> Card | None:
        """Pick the highest ranked playable card."""
        playable_cards = self.get_playable_cards(top_discard)
        if playable_cards:
            return max(playable_cards, key=lambda card: RANKS.index(card.rank))
        elif eight := self.get_eight():
            return eight
        return None
