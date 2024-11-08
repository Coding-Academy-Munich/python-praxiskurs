from enum import StrEnum

from crazyeights.deck import Card, Deck
from crazyeights.player import Player, TurnAction


class GameResult(StrEnum):
    """Reasons for the game ending."""

    NOT_ENOUGH_PLAYERS = "Not enough players"
    NO_PLAYABLE_CARDS = "No playable cards"
    CURRENT_PLAYER_WON = "Current player won"


class CrazyEightsGame:
    def __init__(self, players):
        self.deck = Deck()
        self.players = players
        self.discard_pile = [self.deck.draw_card()]
        self.current_player_index = 0
        self.deal_cards()

    def __repr__(self):
        return f"CrazyEightsGame({self.players!r})"

    def deal_cards(self):
        for player in self.players:
            player.draw_n_cards(self.deck, 7)

    @property
    def top_discard(self):
        return self.discard_pile[-1]

    def discard(self, card: Card):
        self.discard_pile.append(card)

    @property
    def current_player(self) -> Player:
        return self.players[self.current_player_index]

    def pick_next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play(self) -> GameResult:
        if len(self.players) < 2:
            print("Must have at least two players to play.")
            return GameResult.NOT_ENOUGH_PLAYERS

        num_players_skipped = 0

        while True:
            action_taken = self.current_player.take_turn(self)
            if action_taken == TurnAction.FAILED_DRAW:
                num_players_skipped += 1
                if num_players_skipped == len(self.players):
                    return GameResult.NO_PLAYABLE_CARDS
            else:
                num_players_skipped = 0

            # Check for win
            if self.current_player.has_won():
                return GameResult.CURRENT_PLAYER_WON

            self.pick_next_player()

    def print_result(self, reason: GameResult):
        if reason == GameResult.NO_PLAYABLE_CARDS:
            print(
                "Deck is empty and no players can match "
                f"{self.top_discard.shorthand}."
            )
            print("No one wins!")
        else:
            print(f"\n{self.current_player.name} wins!")
