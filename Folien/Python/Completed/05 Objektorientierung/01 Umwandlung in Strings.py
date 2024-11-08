# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Umwandlung in Strings</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# # Umwandlung in Strings
#
# Python bietet zwei Funktionen an, mit denen beliebige Werte in Strings umgewandelt
# werden können:
#
# - `repr` für eine "programmnahe" Darstellung (wie könnte der Wert im Programm
#   erzeugt werden)
# - `str` für eine "benutzerfreundliche" Darstellung

# %%
text = "Hallo\nWelt!"

# %%
print(str(text))

# %%
print(repr(text))

# %% [markdown]
# Für manche Datentypen liefern `str` und `repr` den gleichen String zurück:

# %%
my_list = ["a", "b", "c"]

# %%
print(str(my_list))

# %%
print(repr(my_list))

# %% [markdown]
#
# Die `print()`-Funktion wendet `str()` auf ihre Argumente an:

# %%
text = "My\nstring"

# %%
print(repr(text))

# %%
print(str(text))

# %%
print(text)

# %% [markdown]
#
# In F-Strings werden Werte mit `str()` in Strings umgewandelt. Mit dem Postfix
# `!r` kann statt dessen `repr()` verwendet werden.


# %%
text = "Hi,\nthere!"

# %%
print(f"{text}")

# %%
print(f"{text!s}")

# %%
print(f"{text!r}")

# %% [markdown]
#
# ## Mini-Workshop: Umwandlung in Strings
#
# Welche Funktion wurde verwendet, um die folgenden Ausgaben zu erzielen?

# %% [markdown]
# ```python
# >>> my_string = "Hello, world!"
# >>> print(???(my_string))
# Hello, world!
# ```

# %%
my_string = "Hello, world!"

# %%
print(str(my_string))

# %% [markdown]
# ```python
# >>> print(???(my_string))
# 'Hello, world!'
# ```

# %%
print(repr(my_string))
