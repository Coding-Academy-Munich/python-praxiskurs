import random
import click
from .player import Player
from .game import CrazyEightsGame


def main(player, seed):
    players = [Player(name) for name in player]
    if len(players) < 2:
        for i in range(2 - len(players)):
            players.append(Player(f"Computer {i + 1}"))
    if seed >= 0:
        random.seed(seed)
    game = CrazyEightsGame(players)
    game.play()


@click.command()
@click.option("-p", "--player", multiple=True, help="Names of computer players.")
@click.option("--seed", default=-1, help="Random seed.")
@click.version_option()
def app(player, seed):
    main(player, seed)


if __name__ == "__main__":
    app()
