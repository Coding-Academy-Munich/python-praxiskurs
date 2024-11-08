from crazyeights_sk.__main__ import main


def test_main_function(capsys):
    main([], 2023)
    captured = capsys.readouterr()
    assert captured.out == (
        "Crazy Eights with 2 players:\n"
        "  Computer 1 (K♦, 7♠, 4♣, A♠, 9♦, 2♠, Q♣)\n"
        "  Computer 2 (T♦, 3♠, 8♥, 9♥, 8♦, T♣, 9♣)\n\n"
    )
