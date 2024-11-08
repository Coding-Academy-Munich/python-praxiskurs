# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>GRASP Pattern: Creator</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# <img src="img/cards-15.png" width="100%">

# %% [markdown]
#
# - Wer ist verantwortlich für das Erzeugen der Karten?
# - Wer ist verantwortlich für das Erzeugen des Kartenspiels?
# - Wer ist verantwortlich für das Mischen der Karten?
# - Wer ist verantwortlich für das Erzeugen des Ablagestapels (mit der ersten Karte)?

# %% [markdown]
#
# ### Erzeugen der Karten
#
# Kandidaten:
#
# - `Game`
# - `Player`
# - `Deck`
# - Eine andere Klasse?

# %% [markdown]
#
# <img src="img/crazy-eights-dm.svg" width="70%"
#      style="margin-left: auto; margin-right: auto;">

# %% [markdown]
#
# ## Das Creator Pattern (GRASP)
#
# ### Frage
#
# - Wer ist verantwortlich für die Erzeugung eines Objekts?
#
# ### Antwort
#
# Klasse `A` bekommt die Verantwortung, ein Objekt der Klasse `B` zu erzeugen,
# wenn eine oder mehrere der folgenden Bedingungen zutreffen:
#
# - `A` enthält `B` (oder ist Eigentümer von `B`)
# - `A` speichert `B` (z.B. in einer Datenbank)
# - `A` benutzt `B` eng
# - `A` hat die initialisierenden Daten, die `B` benötigt


# %% [markdown]
#
# <div style="float:left;margin:auto;padding:80px 0;width:35%">
# <ul>
# <li> <strike><code>Game</code></strike></li>
# <li> <strike><code>Player</code></strike></li>
# <li> <code>Deck</code></li>
# <li> <strike>Eine andere Klasse?</strike></li>
# </ul>
# </div>
# <img src="img/crazy-eights-dm.svg"
#      style="float:right;margin:auto;width:60%"/>

# %%
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self) -> str:
        return f"Card({self.suit}, {self.rank})"

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self.suit == other.suit and self.rank == other.rank


# %%
SUITS = ["♥", "♦", "♣", "♠"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


# %%
class Deck:  # noqa
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def __repr__(self) -> str:
        return f"<Deck with {len(self.cards)} cards>"

    def __str__(self) -> str:
        return f"Deck with {len(self.cards)} cards" if self.cards else "Empty deck"

    def __len__(self) -> int:
        return len(self.cards)

    def __getitem__(self, index) -> Card:
        return self.cards[index]


# %%
deck = Deck()

# %%
deck

# %%
len(deck)

# %%
deck[0]

# %%
deck[10]


# %% [markdown]
#
# ### Mischen der Karten
#
# - Wer ist verantwortlich für das Mischen der Karten?
# - Überlegung: Die Karten müssen nur einmal gemischt werden
# - Damit können wir das Kartenspiel gleich beim Erzeugen mischen

# %% [markdown]
#
# ### Faustregel
#
# Wo immer möglich verlagere Arbeit in die Initialisierungsphase

# %%
import random


# %%
class Deck:  # noqa
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)

    def __repr__(self) -> str:
        return f"<Deck with {len(self.cards)} cards>"

    def __str__(self) -> str:
        return f"Deck with {len(self.cards)} cards" if self.cards else "Empty deck"

    def __len__(self) -> int:
        return len(self.cards)

    def __getitem__(self, index) -> Card:
        return self.cards[index]


# %%
deck = Deck()

# %%
deck

# %%
len(deck)

# %%
deck[0]

# %%
deck[10]


# %% [markdown]
#
# ### Erzeugen des Kartenspiels
#
# <div style="float:left;margin:auto;padding:80px 0;width:35%">
# <ul>
# <li> <code>Game</code></li>
# <li> <code>Board</code></li>
# <li> <code>Player</code></li>
# <li> Eine andere Klasse?</li>
# </ul>
# </div>
# <img src="img/crazy-eights-dm.svg"
#      style="float:right;margin:auto;width:60%"/>

# %% [markdown]
#
# ### Erzeugen des Kartenspiels
#
# <div style="float:left;margin:auto;padding:80px 0;width:35%">
# <ul>
# <li> <code>Game</code></li>
# <li> <strike><code>Board</code></strike></li>
# <li> <strike><code>Player</code></strike></li>
# <li> <strike>Eine andere Klasse?</strike></li>
# </ul>
# </div>

# %%
class CrazyEightsGame:  # noqa
    def __init__(self, players):
        self.deck = Deck()
        self.players = players


# %% [markdown]
#
# ## Workshop: Drei Gewinnt
#
# - Erweitern Sie Ihre Implementierung von Drei Gewinnt, so dass alle benötigten
#   Objekte erzeugt werden
# - Verwenden Sie dazu das Creator Pattern

# %%
from enum import StrEnum


# %%
class Mark(StrEnum):
    EMPTY = " "
    X = "X"
    O = "O"


# %%
class Field:
    def __init__(self):
        self.mark = Mark.EMPTY

    def __str__(self):
        return self.mark


# %%
class Board:
    def __init__(self):
        self.fields = [[Field() for _ in range(3)] for _ in range(3)]


# %%
class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark


# %%
class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player_index = 0
