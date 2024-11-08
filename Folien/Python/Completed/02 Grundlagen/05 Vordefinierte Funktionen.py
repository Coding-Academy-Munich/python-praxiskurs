# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Vordefinierte Funktionen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ### Vordefinierte Funktionen
#
# Einige Funktionen in Python sind vom Interpreter
# [vordefiniert](https://docs.python.org/3/library/functions.html#built-in-functions).
# Viele weitere können durch Module geladen werden.

# %%
print("Hello, world!")

# %% [markdown]
#
# ## Umwandlung von Datentypen
#
# - Python nimmt keine automatischen Umwandlungen von Datentypen vor.
# - Man kann aber die Konversion oft explizit durchführen.

# %%
type(123)

# %%
int("123")

# %%
int(3.8)

# %% [markdown]
#
# Praktisch jedes Objekt in Python lässt sich in einen String umwandeln:

# %%
str(1.2)

# %% [markdown]
#
# Aber natürlich gibt es Fälle, in denen Python die Konversion in den gewünschten Typ
# nicht durchführen kann:

# %%
# int("Hello, there!")

# %% [markdown]
#
# ## Andere Eingebaute Funktionen

# %%
abs(10)

# %%
abs(-10)

# %%
round(4.4)

# %%
round(4.6)

# %%
print(round(0.5), round(1.5), round(2.5), round(3.5))

# %% [markdown]
#
# ## Mini-Workshop: Vordefinierte Funktionen
#
# In diesem Workshop sollen Sie einige Aufgaben mit vordefinierten Funktionen lösen.
# Manche der Funktionen wurden noch nicht besprochen. Verwenden Sie die [Tabelle der
# vordefinierten
# Funktionen](https://docs.python.org/3/library/functions.html#built-in-functions)
# um geeignete Kandidaten zu finden.

# %% [markdown]
#
# Wandeln Sie die Zahl `1.5` in einen String um.

# %%
str(1.5)

# %% [markdown]
#
# Bestimmen Sie das Maximum der Zahlen 2.5 und 1.7 mit einer eingebauten Funktion.

# %%
max(2.5, 1.7)

# %% [markdown]
#
# Wandeln Sie den String "1.234" in eine Gleitkommazahl um und addieren Sie `2.345`
# dazu.

# %%
float("1.234") + 2.345

