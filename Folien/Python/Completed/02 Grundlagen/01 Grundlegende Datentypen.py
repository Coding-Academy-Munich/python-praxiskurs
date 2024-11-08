# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Grundlegende Datentypen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# # Woraus besteht ein Programm?
#
# Wir wollen ein Programm schreiben, das
#
# ```
# Hello, world!
# ```
#
# auf dem Bildschirm ausgibt.
#
# Was benötigen wir dazu?

# %% [markdown]
# Was benötigen wir dazu?
#
# - Daten
#     - den Text `Hello, world!`
# - Anweisungen
#     - *Gib den folgenden Text auf dem Bildschirm aus*
# - Kommentare
#     - Hinweise für den Programmierer, werden von Python ignoriert

# %% [markdown]
# ## Kommentare
#
# - `#` gefolgt von beliebigem Text
# - bis zum Ende der Zeile

# %%
# Das ist ein Kommentar.
# Alle Zeilen in dieser Zelle werden
# von Python ignoriert.


# %% [markdown]
# ## Daten
#
# - Zahlen: `123`, `3.141592`
# - Text (Strings): `'Das ist ein Text'`, `"Hello, world!"`

# %%
123

# %%
1 + 2

# %%
3.141592

# %%
2.1 + 3.8

# %%
# fmt: off
3,141592

# %%
2,1 + 3,8
# fmt: on


# %%
"Hello, world!"

# %%
# fmt: off
'Das ist ein Text'
# fmt: on

# %%
"1"

# %%
"1" + "2"

# %%
"""Ein Text,
der über mehrere Zeilen geht."""

# %%
"Benachbarte " "Stringliterale " "werden zusammengefügt"

# %% [markdown]
#
# ## Anzeige von Werten mit der `print()` Funktion
#
# Um Werte anzuzeigen kann man die `print()`-Funktion verwenden:
#
# `print(...)` gibt den in Klammern eingeschlossenen Text auf dem Bildschirm
# aus.

# %%
print(123)

# %%
print("Hello, world!")

# %% [markdown]
#
# Der `print()` Funktion können mehrere Argumente übergeben werden.
# - Die Argumente werden durch Kommata getrennt
# - Alle Argumente werden in einer Zeile ausgegeben, mit Leerzeichen zwischen
#   den Argumenten.

# %%
print("Der Wert von 1 + 1 ist", 1 + 1, ".")

# %% [markdown]
#
# Durch Angabe eines *benannten Arguments* `sep=''` kann die Ausgabe der
# Leerzeichen unterdrückt werden:

# %%
print("Der Wert von 1 + 1 ist", 1 + 1, ".", sep="")

# %% [markdown]
#
# Es sind auch beliebige andere Strings als Wert des Arguments `sep` zulässig:

# %%
# CSV (don't do this!)
print(1, 3, 7.5, 2, sep=",")

# %%
# Uh, oh
print(1, 3, 7.5, 2, "who, me?", sep=",")

# %% [markdown]
#
# Mit dem Argument `end` kann man bestimmen, welcher String am Zeilenende
# ausgegeben wird:

# %%
print("a", end=", ")
print("b", end=", ")
print("c")

# %% [markdown]
#
# ## Mini-Workshop: Grundlegende Datentypen

# %% [markdown]
# Wie können Sie den String `Hello, world!` in Python darstellen?

# %%
"Hello, world!"

# %% [markdown]
# Wie können Sie den String `Hello, World!` auf dem Bildschirm ausgeben?

# %%
print("Hello, World!")

# %% [markdown]
# Wie können Sie Ihren Namen als Text (String) in Python darstellen?

# %%
"Matthias"

# %% [markdown]
#
# Wie können Sie die Zahl 123 in Python darstellen?

# %%
123

# %% [markdown]
# Wie können Sie Ihren Namen auf dem Bildschirm ausgeben?

# %%
print("Matthias")

# %% [markdown]
# Wie können Sie die Zahl 123 auf dem Bildschirm ausgeben?

# %%
print("Matthias")

# %% [markdown]
# Wie können Sie
#
# ```
# 130 g   Mehl
# 250 ml  Milch
# 1 EL    Vanillezucker
# 1 Prise Salz
# ```
#
# auf dem Bildschirm ausgeben?

# %%
print("130 g   Mehl")
print("250 ml  Milch")
print("1 EL    Vanillezucker")
print("1 Prise Salz")

# %%
# Alternativ:
# fmt: off
print("130 g   Mehl", "250 ml  Milch", "1 EL    Vanillezucker", "1 Prise Salz",
      sep="\n")
# fmt: on

# %%
# Alternativ:
print(
    """130 g   Mehl
250 ml  Milch
1 EL    Vanillezucker
1 Prise Salz"""
)

# %%
# Alternativ:
# fmt: off
print("130 g   Mehl\n"
      "250 ml  Milch\n"
      "1 EL    Vanillezucker\n"
      "1 Prise Salz")  # fmt: on

