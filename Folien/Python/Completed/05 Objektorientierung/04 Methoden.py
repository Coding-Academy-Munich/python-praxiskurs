# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Methoden</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ## Methoden
#
# - Klassen können Methoden enthalten.
# - Methoden sind Funktionen, die "zu einem Objekt gehören".
# - In Python gibt es kein implizites `this`.
# - Methoden werden mit der "Dot-Notation" aufgerufen: `my_object.method()`.

# %%
class MyClass:
    def method(self):
        print(f"Called method on {self}")


# %%
my_object = MyClass()
my_object.method()
print(repr(my_object))

# %% [markdown]
#
# Wir können eine Methode zum Verschieben eines Punktes zu unserer `Point`
# Klasse hinzufügen:

# %%
# noinspection PyRedeclaration
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx=0.0, dy=0.0):
        self.x += dx
        self.y += dy


# %%
def print_point(p):
    print(f"Point: x = {p.x}, y = {p.y}")


# %%
p = Point(2, 3)
print_point(p)

# %%
p.move(3, 5)
print_point(p)


# %% [markdown]
#
# ## Workshop: Kraftfahrzeuge (Teil 2)
#
# In Teil 1 haben wir die folgende Klasse `Kfz` definiert:
#
# ```python
# class Kfz:
#     def __init__(self, hersteller, kennzeichen):
#         self.hersteller = hersteller
#         self.kennzeichen = kennzeichen
# ```


# %% [markdown]
#
# Erweitern Sie diese Klasse um eine Methode
#
# `melde_um(self, neues_kennzeichen)`,
#
# die das Kennzeichen des Fahrzeugs ändert.


# %%
class Kfz:
    def __init__(self, hersteller, kennzeichen):
        self.hersteller = hersteller
        self.kennzeichen = kennzeichen

    def melde_um(self, neues_kennzeichen):
        self.kennzeichen = neues_kennzeichen


# %% [markdown]
#
# Mit der folgenden Funktion können wir Fahrzeuge ausdrucken:

# %%
def drucke_kfz(kfz: Kfz):
    print(f"Kfz: {kfz.hersteller} mit Kennzeichen {kfz.kennzeichen!r}")


# %% [markdown]
#
# Wir können dann wieder folgende Instanzen erzeugen:

# %%
bmw = Kfz("BMW", "M-BW 123")
bmw2 = Kfz("BMW", "M-BW 123")
vw = Kfz("VW", "WOB-VW 246")

# %% [markdown]
#
# Melden Sie den oben erzeugten VW um, so dass er das neue Kennzeichen "BGL-A
# 9" hat. Wie können Sie feststellen ob das Ummelden die gewünschte Änderung
# hatte?

# %%
vw.melde_um("BGL-A 9")

# %%
# Z.B
assert vw.kennzeichen == "BGL-A 9" and vw.hersteller == "VW"
# Oder
drucke_kfz(vw)

# %% [markdown]
#
# Melden Sie den in `bmw` gespeicherten BMW um (mit Kennzeichen "F-B 21"). Wirkt
# sich die Änderung auf das in `bmw2` gespeicherte KFZ aus?

# %%
bmw.melde_um("F-B 21")

# %%
drucke_kfz(bmw)
drucke_kfz(bmw2)
