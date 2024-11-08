import random

import click

from crazyeights.game import CrazyEightsGame
from crazyeights.interactive.player import InteractivePlayer
from crazyeights.ai.player import GreedyPlayer


def play_game(players):
    game = CrazyEightsGame(players)
    result = game.play()
    game.print_result(result)


def main(interactive, greedy, seed):
    interactive_players = [InteractivePlayer(name) for name in interactive]
    computer_players = [GreedyPlayer(name) for name in greedy]
    players = interactive_players + computer_players
    if len(players) < 2:
        for i in range(2 - len(players)):
            players.append(GreedyPlayer(f"Computer {i + 1}"))
    if seed >= 0:
        random.seed(seed)
    play_game(players)


@click.command()
@click.option(
    "-i", "--interactive", multiple=True, help="Names of interactive players."
)
@click.option("-g", "--greedy", multiple=True, help="Names of greedy players.")
@click.option("--seed", default=-1, help="Random seed.")
@click.version_option()
def app(interactive, greedy, seed):
    main(interactive, greedy, seed)


if __name__ == "__main__":
    app()
