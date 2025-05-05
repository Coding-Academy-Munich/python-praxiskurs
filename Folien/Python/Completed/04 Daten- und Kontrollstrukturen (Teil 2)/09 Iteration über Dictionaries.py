# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Iteration über Dictionaries</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Iteration über Schlüssel

# %%
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Pferd"}

# %%
for key in translations:
    print(key)

# %%
for key in translations.keys():
    print(key)

# %% [markdown]
#
# ## Iteration über Werte

# %%
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Pferd"}

# %%
for val in translations.values():
    print(val)

# %% [markdown]
#
# ## Iteration über Key-Value-Paare

# %%
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Pferd"}

# %%
for item in translations.items():
    print(item)

# %%
for key, val in translations.items():
    print(f"Key: {key:<8}Value: {val}")

# %% [markdown]
#
# ## Mini-Workshop: Drucken von Lagerbeständen
#
# Wir schreiben die Software für ein Hochregallager, in dem der Lagerbestand in einem
# Dictionary verwaltet wird.
#
# Die Keys im Dictionary sind die Plätze im Lager, die Werte das am jeweiligen Platz
# gespeicherte Produkt.
#
# Schreiben Sie die folgenden Funktionen:
#
# - `print_inventory(warehouse)`, die alle im Lager vorhandenen Produkte ausdruckt
# - `print_locations(warehouse)`, die alle Plätze im Lager ausdruckt
# - `print_assignments(warehouse)`, die für jedes Produkt ausgibt, in welchem
#    Platz es gespeichert ist.


# %% [markdown]
#
# ```python
# >>> my_warehouse = {(0, 0): "plugs", (1, 0): "cables", (0, 1): "circuit boards"}
# ```
#
# ```python
# >>> print_inventory(my_warehouse)
# plugs
# cables
# circuit boards
# ```
#
# ```python
# >>> print_locations(my_warehouse)
# (0, 0)
# (1, 0)
# (0, 1)
# ```
#
# ```python
# >>> print_assignments(my_warehouse)
# plugs          -> (0, 0)
# cables         -> (1, 0)
# circuit boards -> (0, 1)
# ```


# %%
my_warehouse = {(0, 0): "plugs", (1, 0): "cables", (0, 1): "circuit boards"}


# %%
def print_inventory(warehouse):
    for item in warehouse.values():
        print(item)


# %%
print_inventory(my_warehouse)


# %%
def print_locations(warehouse):
    for location in warehouse:
        print(location)


# %%
print_locations(my_warehouse)


# %%
def print_assignments(warehouse):
    for location, item in warehouse.items():
        print(f"{item:<14} -> {location}")


# %%
print_assignments(my_warehouse)
