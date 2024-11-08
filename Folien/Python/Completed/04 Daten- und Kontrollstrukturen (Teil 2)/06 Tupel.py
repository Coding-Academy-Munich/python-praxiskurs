# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Tupel</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ## Tupel
#
# Tupel sind ähnlich zu Listen, allerdings sind Tupel nach ihrer Konstruktion
# unveränderlich. Funktionen und Methoden für Listen, die die Liste nicht
# destruktiv modifizieren sind in der Regel auch auf Tupel anwendbar.

# %% [markdown]
#
# ## Tupel-Literale
#
# - Elemente durch Kommata getrennt: `1, 2, 3, 4`
# - In vielen Fällen müssen Tupel eingeklammert werden: `(1, 2, 3)`

# %%
my_tuple = 1, 2, 3
my_tuple

# %%
type(my_tuple)

# %%
my_tuple = (1, 2, 3)
my_tuple

# %%
type(my_tuple)

# %% [markdown]
#
# ### Leeres Tupel

# %%
empty_tuple = ()
empty_tuple

# %%
type(empty_tuple)

# %% [markdown]
#
# ### Singleton-Tupel

# %%
# fmt: off
non_tuple = (1)
non_tuple
# fmt: on

# %%
type(non_tuple)

# %%
singleton_tuple = (1,)
singleton_tuple

# %%
type(singleton_tuple)

# %% [markdown]
#
# ### Heterogenes Tupel

# %%
mixed_tuple = ("a", 1, True)

# %%
type(mixed_tuple)

# %% [markdown]
#
# ## Operationen auf Tupeln
#
# - Viele der Operationen auf Listen lassen sich auf Tupel anwenden.
# - Die Operationen, die Listen verändern sind nicht anwendbar.

# %% [markdown]
#
# ### Konstruktion von Tupeln

# %%
values = (1, 2, 3)
values

# %%
tuple([1, 2, 3, 4])

# %% [markdown]
#
# ### Konkatenation von Tupeln

# %%
values = (1, 2, 3)

# %%
values + ("a", "b")

# %%
values

# %%
values * 3

# %%
values

# %% [markdown]
#
# ### Tupel und Indizes

# %%
values = (1, 2, 3)

# %%
values[1]

# %%
values.index(2)

# %% [markdown]
#
# ### Funktionen und Methoden

# %%
values = (1, 2, 3, 1, 2, 1, 2)

# %%
len(values)

# %%
values.count(1)

# %% [markdown]
#
# ### Schleifen über Tupel

# %%
for x in 1, 2, 3:
    print(x)

# %% [markdown]
#
# ### Illegale Operationen

# %%
values = (1, 2, 3)

# %%
# values[1] = 10

# %%
# values.append(4)


# %% [markdown]
# ### Mini-Workshop: Funktionen mit mehreren Rückgabewerten
#
# Schreiben Sie eine Funktion `min_max(numbers)`, die das Minimum und das
# Maximum aus einer Liste von Zahlen zurückgibt.
# ```python
# >>> min_max([5, 3, 1, 7, 2])
# (1, 7)
# ```


# %%
def min_max(numbers):
    min_number = min(numbers)
    max_number = max(numbers)
    return min_number, max_number


# %%
assert min_max([5, 3, 1, 7, 2]) == (1, 7)


# %% [markdown]
#
# ## Mini-Workshop: Zufällige Tupel
#
# Die folgenden Anweisungen erzeugen ein Tupel von Zufallszahlen mit
# zufälliger Länge:


# %%
import random

# %%
random.seed(2022)
my_tuple = random.choices(range(1000), k=random.randint(5_000, 15_000))

# %% [markdown]
#
# Wie viele Elemente enthält `my_tuple`?

# %%
len(my_tuple)

# %% [markdown]
#
# Kommt die Zahl 1 in `my_tuple` vor?
# Falls ja, bei welchem Index ist ihr erstes Vorkommen?

# %%
1 in my_tuple

# %%
my_tuple.index(1)

# %% [markdown]
#
# Drucken Sie eine Tabelle, die angibt, wie oft jede der Zahlen 0 bis 9
# in `my_tuple` vorkommt.

# %%
for i in range(10):
    print(f"{i}: {my_tuple.count(i)}")


# %%
