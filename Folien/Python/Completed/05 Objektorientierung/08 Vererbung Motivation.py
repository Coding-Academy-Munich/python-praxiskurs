# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Vererbung: Motivation</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
#  ## Motivation für Vererbung
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


# %%
def build_rectangle(left_lower: Point, right_upper: Point):
    return [left_lower, right_upper]


# %%
build_rectangle(Point(0, 0), Point(1, 1))


# %% [markdown]
#
# Wie können wir farbige Punkte einführen?

# %%
class ColorPoint:
    def __init__(self, x=0, y=0, color="black"):
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f"ColorPoint({self.x:.1f}, {self.y:.1f}, {self.color!r})"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def randomize(self):
        self.x = random.gauss(2, 0.5)
        self.y = random.gauss(3, 0.5)


# %%
cp = ColorPoint(2, 3)
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
# ### Probleme
#
# - Code-Duplizierung
# - Das Python Typsystem weiß nicht, dass `ColorPoint` ein `Point` ist:

# %%
isinstance(Point(0, 0), Point)

# %%
isinstance(ColorPoint(0, 0), Point)


# %%
build_rectangle(ColorPoint(0, 0), ColorPoint(1, 1))

# %% [markdown]
#
# ### Welche Lösungen gibt es?
#
# - Vererbung: `ColorPoint` erbt von `Point`
# - Protokolle: `ColorPoint` und `Point` implementieren das gleiche Protokoll
#
# Ergebnis: Subtyp- bzw. Konsistenz-Beziehung
