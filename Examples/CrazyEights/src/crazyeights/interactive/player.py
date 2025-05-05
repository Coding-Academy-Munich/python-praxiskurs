from crazyeights.deck import Card, SUITS
from crazyeights.interactive.notifier import InteractivePlayerNotifier
from crazyeights.player import Player


class InteractivePlayer(Player):
    """A player that inputs its moves from the console."""

    def __init__(self, name):
        notifier = InteractivePlayerNotifier(self)
        super().__init__(name, notifier)

    def pick_card_to_play(self, top_discard: Card) -> Card | None:
        """Pick a card to play from the given list of playable cards.

        Returns the card the player wants to play, or None if the player cannot play
        any of the cards."""
        playable_cards = self.get_playable_cards(top_discard)
        if playable_cards:
            for i, card in enumerate(playable_cards, 1):
                print(f"{i}: {card.shorthand}")
            while True:
                try:
                    index = int(input("Pick a card to play (-1 to skip): "))
                    if index == -1:
                        return None
                    return playable_cards[index - 1]
                except (ValueError, IndexError):
                    print("Invalid input. Try again.")
        else:
            return None

    def pick_suit(self) -> str:
        """Pick a suit after playing an 8."""
        while True:
            suit = input("Pick a suit (h♥/d♦/c♣/s♠): ")
            if suit.lower() in ["h", "hearts", "♥"]:
                suit = "Hearts"
            elif suit.lower() in ["d", "diamonds", "♦"]:
                suit = "Diamonds"
            elif suit.lower() in ["c", "clubs", "♣"]:
                suit = "Clubs"
            elif suit.lower() in ["s", "spades", "♠"]:
                suit = "Spades"
            if suit in SUITS:
                return suit
            print("Invalid suit. Try again.")
