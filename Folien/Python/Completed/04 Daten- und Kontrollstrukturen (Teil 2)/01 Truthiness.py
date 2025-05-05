# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Truthiness</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Truthiness
#
# Die `if`-Anweisung kann als Argument beliebige Python-Werte bekommen,
# nicht nur Boolesche Werte.
#
# Folgende Werte gelten als *falsch*
#
# - `None` und `False`
# - `0` und `0.0` (und Null-Werte von anderen Zahlentypen)
# - Leere Strings, Listen und andere Collections: `""`, `[]`, ...
# - Manche Werte von benutzerdefinierten Datentypen
#
#  Alle anderen Werte gelten als wahr.

# %%
def check(value):
    if value:
        print(f"{value!r} is truthy.")
    else:
        print(f"{value!r} is falsy.")


# %%
check(True)

# %%
check(False)

# %%
check(None)

# %%
check(0)

# %%
check(1)

# %%
check("")

# %%
check("123")

# %%
check([])

# %%
check([1, 2, 3])


# %% [markdown]
#
# Wie wird das verwendet?

# %%
def print_elements(collection):
    if collection:
        for elt in collection:
            print(elt)
    else:
        print(f"{collection} has no elements!")


# %%
print_elements([1, 2, 3])

# %%
print_elements([])


# %% [markdown]
#
# ## Mini-Workshop: Truthiness
#
# Für welche Werte von `x` ist `len(x) - 1` falsy?


# %% [markdown]
# *Antwort:* 
# Für Listen oder Strings der Länge 1.

# %% [markdown]
#
# Geben Sie zwei Beispielwerte mit verschiedenem Typ an.

# %%
assert not (len([1]) - 1)

# %%
assert not (len("x") - 1)


# %% [markdown]
#
# Gibt es einen String `s`, für den `s[0]` falsy ist?

# %% [markdown]
# *Antwort:* 
# Nein. Das Ergebnis ist immer ein String der Länge 1 und damit truthy.
