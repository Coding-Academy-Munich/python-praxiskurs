from crazyeights_simple.player import Player
from crazyeights_simple.__main__ import main

EXPECTED = """
Alice's turn. Top of discard pile: K♦
Alice's hand: A♣, 3♠, K♥, T♣, 2♦, 7♦, 6♦
Playable cards: K♥, 2♦, 7♦, 6♦
Alice plays K♥

Bob's turn. Top of discard pile: K♥
Bob's hand: K♠, 9♥, Q♣, 5♥, Q♦, 6♣, J♥
Playable cards: K♠, 9♥, 5♥, J♥
Bob plays K♠

Alice's turn. Top of discard pile: K♠
Alice's hand: A♣, 3♠, T♣, 2♦, 7♦, 6♦
Playable cards: 3♠
Alice plays 3♠

Bob's turn. Top of discard pile: 3♠
Bob's hand: 9♥, Q♣, 5♥, Q♦, 6♣, J♥
No playable card. Bob draws 9♠
Bob plays 9♠

Alice's turn. Top of discard pile: 9♠
Alice's hand: A♣, T♣, 2♦, 7♦, 6♦
No playable card. Alice draws 7♥

Bob's turn. Top of discard pile: 9♠
Bob's hand: 9♥, Q♣, 5♥, Q♦, 6♣, J♥
Playable cards: 9♥
Bob plays 9♥

Alice's turn. Top of discard pile: 9♥
Alice's hand: A♣, T♣, 2♦, 7♦, 6♦, 7♥
Playable cards: 7♥
Alice plays 7♥

Bob's turn. Top of discard pile: 7♥
Bob's hand: Q♣, 5♥, Q♦, 6♣, J♥
Playable cards: 5♥, J♥
Bob plays J♥

Alice's turn. Top of discard pile: J♥
Alice's hand: A♣, T♣, 2♦, 7♦, 6♦
No playable card. Alice draws 8♣
Alice plays 8♣
Alice picks ♦ for crazy 8

Bob's turn. Top of discard pile: 8♦
Bob's hand: Q♣, 5♥, Q♦, 6♣
Playable cards: Q♦
Bob plays Q♦

Alice's turn. Top of discard pile: Q♦
Alice's hand: A♣, T♣, 2♦, 7♦, 6♦
Playable cards: 2♦, 7♦, 6♦
Alice plays 7♦

Bob's turn. Top of discard pile: 7♦
Bob's hand: Q♣, 5♥, 6♣
No playable card. Bob draws A♦
Bob plays A♦

Alice's turn. Top of discard pile: A♦
Alice's hand: A♣, T♣, 2♦, 6♦
Playable cards: A♣, 2♦, 6♦
Alice plays A♣

Bob's turn. Top of discard pile: A♣
Bob's hand: Q♣, 5♥, 6♣
Playable cards: Q♣, 6♣
Bob plays Q♣

Alice's turn. Top of discard pile: Q♣
Alice's hand: T♣, 2♦, 6♦
Playable cards: T♣
Alice plays T♣

Bob's turn. Top of discard pile: T♣
Bob's hand: 5♥, 6♣
Playable cards: 6♣
Bob plays 6♣

Alice's turn. Top of discard pile: 6♣
Alice's hand: 2♦, 6♦
Playable cards: 6♦
Alice plays 6♦

Bob's turn. Top of discard pile: 6♦
Bob's hand: 5♥
No playable card. Bob draws 9♦
Bob plays 9♦

Alice's turn. Top of discard pile: 9♦
Alice's hand: 2♦
Playable cards: 2♦
Alice plays 2♦

Alice wins!
"""


def test_main_function(capsys):
    main([Player("Alice"), Player("Bob")], 2023)
    captured = capsys.readouterr()
    assert captured.out == EXPECTED
