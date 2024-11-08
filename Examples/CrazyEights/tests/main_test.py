import random

from crazyeights.__main__ import play_game
from crazyeights.ai.player import GreedyPlayer

EXPECTED = """
Alice's turn. Top of discard pile: K♦
Alice's hand: 7♠, 4♣, A♠, 9♦, 2♠, Q♣, T♦
Playable cards: 9♦, T♦
Alice plays T♦

Bob's turn. Top of discard pile: T♦
Bob's hand: 3♠, 8♥, 9♥, 8♦, T♣, 9♣, 6♠
Playable cards: 8♥, 8♦, T♣
Bob plays T♣

Alice's turn. Top of discard pile: T♣
Alice's hand: 7♠, 4♣, A♠, 9♦, 2♠, Q♣
Playable cards: 4♣, Q♣
Alice plays Q♣

Bob's turn. Top of discard pile: Q♣
Bob's hand: 3♠, 8♥, 9♥, 8♦, 9♣, 6♠
Playable cards: 8♥, 8♦, 9♣
Bob plays 9♣

Alice's turn. Top of discard pile: 9♣
Alice's hand: 7♠, 4♣, A♠, 9♦, 2♠
Playable cards: 4♣, 9♦
Alice plays 9♦

Bob's turn. Top of discard pile: 9♦
Bob's hand: 3♠, 8♥, 9♥, 8♦, 6♠
Playable cards: 8♥, 9♥, 8♦
Bob plays 9♥

Alice's turn. Top of discard pile: 9♥
Alice's hand: 7♠, 4♣, A♠, 2♠
No playable card. Alice draws K♥
Alice plays K♥

Bob's turn. Top of discard pile: K♥
Bob's hand: 3♠, 8♥, 8♦, 6♠
Playable cards: 8♥, 8♦
Bob plays 8♥
Bob picks Spades for crazy 8

Alice's turn. Top of discard pile: 8♠
Alice's hand: 7♠, 4♣, A♠, 2♠
Playable cards: 7♠, A♠, 2♠
Alice plays A♠

Bob's turn. Top of discard pile: A♠
Bob's hand: 3♠, 8♦, 6♠
Playable cards: 3♠, 8♦, 6♠
Bob plays 8♦
Bob picks Spades for crazy 8

Alice's turn. Top of discard pile: 8♠
Alice's hand: 7♠, 4♣, 2♠
Playable cards: 7♠, 2♠
Alice plays 7♠

Bob's turn. Top of discard pile: 7♠
Bob's hand: 3♠, 6♠
Playable cards: 3♠, 6♠
Bob plays 6♠

Alice's turn. Top of discard pile: 6♠
Alice's hand: 4♣, 2♠
Playable cards: 2♠
Alice plays 2♠

Bob's turn. Top of discard pile: 2♠
Bob's hand: 3♠
Playable cards: 3♠
Bob plays 3♠

Bob wins!
"""


def test_main_function(capsys):
    random.seed(2023)
    play_game([GreedyPlayer("Alice"), GreedyPlayer("Bob")])
    captured = capsys.readouterr()
    assert captured.out == EXPECTED
