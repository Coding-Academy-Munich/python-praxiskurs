# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Funktionen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# # Funktionen
#
# Wir haben eine Firma zum Einzäunen dreieckiger Grundstücke gegründet.
#
# Für jedes von Straßen $A$, $B$ und $C$ begrenze Grundstück berechnen wir:

# %%
länge_a = 10  # Beispielwert
länge_b = 40  # Beispielwert
länge_c = (länge_a**2 + länge_b**2) ** 0.5
länge_gesamt = länge_a + länge_b + länge_c
print(länge_gesamt)


# %% [markdown]
# Können wir das etwas eleganter gestalten?

# %% [markdown]
# ## Satz von Pythagoras
#
# Wir berechnen die Länge von $C$ aus $A$ und $B$ immer nach dem Satz von
# Pythagoras: $C = \sqrt{A^2 + B^2}$.
#
# Das können wir in Python durch eine *Funktion* ausdrücken:

# %%
def pythagoras(a, b):
    c = (a**2 + b**2) ** 0.5
    return c


# %%
pythagoras(3, 4)

# %%
pythagoras(1, 1)

# %% [markdown]
# ## Funktionsdefinition
# - Schlüsselwort `def`
# - Name der Funktion
# - Parameter der Funktion, in Klammern
# - **Doppelpunkt**
# - Rumpf der Funktion, *4 Leerzeichen eingerückt*
# - Im Rumpf können die Parameter wie Variablen verwendet werden
# - Schlüsselwort `return`
#     - Beendet die Funktion
#     - Bestimmt welcher Wert zurückgegeben wird

# %% [markdown]
# ## Funktionsaufruf
#
# - Name der Funktion
# - Argumente des Aufrufs, in Klammern
# - Ein Argument für jeden Parameter

# %%
pythagoras(3, 4)


# %% [markdown]
# ### Mini-Workshop
#
# Schreiben Sie eine Funktion `begrüßung(name)`, die eine Begrüßung in der Form
# "Hallo *name*!" zurückgibt, z.B.
# ```python
# >>> begrüßung("Max")
# 'Hallo Max!'
# >>>
# ```
#
# *Hinweis:* Sie können Strings mit dem `+`-Operator konkatenieren:
# ```python
# >>> name = "Max"
# >>> "Hallo, " + name
# 'Hallo, Max'
# ```

# %%
def begrüßung(name):
    return "Hallo " + name + "!"


# %%
begrüßung("Max")


# %% [markdown]
# ### Mini-Workshop: Funktionen die sich selbst aufrufen
#
# Schreiben Sie eine Funktion `fakultät(n)`, die die Fakultät einer Zahl `n`
# berechnet.
#
# *Hinweis:* Die Fakultät von 0 ist 1, die Fakultät von 1 ist 1, und die Fakultät
# von n ist n mal die Fakultät von n-1.

# %%
def fakultät(n):
    if n == 0:
        return 1
    else:
        return n * fakultät(n - 1)


# %%
assert fakultät(0) == 1
assert fakultät(1) == 1
assert fakultät(2) == 2
assert fakultät(5) == 120
