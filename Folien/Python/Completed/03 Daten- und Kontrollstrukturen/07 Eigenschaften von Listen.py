# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Eigenschaften von Listen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# # Eigenschaften von Listen
#
# - Listen können beliebige Python-Werte speichern
# - Elemente in einer Liste haben eine feste Reihenfolge
# - Auf Elemente einer Liste kann mit einem Index zugegriffen werden
# - Listen können modifiziert werden
#
# Listen können Elemente mit verschiedenen Typen enthalten, die meisten Listen
# enthalten aber Elemente eines einzigen Typs.

# %% [markdown]
#
# ## Anzahl der Vorkommen eines Elements

# %%
numbers = [1, 1, 2, 1, 3, 2, 1]

# %%
numbers.count(1)

# %%
numbers.count(4)

# %% [markdown]
# ## Finden der Position eines Elements

# %%
my_list = ["a", "b", "c", "d", "b", "d", "b"]

# %%
my_index = my_list.index("b")
my_index

# %%
my_list[my_index]


# %%
# Fehler
# [1, 3, 5].index(2)

# %% [markdown]
# ## Mini-Workshop:
#
# Die Methode `index` wirft eine Exception, wenn das gesuchte Objekt nicht in
# der Liste vorkommt. Schreiben Sie eine Funktion
# ```
# find(element, a_list: list)
# ```
#
# - die einen Index zurückgibt, falls das Element `element` in der Liste
#   vorkommt, und
# - die `None` zurückgibt, falls es nicht vorkommt

# %%
def find(element, a_list: list):
    if element in a_list:
        return a_list.index(element)
    else:
        return None


# %%
my_list = ["a", "b", "c", "d", "e"]

# %%
assert find("a", my_list) == 0

# %%
assert find("d", my_list) == 3

# %%
assert find("x", my_list) is None


# %% [markdown]
# ## Mini-Workshop:
#
# Schreiben Sie eine Funktion
#
# ```
# remove_all(element, a_list: list)
# ```
#
# die alle Vorkommen von `element` aus `a_list` entfernt

# %%
def remove_all(element, a_list: list):
    for i in range(a_list.count(element)):
        a_list.remove(element)


# %%
my_list = ["a", "b", "c", "d", "e", "a", "a", "b"]

# %%
remove_all("a", my_list)
assert my_list == ["b", "c", "d", "e", "b"]

# %%
remove_all("x", my_list)
assert my_list == ["b", "c", "d", "e", "b"]
