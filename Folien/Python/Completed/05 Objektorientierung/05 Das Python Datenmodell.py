# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Das Python Datenmodell</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %%
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx=0.0, dy=0.0):
        self.x += dx
        self.y += dy


# %%
p = Point(2, 5)

# %%
print(p)

# %%
p == Point(2, 5)

# %%
[2, 5] == [2, 5]


# %% [markdown]
#
# # Das Python Datenmodell
#
# Mit Dunder-Methoden können benutzerdefinierten Datentypen benutzerfreundlicher
# gestaltet werden.

# %% [markdown]
#
# Durch Definition der Methode `__repr__(self)` kann der von `repr`
# zurückgegebene String für benutzerdefinierte Klassen angepasst werden: Der
# Funktionsaufruf `repr(x)` überprüft, ob `x` eine Methode `__repr__` hat und
# ruft diese auf, falls sie existiert.

# %%
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %%
p = Point(2, 5)

# %%
print(repr(p))

# %% [markdown]
#
# Entsprechend kann eine `__str__()` Methode definiert werden, die von `str()`
# verwendet wird. Die Funktion `str()` delegiert an `__repr__()`, falls keine
# `__str__()`-Methode definiert ist:
#

# %%
p = Point(2, 5)
print(repr(p))

# %%
print(str(p))


# %%
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"

    def __str__(self):
        return f"a point at {self.x}, {self.y}"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %%
p = Point(2, 5)
print(repr(p))

# %%
print(str(p))


# %% [markdown]
#
# Python bietet viele Dunder-Methoden an: siehe das
# [Python Datenmodell](https://docs.python.org/3/reference/datamodel.html)
# in der Dokumentation.


# %% [markdown]
#
# Durch Definition der Methode `__eq__()` kann das Verhalten von Tests mit `==`
# angepasst werden:

# %%
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %%
p = Point(2, 5)

# %%
print(p)

# %%
p == Point(2, 5)

# %%
p == 123

# %%
123 == p

# %% [markdown]
#
# # Kraftfahrzeuge (Teil 3)
#
# In Teil 2 haben wir die folgende Klasse `Kfz` definiert:
#
# ```python
# >>> class Kfz:
# ...     def __init__(self, hersteller, kennzeichen):
# ...         self.hersteller = hersteller
# ...         self.kennzeichen = kennzeichen
# ...
# ...     def melde_um(self, neues_kennzeichen):
# ...         self.kennzeichen = neues_kennzeichen
# ```
#


# %% [markdown]
#
# Verbessern Sie die Klasse `Kfz` indem Sie
# - Eine `__repr__()` Methode implementieren, die eine geeignete Repräsentation
#   des Fahrzeugs zurückgibt.
# - Eine `__eq__()` Methode implementieren, die die Werte der Attribute zweier
#   Fahrzeuge vergleicht.
#
# Führen Sie die Beispiele mit der verbesserten Klasse aus.


# %%
class Kfz:
    def __init__(self, hersteller, kennzeichen):
        self.hersteller = hersteller
        self.kennzeichen = kennzeichen

    def melde_um(self, neues_kennzeichen):
        self.kennzeichen = neues_kennzeichen

    def __repr__(self):
        return f"Kfz({self.hersteller!r}, {self.kennzeichen!r})"

    def __eq__(self, rhs):
        if isinstance(rhs, Kfz):
            return (
                self.hersteller == rhs.hersteller
                and self.kennzeichen == rhs.kennzeichen
            )
        return False


# %%
bmw = Kfz("BMW", "M-BW 123")
bmw

# %%
bmw2 = Kfz("BMW", "M-BW 123")
bmw2

# %%
assert bmw == bmw2

# %%
vw = Kfz("VW", "WOB-VW 246")
vw

# %%
vw.melde_um("BGL-A 9")
vw

# %%
assert vw.kennzeichen == "BGL-A 9" and vw.hersteller == "VW"

# %%
bmw.melde_um("F-B 21")
bmw

# %%
assert bmw != bmw2

