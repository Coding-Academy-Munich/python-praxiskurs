import random

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
SUIT_SYMBOLS = {
    "Hearts": "♥",
    "Diamonds": "♦",
    "Clubs": "♣",
    "Spades": "♠",
}
RANK_SYMBOLS = {
    "Ace": "A",
    "King": "K",
    "Queen": "Q",
    "Jack": "J",
    "10": "T",
    "9": "9",
    "8": "8",
    "7": "7",
    "6": "6",
    "5": "5",
    "4": "4",
    "3": "3",
    "2": "2",
}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self) -> str:
        return f"Card({self.suit}, {self.rank})"

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self.suit == other.suit and self.rank == other.rank

    @property
    def shorthand(self) -> str:
        """Return shorthand notation for card.

        Examples:
        >>> Card("Hearts", "Ace").shorthand
        'A♥'
        >>> Card("Diamonds", "10").shorthand
        'T♦'
        """
        return f"{RANK_SYMBOLS[self.rank]}{SUIT_SYMBOLS[self.suit]}"

    def matches(self, top_discard: "Card") -> bool:
        """Returns True if the card matches the given card.

        Cards match if they have the same suit, rank, or if the card is an 8.

        Examples:
        >>> Card("Hearts", "Ace").matches(Card("Hearts", "King"))
        True
        >>> Card("Hearts", "Ace").matches(Card("Diamonds", "Ace"))
        True
        >>> Card("Hearts", "Ace").matches(Card("Diamonds", "King"))
        False
        >>> Card("Hearts", "Ace").matches(Card("Hearts", "8"))
        True
        >>> Card("Hearts", "Ace").matches(Card("Diamonds", "8"))
        False
        >>> Card("Hearts", "8").matches(Card("Diamonds", "8"))
        True
        """
        return (
            self.suit == top_discard.suit
            or self.rank == top_discard.rank
            or self.rank == "8"
        )


def short_string(cards: list[Card]) -> str:
    """Return a short string representation of the given list of cards.

    Examples:
    >>> _cards = [Card("Hearts", "Ace"), Card("Diamonds", "10"), Card("Clubs", "2")]
    >>> short_string(_cards)
    'A♥, T♦, 2♣'
    """
    return ", ".join(card.shorthand for card in cards) if cards else "none"


class Deck:
    """A deck of (initially) 52 cards in shuffled order.

    When a card is drawn, it is removed from the deck.

    Implements `__len__` and `__getitem__` methods and can therefore be treated as a
    sequence of remaining cards.
    """

    def __init__(self):
        """Initialize deck of 52 cards. Cards are shuffled."""
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)

    def __repr__(self) -> str:
        return f"<Deck with {len(self.cards)} cards>"

    def __str__(self) -> str:
        return f"Deck with {len(self.cards)} cards" if self.cards else "Empty deck"

    def __len__(self) -> int:
        """Return the number of cards remaining in deck.

        Examples:
        >>> deck = Deck()
        >>> len(deck)
        52
        """
        return len(self.cards)

    def __getitem__(self, index) -> Card:
        """Return the card at the given index."""
        return self.cards[index]

    @property
    def short_str(self) -> str:
        """Return a short string representation of the deck."""
        return short_string(self.cards)

    def draw_card(self) -> Card | None:
        """Draw a card from the deck.

        Returns:
            Card: The card drawn from the deck.
            None: If the deck is empty.
        """
        return self.cards.pop() if self.cards else None
