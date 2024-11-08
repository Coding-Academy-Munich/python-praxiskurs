# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Operationen auf Listen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ## Modifikation von Listeneinträgen

# %%
numbers = [2, 4, 6, 8]
numbers

# %%
numbers[1]

# %%
numbers[1] = 10
numbers

# %% [markdown]
#
# ## Test, ob ein Element enthalten ist

# %%
numbers = [5, 6, 7]

# %%
5 in numbers

# %%
3 in numbers

# %%
3 not in numbers

# %% [markdown]
# ## Länge einer Liste

# %%
numbers = [2, 4, 6, 8]
numbers

# %%
len(numbers)

# %% [markdown]
#
# ## Methoden auf Listen
#
# - Viele Operationen auf Listen sind als sog. *Methoden* implementiert.
# - Eine Methode ist sehr ähnlich zu einer Funktion, gehört aber zu einem Objekt.
# - Das "Objekt zu dem die Methode gehört" steht vor dem Methodennamen.
# - Die Syntax ist `object.my_method()`.
# - Die Bedeutung ist ähnlich zu `my_method(object)`.
# - Viele Methoden verändern das Objekt, auf dem sie arbeiten, destruktiv.

# %% [markdown]
#
# ## Einfügen und Löschen von Elementen
#
# - Einfügen und Löschen sind an beliebigen Stellen möglich.
# - Aus Effizienzgründen ist es zweckmäßig Elemente am Ende der Liste
#   einzufügen und zu löschen.

# %%
numbers = [2, 3, 4]
numbers.append(10)
numbers

# %%
numbers = [2, 3, 4]
numbers.extend([10, 20])
numbers

# %% [markdown]
#
# ### Append vs. Extend

# %%
numbers = [2, 3, 4]

# %%
numbers.append([10, 20])
numbers

# %%
numbers = [2, 3, 4]

# %%
numbers.extend([10, 20])
numbers

# %% [markdown]
#
# ### Extend vs. `+`

# %%
numbers = [2, 3, 4]

# %%
numbers.extend([10, 20])

# %%
numbers

# %%
numbers = [2, 3, 4]

# %%
numbers + [50, 60]

# %%
numbers

# %% [markdown]
#
# ### Löschen und Einfügen an beliebigen Positionen

# %%
numbers = [2, 3, 4, 5]
numbers.pop()
numbers

# %%
numbers.insert(1, 10)
numbers

# %%
numbers.pop(1)
numbers

# %%
del numbers[1]
numbers

# %% [markdown]
#
# ## Sortieren von Listen
#
# - Mit der Methode `sort()` können Listen sortiert werden. Dabei wird die Reihenfolge
#   der Elemente in der Liste geändert, auf der die Methode aufgerufen wird.
# - Mit der Funktion `sorted()` kann eine neue Liste erzeugt werden, die die Elemente
#   der ursprünglichen Liste in sortierter Reihenfolge enthält.


# %%
numbers = [3, 8, 6, 1, 9, 2, 5, 4]
numbers

# %%
numbers.sort()

# %%
numbers

# %%
numbers = [3, 8, 6, 1, 9, 2, 5, 4]
numbers

# %%
sorted(numbers)

# %%
numbers

# %% [markdown]
#
# ## Mini-Workshop: Farben (Teil 2)
#
# Gegeben seien die folgenden Listen:

# %%
grundfarben = ["Rot", "Grün", "Blau"]
mischfarben = ["Cyan", "Gelb"]
farben = grundfarben + mischfarben

# %% [markdown]
#
# - Überprüfen Sie, ob Gelb eine Grundfarbe ist, ob also der String `"Gelb"`
#   in `grundfarben` enthalten ist.
# - Ist Grün eine Grundfarbe?

# %%
"Gelb" in grundfarben

# %%
"Grün" in grundfarben

# %% [markdown]
#
# - Wie viele Elemente hat die Liste `grundfarben`?
# - Wie viele Elemente hat die Liste `mischfarben`?

# %%
len(grundfarben)

# %%
len(mischfarben)

# %% [markdown]
#
# Wir haben vergessen Magenta in die Mischfarben einzufügen.
#
# - Überprüfen Sie, dass der String `"Magenta"` nicht in `mischfarben` enthalten ist.
# - Fügen Sie `Magenta` zu den Mischfarben hinzu.
# - Überprüfen Sie, dass der String `"Magenta"` jetzt in `mischfarben` enthalten ist.
# - Wie lange ist die Liste `mischfarben` jetzt?

# %%
"Magenta" in mischfarben

# %%
mischfarben.append("Magenta")

# %%
"Magenta" in mischfarben

# %%
len(mischfarben)


# %% [markdown]
# - Ändern Sie das erste Element von `farben` in `Dunkelrot`
# - Was ist jetzt das erste Element von `grundfarben`?

# %%
farben[0] = "Dunkelrot"
farben

# %%
grundfarben[0]

# %% [markdown]
# Was ist das dritte Element der Liste `farben`?

# %%
farben[2]

# %% [markdown]
# Fügen Sie `Lila` als zweites Element in die Liste `farben` ein.

# %%
farben.insert(1, "Lila")

# %% [markdown]
# Was ist jetzt das dritte Element der Liste `farben`?

# %%
farben[2]

# %% [markdown]
# Löschen Sie das zweite Element der Liste `farben`

# %%
farben.pop(1)
farben

# %% [markdown]
#
# Sortieren Sie die Liste `farben`.

# %%
farben.sort()
farben

# %% [markdown]
# Was ist jetzt das erste Element der Liste `farben`?

# %%
farben[0]

