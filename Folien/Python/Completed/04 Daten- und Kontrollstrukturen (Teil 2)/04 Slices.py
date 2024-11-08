# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Slices</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ## Slices
#
# Mit der Notation `liste[m:n]` kann man eine "Teilliste" von `liste`
# extrahieren.
#
# - Das erste Element ist `liste[m]`
# - Das letzte Element ist `liste[n-1]`

# %% [markdown]
#
# ## Einfache Slices

# %%
string_list = ["a", "b", "c", "d", "e"]

# %%
string_list[1:3]

# %%
string_list[1:1]

# %%
string_list[0 : len(string_list)]

# %%
string_list[0:100]

# %% [markdown]
#
# ## Slices ohne Endwerte

# %%
string_list = ["a", "b", "c", "d", "e"]

# %%
string_list[:3]

# %%
string_list[1:]

# %%
string_list[:]

# %% [markdown]
#
# ## Slices mit Schrittweite $>$ 1

# %%
string_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
string_list[1], string_list[7]

# %%
string_list[1:7:2]

# %%
string_list[1:8:2]

# %%
string_list[1::2]

# %% [markdown]
#
# ## Slices mit negativer Schrittweite

# %%
string_list = ["a", "b", "c", "d", "e"]
string_list[1], string_list[4]

# %%
string_list[4:1:-1]

# %%
string_list[4:0:-1]

# %%
string_list[4:-1:-1]

# %%
string_list[4::-1]

# %%
list(reversed(string_list))

# %% [markdown]
#
# ## Mini-Workshop: Slice
#
# Gegeben sei die folgende Liste:


# %%
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# %% [markdown]
# Extrahieren Sie von `my_list` eine Liste mit allen Elementen außer den ersten beiden.

# %%
my_list[2:]

# %% [markdown]
# Extrahieren Sie von `my_list` eine Liste, die aus dem 2. und 3. Element besteht.

# %%
my_list[1:3]

# %% [markdown]
# Extrahieren Sie von `my_list` eine neue Liste, die alle Elemente außer dem
# ersten und dem letzten enthält.

# %%
my_list[1:-1]


# %% [markdown]
# Extrahieren Sie von `my_list` eine neue Liste, die alle Elemente mit ungeradem
# Index enthält (also die Elemente an Position 1, 3, 5, 7 und 9).

# %%
my_list[1::2]

