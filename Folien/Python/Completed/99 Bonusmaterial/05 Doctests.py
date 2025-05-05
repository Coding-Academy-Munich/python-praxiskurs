# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Doctests</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Doctests
#
# - Tests, die in Docstrings integriert sind
# - Können mit dem `doctest`-Modul (oder mit `pytest`) ausgeführt werden
# - Code-Zeilen werden mit dem Präfix `>>>` versehen
# - Die Ausgabe, die der Python-Interpreter dafür anzeigen würde, wird in den folgenden
#   Zeilen ohne Präfix angegeben:

# %%
def add(x, y):  # type: ignore
    """Adds two numbers or concatenates two sequences.

    >>> add(2, 3)
    5
    """
    return x + y


# %% [markdown]
#
# Um Doctests in einem Notebook auszuführen kann man folgende Anweisungen
# verwenden:

# %%
import doctest

# %%
doctest.testmod()


# %% [markdown]
#
# In der Kommandozeile können Doctests mit
#
# ```shell
# $ python -m doctest my_module.py
# ```
# oder
# ```shell
# $ pytest --doctest-modules my_module.py
# ```
#
# ausgeführt werden.

# %%
def add(x, y):  # type: ignore
    """Adds two numbers or concatenates two sequences.

    >>> add(2, 3)
    5
    >>> add([1], [2])
    [1, 2]
    >>> add(1, "a")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return x + y


# %%
doctest.testmod()

# %%
# add(1, "a")

# %% [markdown]
#
# ## Welche Tests eignen sich für Doctests?
#
# - Test einer einzelnen Funktion/Methode
# - Wenig Kontext notwendig
# - **Helfen dem Leser, die Funktion zu verstehen**

# %% [markdown]
#
# ## Mini-Workshop: Doctests
#
# Schreiben Sie Doctests für die `negate()` und `my_abs()` Funktionen in
# `examples/SimplePytestStarterKit`.
#
# Falls Sie mit Jupyter Lite arbeiten, können sie das Notebook
# `examples/SimplePytestStarterKit/src/Simple Doctest.ipynb` verwenden,
# um die Doctests auszuführen.
