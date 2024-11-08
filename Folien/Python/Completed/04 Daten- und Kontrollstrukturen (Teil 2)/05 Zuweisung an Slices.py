# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Zuweisung an Slices</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ## Zuweisung an Slices
#
# Man kann Werte an Slices zuweisen:

# %%
liste = [1, 2, 3, 4]
liste[1:3]

# %%
liste[1:3] = ["a", "b", "c"]
liste

# %%
liste[2:2]

# %%
liste[2:2] = ["x"]
liste

# %%
liste[:] = [11, 22, 33]
liste

# %% [markdown]
#
# ## Mini-Workshop: Ändern von Prioritäten
#
# Gegeben die folgende Liste von Prioritäten:

# %%
prioritäten = ["sehr niedrig", "geht so", "extrem hoch"]

# %% [markdown]
#
# Ändern Sie die Liste `prioritäten` durch eine Zuweisung an ein Slice in die folgende
# Liste:
# ```python
# ['sehr niedrig', 'niedrig', 'mittel', 'hoch', 'extrem hoch']
# ```

# %%
prioritäten

# %%
prioritäten[1:2]

# %%
prioritäten[1:2] = ["niedrig", "mittel", "hoch"]

# %% [markdown]
#
# Verwenden Sie Zuweisung an ein Slice um den Inhalt von `prioritäten` durch
# die Zahlen `5, 4, 3, 2, 1` zu ersetzen.
#
# *Hinweis:* Verwenden Sie dazu eine Range.

# %%
prioritäten[:] = range(5, 0, -1)
prioritäten
