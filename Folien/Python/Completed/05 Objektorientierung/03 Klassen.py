# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Klassen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# # Benutzerdefinierte Datentypen
#
# Wir wollen uns jetzt der Definition von benutzerdefinierten Datentypen (Klassen)
# zuwenden:


# %%
class PointV0:
    pass


# %% [markdown]
#
# Klassennamen werden in Pascal-Case (d.h. groß und mit Großbuchstaben zur
# Trennung von Namensbestandteilen) geschrieben, z.B. `MyVerySpecialClass`.

# %% [markdown]
#
# Wir verwenden im Folgenden [Python Tutor](https://tinyurl.com/python-classe-point-v0)
# um die Klasse `Point` zu implementieren.

# %% [markdown]
#
# Instanzen von benutzerdefinierten Klassen werden erzeugt, indem man den
# Klassennamen als Funktion aufruft. Manche der Python Operatoren und
# Funktionen können verwendet werden ohne, dass zusätzliche Implementierungsarbeit
# nötig ist:

# %%
p1 = PointV0()
p1

# %%
print(p1)

# %%
p2 = PointV0()
p1 == p2

# %%
# Fehler
# p1 < p2

# %% [markdown]
#
# Ähnlich wie Dictionaries neue Einträge zugewiesen werden können, kann man
# benutzerdefinierten Datentypen neue *Attribute* zuweisen, allerdings verwendet
# man die `.`-Notation statt der Indexing Notation `[]`:

# %%
# Möglich, aber nicht gut... / Possible but not good...
p1.x = 1.0
p1.y = 2.0
print(p1.x)
print(p1.y)


# %%
# Error!
# p2.x

# %% [markdown]
#
# Im Gegensatz zu Dictionaries werden Instanzen von Klassen typischerweise
# *nicht* nach der Erzeugung beliebige Attribute zugewiesen!
#
# Statt dessen sollen allen Instanzen die gleiche Form haben. Deswegen werden
# die Attribute eines Objekts bei seiner Konstruktion initialisiert. Das geht
# über die `__init__()` Methode.
#
# Die `__init__()`-Methode hat immer
# (mindestens) einen Parameter, der per Konvention `self` heißt:

# %%
class PointV1:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0


# %%
def print_point(name, p):
    print(f"{name}: x = {p.x}, y = {p.y}")


# %%
p1 = PointV1()
p2 = PointV1()
print_point("p1", p1)
print_point("p2", p2)

# %%
p1 == p2

# %% [markdown]
#
# Die Werte von Attributen können verändert werden:

# %%
p1.x = 1.0
p1.y = 2.0
print_point("p1", p1)
print_point("p2", p2)


# %% [markdown]
#
# In vielen Fällen wäre es besser, bei der Konstruktion eines Objekts Werte für
# die Attribute anzugeben. Das ist möglich, indem man der `__init__()`-Methode
# zusätzliche Parameter gibt.

# %%
class PointV2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# %%
p1 = PointV2(2.0, 3.0)
p2 = PointV2(0.0, 0.0)
print_point("p1", p1)
print_point("p2", p2)


# %% [markdown]
#
# # Kraftfahrzeuge (Teil 1)
#
# Definieren Sie eine Klasse `Kfz`, deren Instanzen Kraftfahrzeuge beschreiben.
# Jedes KFZ soll Attribute `hersteller` und `kennzeichen` haben.


# %%
class Kfz:
    def __init__(self, hersteller, kennzeichen):
        self.hersteller = hersteller
        self.kennzeichen = kennzeichen


# %% [markdown]
#
# Erzeugen Sie zwei Kraftfahrzeuge:
# - einen BMW mit Kennzeichen "M-BW 123"
# - einen VW mit Kennzeichen "WOB-VW 246"
# und speichern Sie sie in Variablen `bmw` und `vw`

# %%
bmw = Kfz("BMW", "M-BW 123")
vw = Kfz("VW", "WOB-VW 246")

# %% [markdown]
#
# Erzeugen Sie eine neue Instanz von `Kfz` mit Hersteller BMW und Kennzeichen
# "M-BW 123" und speichern Sie sie in einer Variablen `bmw2`.

# %%
bmw2 = Kfz("BMW", "M-BW 123")

# %% [markdown]
#
# Wie können Sie feststellen, ob `bmw` und `bmw2` (bzw. `bmw` und `vw`) das
# gleiche Fahrzeug beschreiben?

# %%
bmw.hersteller == bmw2.hersteller and bmw.kennzeichen == bmw2.kennzeichen

# %%
bmw.hersteller == vw.hersteller and bmw.kennzeichen == vw.kennzeichen
