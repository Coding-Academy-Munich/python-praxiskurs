import random

import pytest

from crazyeights.ai.player import GreedyPlayer
from crazyeights.deck import Card, Deck


@pytest.fixture
def deck():
    random.seed(2023)
    return Deck()


def test_deck_fixture(deck):
    assert len(deck) == 52
    assert deck.cards[:4] == [
        Card("Hearts", "7"),
        Card("Spades", "Jack"),
        Card("Diamonds", "7"),
        Card("Clubs", "7"),
    ]


class TestCard:
    @pytest.mark.parametrize(
        "suit,rank",
        [
            ("Hearts", "Ace"),
            ("Spades", "Jack"),
            ("Diamonds", "10"),
            ("Clubs", "2"),
        ],
    )
    def test_eq(self, suit, rank):
        assert Card(suit, rank) == Card(suit, rank)

    @pytest.mark.parametrize(
        "suit,rank,expected",
        [
            ("Hearts", "Ace", "Ace of Hearts"),
            ("Diamonds", "King", "King of Diamonds"),
            ("Clubs", "Queen", "Queen of Clubs"),
            ("Spades", "Jack", "Jack of Spades"),
            ("Hearts", "10", "10 of Hearts"),
            ("Diamonds", "8", "8 of Diamonds"),
            ("Clubs", "4", "4 of Clubs"),
            ("Spades", "2", "2 of Spades"),
        ],
    )
    def test_str(self, suit, rank, expected):
        assert str(Card("Hearts", "Ace")) == "Ace of Hearts"

    @pytest.mark.parametrize(
        "suit,rank,expected",
        [
            ("Hearts", "Ace", "A♥"),
            ("Diamonds", "King", "K♦"),
            ("Clubs", "Queen", "Q♣"),
            ("Spades", "Jack", "J♠"),
            ("Hearts", "10", "T♥"),
            ("Diamonds", "8", "8♦"),
            ("Clubs", "4", "4♣"),
            ("Spades", "2", "2♠"),
        ],
    )
    def test_shorthand(self, suit, rank, expected):
        assert Card(suit, rank).shorthand == expected


@pytest.fixture
def player():
    return GreedyPlayer("Alice")


class TestGreedyPlayer:
    def test_show_hand(self, player):
        assert player.hand_string == ""

    def test_draw_card(self):
        pass
