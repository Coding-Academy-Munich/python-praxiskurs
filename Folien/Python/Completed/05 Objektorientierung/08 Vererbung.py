# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Vererbung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
#  ## Vererbung
#
# Wir haben folgende Klasse implementiert:

# %%
import random


# %%
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x:.1f}, {self.y:.1f})"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def randomize(self):
        self.x = random.gauss(2, 0.5)
        self.y = random.gauss(3, 0.5)


# %%
p = Point(1, 1)
p

# %%
p.move(2, 3)
p

# %%
p.randomize()
p


# %% [markdown]
#
# Wie können wir farbige Punkte einführen, ohne die komplette Funktionalität
# von `Point` neu implementieren zu müssen?

# %%
class ColorPoint(Point):
    def __init__(self, x=0, y=0, color="black"):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return f"ColorPoint({self.x:.1f}, {self.y:.1f}, {self.color!r})"

    def randomize(self):
        super().randomize()
        self.color = random.choice(["black", "red", "green", "blue", "yellow", "white"])


# %%
cp = ColorPoint(2, 3)
assert isinstance(cp, Point)
# cp


# %%
assert cp.x == 2.0
assert cp.y == 3.0
assert cp.color == "black"

# %%
cp.color = "red"

# %%
assert cp.x == 2.0
assert cp.y == 3.0
assert cp.color == "red"

# %%
cp.move(2, 3)
# cp


# %%
assert cp.x == 4.0
assert cp.y == 6.0
assert cp.color == "red"

# %%
cp.randomize()
# cp

# %% [markdown]
#
# ## Workshop: Mitarbeiter
#
# Im Folgenden soll eine Klassenhierarchie für Mitarbeiter einer Firma erstellt
# werden:
#
# - Mitarbeiter können entweder Arbeiter oder Manager sein
# - Jeder Mitarbeiter der Firma hat einen Namen, eine Personalnummer und ein
#   Grundgehalt
# - Für jeden Arbeiter werden die angefallenen Überstunden und der Stundenlohn
#   gespeichert.
# - Das Gehalt eines Arbeiters berechnet sich als das 13/12-fache des
#   Grundgehalts plus der Bezahlung für die Überstunden
# - Jeder Manager hat einen individuellen Bonus
# - Das Gehalt eines Managers berechnet sich als das 13/12-fache des
#   Grundgehalts plus Bonus
#
# Implementieren Sie Python Klassen `Mitarbeiter`, `Arbeiter` und `Manager` mit
# geeigneten Attributen und einer Methode `gehalt()`, die das Gehalt berechnet.
#

# %%
from dataclasses import dataclass

# %%
@dataclass
class Mitarbeiter:
    name: str
    pers_nr: str
    grundgehalt: float

    def gehalt(self):
        return 13 / 12 * self.grundgehalt


# %%
@dataclass
class Arbeiter(Mitarbeiter):
    überstunden: float = 0.0
    stundensatz: float = 0.0

    def gehalt(self):
        return super().gehalt() + self.überstunden * self.stundensatz


# %%
@dataclass
class Manager(Mitarbeiter):
    bonus: float

    def gehalt(self):
        return super().gehalt() + self.bonus


# %% [markdown]
#
# Erzeugen Sie einen Arbeiter mit Namen Hans, Personalnummer 123, einem
# Grundgehalt von  36000.0 Euro, der 3.5 Überstunden zu je 40.0 Euro gearbeit
# hat. Drucken Sie das Gehalt aus.

# %%
a = Arbeiter("Hans", "123", 36_000, 3.5, 40.0)
print(a.gehalt())
a

# %% [markdown]
#
# Schreiben sie Assertions, die die Funktionalität der Klasse `Arbeiter` testen.

# %%
# Diese Assertions sind überflüssig!
assert a.name == "Hans"
assert a.pers_nr == "123"
assert a.grundgehalt == 36_000
assert a.überstunden == 3.5
assert a.stundensatz == 40.0

# Diese Assertion sollte vorhanden sein
assert a.gehalt() == 39_140.0

# %% [markdown]
#
# Erzeugen Sie einen Manager mit Namen Sepp, Personalnummer 843, der ein
# Grundgehalt von 60000.0 Euro und einen Bonus von 30000.0 Euro hat. Drucken Sie
# das Gehalt aus.

# %%
m = Manager("Sepp", "843", 60_000.0, 30_000.0)
print(m.gehalt())
m

# %% [markdown]
# Testen Sie die Funktionalität der `Manager` Klasse.

# %%
assert m.gehalt() == 95_000.0


# %% [markdown]
# ## Lösung ohne Dataclasses:

# %%
class Mitarbeiter:
    def __init__(self, name, pers_nr, grundgehalt):
        self.name = name
        self.pers_nr = pers_nr
        self.grundgehalt = grundgehalt

    def gehalt(self):
        return 13 / 12 * self.grundgehalt


# %%
class Arbeiter(Mitarbeiter):
    def __init__(self, name, pers_nr, grundgehalt, überstunden, stundensatz):
        super().__init__(name, pers_nr, grundgehalt)
        self.überstunden = überstunden
        self.stundensatz = stundensatz

    def __repr__(self):
        return (
            f"Arbeiter({self.name!r}, {self.pers_nr!r}, {self.grundgehalt}, "
            f"{self.überstunden}, {self.stundensatz})"
        )

    def gehalt(self):
        return super().gehalt() + self.überstunden * self.stundensatz


# %%
class Manager(Mitarbeiter):
    def __init__(self, name, pers_nr, grundgehalt, bonus):
        super().__init__(name, pers_nr, grundgehalt)
        self.bonus = bonus

    def __repr__(self):
        return (
            f"Manager({self.name!r}, {self.pers_nr!r}, {self.grundgehalt}, "
            f"{self.bonus})"
        )

    def gehalt(self):
        return super().gehalt() + self.bonus


# %%
a = Arbeiter("Hans", 123, 36_000, 3.5, 40)

# %%
assert a.gehalt() == 39_140.0


# %%
m = Manager("Sepp", 843, 60_000, 30_000)

# %%
assert m.gehalt() == 95_000.0

# %% [markdown]
#
# Eine Visualisierung für `super()`-Aufrufe bei Vererbung mit Python Tutor
# ist [hier](shorturl.at/efDKW).
