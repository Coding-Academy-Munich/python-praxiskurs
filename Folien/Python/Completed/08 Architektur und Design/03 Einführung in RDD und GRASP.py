# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Einführung in RDD und GRASP</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# <img src="img/interaction.png" width="100%">


# %% [markdown]
#
# Eine Möglichkeit, vom Domänenmodell zu einem Entwurf zu kommen, ist
# Responsibility-Driven Design (RDD).
#
# - Systeme: interagierende Objekte
# - Verhalten von Objekten durch Klassen beschrieben
# - Klassen für die wichtigsten Konzepte des Domänenmodells
#   - Manche Attribute aus dem Domänenmodell
# - Zum Verfeinern: Verantwortlichkeiten

# %% [markdown]
#
# ## Verantwortlichkeiten (Vereinfacht)
#
# - **Doing:** Ein Objekt
#   - erledigt selber eine Aufgabe
#   - initiiert eine Aktivität in einem anderen Objekt
# - **Knowing:** Ein Objekt
#   - kennt seinen gekapselten Zustand
#   - kennt andere Objekte

# %% [markdown]
#
# ## Merkregel
#
# - Assoziationen aus Domänenmodell: "Knowing"-Verantwortlichkeiten
#   - Dadurch: geringe Repräsentationslücke (low representational gap)
# - Operationen aus Domänenmodell: "Doing"-Verantwortlichkeiten

# %% [markdown]
#
# ## Kollaboration
#
# Verantwortlichkeiten werden oft durch Kollaboration mehrerer Objekte und
# Methoden implementiert.
#
# Beim RDD betrachten wir ein OO-Design als Sammlung miteinander kollaborierender
# Objekte mit verschiedenen Verantwortlichkeiten

# %% [markdown]
#
# <img src="img/cards-07.png" width="100%">

# %% [markdown]
#
# ## Beispiel: Crazy Eights
#
# - Spiel mit 2-6 Spielern
# - Jeder Spieler erhält 7 Karten
# - Ziel: Alle Karten ablegen
# - Jeder Spieler legt eine Karte auf dem Stapel aller abgelegten Karten ab
# - Die abgelegte Karte muss mit der obersten Karte des Stapels übereinstimmen:
#   - die gleiche Farbe
#   - den gleichen Wert
#   - eine Acht sein
# - Wenn ein Spieler keine passende Karte hat, muss er eine Karte ziehen

# %% [markdown]
#
# ### Domänenmodell
#
# - Entitäten: Spieler, Karten, Kartenspiel, Ablage-Stapel, Spiel
# - Beziehungen:
#   - Spiel hat Spieler, Kartenspiel und Ablage-Stapel
#   - Spieler hat Karten
#   - Kartenspiel enthält Karten
#   - Ablage-Stapel enthält Karten
# - Operationen:
#   - Spiel wählt Spieler aus
#   - Spieler spielt Karte
#   - Spieler zieht Karte
#   - Spiel endet

# %% [markdown]
#
# <img src="img/crazy-eights-dm.svg" width="70%"
#      style="margin-left: auto; margin-right: auto;">


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
class Deck:
    def __init__(self):
        self.cards: list[Card] = []

    def __repr__(self) -> str:
        return f"<Deck with {len(self.cards)} cards>"

    def __str__(self) -> str:
        return f"Deck with {len(self.cards)} cards" if self.cards else "Empty deck"

    def __len__(self) -> int:
        return len(self.cards)

    def __getitem__(self, index) -> Card:
        return self.cards[index]


# %%
class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []


# %%
class CrazyEightsGame:
    def __init__(self, players, deck):
        self.deck: Deck = deck
        self.players = players


# %% [markdown]
#
# ## GRASP
#
# - GRASP (General Responsibility Assignment Software Patterns) beschreibt Prinzipien,
#   und Techniken, die RDD unterstützen
# - GRASP Patterns kann man beim Modellieren mit UML oder beim Programmieren anwenden
# - Pattern:
#   - *Benanntes*, *bekanntes* Problem/Lösungs-Paar
#   - Kann in neuen Situationen angewandt werden

# %% [markdown]
#
# ## Grasp Patterns: Übersicht
#
# - High Cohesion
# - Low Coupling
# - Creator
# - Information Expert
# - Controller
# - Polymorphism
# - Pure Fabrication
# - Indirection
# - Protected Variations

# %% [markdown]
#
# ## Workshop: Drei Gewinnt (Tic Tac Toe)
#
# Das Spiel Drei Gewinnt (Tic Tac Toe) wird auf einem 3x3 Feld gespielt. Zwei
# Spieler setzen abwechselnd ihr Zeichen (X oder O) auf ein freies Feld. Der
# Spieler, der als erstes drei Zeichen in eine Reihe, Spalte oder Diagonale
# setzen kann, gewinnt.
#
# - Entwerfen Sie ein Domänenmodell für das Spiel Drei Gewinnt
#   - Welche Entitäten gibt es?
#   - Welche Beziehungen gibt es?
# - Implementieren Sie das Domänenmodell in Python
#
# *Hint:* Die Implementierung des Spiels muss nicht vollständig sein. Es reicht,
# wenn Sie die Entitäten und Beziehungen implementieren.

# %% [markdown]
#
# ### Domänenmodell
#
# - Entitäten: Spieler, Spielbrett, Feld, Spiel, Markierung
# - Beziehungen:
#   - Spielbrett enthält Felder
#   - Feld enthält Markierung
# - Operationen:
#   - Spiel wählt Spieler aus
#   - Spieler setzt Markierung auf Feld


# %% [markdown]
# <img src="img/ttt-dm.svg" width="40%"
#      style="margin-left: auto; margin-right: auto;">


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
class Player:  # noqa
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark


# %%
class Board:
    def __init__(self):
        self.fields = []


# %%
class Game:
    def __init__(self):
        self.board = None
        self.players = None
