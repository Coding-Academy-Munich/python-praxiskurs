# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Properties</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ## Properties
#
# Wie können wir es ermöglichen auf einen Punkt sowohl mittels der `x` und
# `y`-Koordinaten zuzugreifen, als auch mittels Radius und Winkel?

# %%
import math


# %%
class GeoPointV0:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def get_radius(self):
        return math.hypot(self.x, self.y)

    def get_angle(self):
        return math.atan2(self.y, self.x)

    def __repr__(self):
        return (
            f"GeoPointV0({self.x:.1f}, {self.y:.1f}, "
            f"r={self.get_radius():.2f}, θ={self.get_angle():.2f})"
        )


# %%
p = GeoPointV0()
p

# %%
assert p.x == 0.0
assert p.y == 0.0
assert p.get_radius() == 0.0
assert p.get_angle() == 0.0

# %%
p = GeoPointV0(1.0, 0.0)
p

# %%
assert p.x == 1.0
assert p.y == 0.0
assert p.get_radius() == 1.0
assert p.get_angle() == 0.0

# %%
p = GeoPointV0(0.0, 2.0)
p

# %%
from math import isclose, pi

assert p.x == 0.0
assert p.y == 2.0
assert p.get_radius() == 2.0
assert isclose(p.get_angle(), pi / 2)

# %% [markdown]
#
# Es ist unschön, dass bei der Verwendung von `GeoPointV0` die Attribute `x` und `y`
# anders behandelt werden müssen als `radius` und `angle`:

# %%
p = GeoPointV0(1.0, 1.0)

# %%
print(p.x, p.y, p.get_radius(), p.get_angle())


# %% [markdown]
# ## Properties mit `@property`
#
# Der `@property`-Dekorator erlaubt es uns, Methoden wie Attribute zu verwenden.

# %%
class GeoPointV1:  # noqa
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    @property
    def radius(self):
        return (self.x**2 + self.y**2) ** 0.5

    @property
    def angle(self):
        return math.atan2(self.y, self.x)

    def __repr__(self):
        return (
            f"GeoPointV1({self.x:.1f}, {self.y:.1f}, "
            f"r={self.radius:.2f}, θ={self.angle:.2f})"
        )


# %%
p = GeoPointV1()
p

# %%
assert p.x == 0.0
assert p.y == 0.0
assert p.radius == 0.0
assert p.angle == 0.0

# %%
p = GeoPointV1(1.0, 0.0)
p

# %%
assert p.x == 1.0
assert p.y == 0.0
assert p.radius == 1.0
assert p.angle == 0.0

# %%
p = GeoPointV1(0.0, 2.0)
p

# %%
from math import isclose, pi

assert p.x == 0.0
assert p.y == 2.0
assert p.radius == 2.0
assert isclose(p.angle, pi / 2)

# %% [markdown]
#
# ## Schreibgeschützte Attribute
#
# Ein häufiger Anwendungsfall für Properties ist das Bereitstellen eines
# schreibgeschützten Zugriffs auf einen internen Wert.
#
# - Wir speichern den eigentlichen Wert in einem "privaten" Attribut (z.B.
#   `_radius`).
# - Wir definieren eine Property (`radius`), um den Wert zu lesen.
# - Dies verhindert unbeabsichtigtes Überschreiben des Attributs von außen,
#   erlaubt aber Lesezugriff.
# - Für den Benutzer sieht es so aus, als ob er auf ein Attribut zugreift.

# %%
class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        # Store the actual value in a "private" attribute
        self._radius = radius

    @property
    def radius(self):
        # The public property only provides read access to _radius
        print(f"Getting radius (internal value: {self._radius})")
        return self._radius

    @property
    def area(self):
        return math.pi * (self._radius**2)

    def __repr__(self):
        return f"Circle(radius={self._radius:.2f})"


# %%
c = Circle(5.0)
print(c)

# %%
# Reading the property works
print(f"Radius: {c.radius}")
print(f"Area: {c.area}")

# %%
# Trying to set the property fails (AttributeError: property 'radius' of 'Circle' object has no setter)
try:
    c.radius = 10.0
except AttributeError as e:
    print(f"Error: {e}")

# %%
# The internal value remains unchanged
print(c)
print(f"Internal value: {c._radius}")  # We can still access _radius (by convention)


# %% [markdown]
# ## Workshop: Buchinformation
#
# Erstellen Sie eine Klasse `Book`, die Informationen über ein Buch verwaltet:
#
# - Implementieren Sie Titel und Autor als schreibgeschützte Attribute.
# - Implementieren Sie eine Property `citation`, die einen Zitationsstring im
#   Format `"Titel" by Autor` zurückgibt.
# - Fügen Sie eine `__repr__`-Methode hinzu, die Titel und Autor anzeigt.
# - Testen Sie die Klasse, indem Sie ein Buch erstellen und die
#   `citation`-Property abrufen.

# %%
class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def citation(self):
        return f'\"{self.title}\" by {self.author}'

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author})"

# %%
b = Book("1984", "George Orwell")

# %%
print(b)  # Book(title=1984, author=George Orwell)
print(b.citation)  # "1984" by George Orwell
print(b.title)  # 1984
print(b.author)  # George Orwell
# %%
