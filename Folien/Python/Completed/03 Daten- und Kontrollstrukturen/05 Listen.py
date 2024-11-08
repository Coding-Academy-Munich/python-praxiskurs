# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Listen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Listen
#
# - Wir können mittlerweile Programme schreiben, die viele Arten von
#   Berechnungen ausführen, aber wir haben noch keine Möglichkeit, mehrere
#   Objekte zusammenzufassen.
# - Wenn wir beispielsweise eine Einkaufsliste erstellen wollen, müssen wir
#   uns im Moment mit folgender Lösung behelfen:

# %%
produkt_1 = "Haferflocken"
produkt_2 = "Kaffeebohnen"
produkt_3 = "Orangenmarmelade"

# %% [markdown]
#
# Diese Vorgehensweise hat viele Probleme:
#
# - Wir müssen genau wissen, wie viele Produkte wir kaufen wollen
# - Es gibt keine Möglichkeit Operationen auf allen Produkten auszuführen,
#   z.B. alle Produkte auszudrucken
# - Python weiß nicht, dass die Produkte zusammengehören
# - ...

# %% [markdown]
#
# ## Die Lösung: Listen

# %%
einkaufsliste = ["Haferflocken", "Kaffeebohnen", "Orangenmarmelade"]

# %% [markdown]
# Der Typ von Listen ist `list`.

# %%
type(einkaufsliste)

# %% [markdown]
# ## Erzeugen von Listen
#
# - Listen werden erzeugt, indem man ihre Elemente in eckige Klammern
#   einschließt.
# - Die Elemente einer Liste können beliebige Python-Werte sein.
# - Eine Liste kann Elemente mit verschiedenen Typen enthalten.

# %%
list_1 = [1, 2, 3, 4, 5]

# %%
list_1

# %%
list_2 = ["string1", "another string"]

# %%
list_2

# %%
list_3 = []

# %%
list_3

# %%
list_4 = [1, 0.4, "ein String", True, None]

# %%
list_4

# %% [markdown]
#
# Die Elemente einer Liste müssen keine Literale sein, man kann auch Werte von
# Variablen in einer Liste speichern:

# %%
produkt_1 = "Haferflocken"
produkt_2 = "Kaffeebohnen"
produkt_3 = "Orangenmarmelade"

# %%
einkaufsliste = [produkt_1, produkt_2, produkt_3, "Erdbeermarmelade"]
einkaufsliste

# %% [markdown]
#
# Nachdem eine Liste erzeugt ist hat sie keine Verbindung zu den Variablen, die
# in ihrer Konstruktion verwendet wurden:

# %%
produkt_1 = "Dinkelflocken"
produkt_2 = "Teebeutel"
einkaufsliste

# %% [markdown]
# ## Zugriff auf Listenelemente

# %%
numbers = [2, 4, 6, 8]

# %%
numbers[0]

# %%
numbers[3]

# %%
numbers[-1]

# %% [markdown]
#
# ## Andere Möglichkeiten, Listen zu erzeugen
#
# Mit dem Additionsoperator `+` können Listen konkateniert werden:

# %%
[1, 2, 3] + [4, 5, 6]

# %% [markdown]
#
# Durch den Multiplikationsoperator `*` können die Elemente einer Liste
# wiederholt werden:

# %%
[1, 2] * 3

# %%
3 * ["a", "b"]

# %%
[0] * 10

# %% [markdown]
# Mit der Funktion `list()` können manche andere Datentypen in Listen umgewandelt
# werden.
#
# Im Moment kennen wir nur Listen und Strings als mögliche Argumenttypen:

# %%
list("abc")

# %%
list([1, 2, 3])


# %% [markdown]
#
# ## Mini-Workshop: Farben (Teil 1)
#
# - Definieren Sie eine Variable `grundfarben`, die eine Liste mit den Strings
#   `"Rot"`, `"Grün"` und `"Blau"` enthält.
# - Definieren Sie eine Variable `mischfarben`, die eine Liste mit den Strings
#   `"Cyan"`, `"Gelb"` und `"Magenta"` enthält.

# %%
grundfarben = ["Rot", "Grün", "Blau"]

# %%
mischfarben = ["Cyan", "Gelb", "Magenta"]


# %% [markdown]
#
# Erzeugen Sie eine Liste `farben`, die die Elemente von `grundfarben` gefolgt von
# den Elementen von `mischfarben` enthält.

# %%
farben = grundfarben + mischfarben
farben


# %% [markdown]
#
# Erzeugen Sie eine Liste, die 15-mal die Zahl `1` enthält.

# %%
[1] * 15


# %% [markdown]
#
# Erzeugen Sie die Liste `["r", "g", "b"]` aus dem String `"rgb"`.

# %%
list("rgb")

