# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Typannotationen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Typannotationen
# - Python ist dynamisch typisiert
# - Typen von
#
#   - Variablen
#   - Funktionsparametern
#   - Rückgabewerten von Funktionen
#   - Attributen von Objekten
#   - etc.
#
#   *müssen* nicht angegeben werden
# - Python *erlaubt* es aber diese Typen anzugeben:

# %%
def repeat_string(string: str, count: int) -> str:
    return string * count


# %%
# repeat_string?

# %%
repeat_string("abc", 3)

# %% [markdown]
#
# Typannotationen werden vom Python Interpreter ignoriert:

# %%
repeat_string(3, 4.0)

# %% [markdown]
#
# ## Vorteile von Typannotationen
#
# - Dokumentation
# - Typprüfung durch externe Tools
# - Verbesserte Code-Vervollständigung in IDEs


# %% [markdown]
#
# ## Mini-Workshop: Typannotationen
#
# Schreiben Sie eine Function `repeat(s: str, n: int) -> str`, die den String `s`
# `n` mal wiederholt:
#
# ```python
# >>> repeat("abc", 3)
# "abcabcabc"
# ```
#
# *Hinweis:* Sie können dazu den Multiplikationsoperator `*` verwenden:
# ```python
# >>> "abc" * 3
# "abcabcabc"
# ```


# %%
def repeat(s: str, n: int) -> str:
    return s * n


# %%
repeat("abc", 3)


# %% [markdown]
#
# Falls Sie VS Code oder PyCharm Professional verwenden:
#
# - Welche Warnungen erhalten Sie in den folgenden Beispielen?
# - Signalisieren diese Warnungen einen Laufzeitfehler?
#
# Falls Sie mit Jupyter Notebooks im Browser arbeiten empfiehlt es sich, den
# Code dieser Aufgabe in eine Python Datei zu kopieren und diese mit Ihrem IDE
# zu öffnen um zu sehen, welche Warnungen angezeigt werden.

# %% [markdown]
#
# - Was passiert, wenn Sie `repeat()` mit zwei Zahlen aufrufen?
# - Was passiert, wenn Sie `repeat()` mit zwei Strings aufrufen?

# %%
repeat(3, 4)

# %%
# repeat("abc", "def")
