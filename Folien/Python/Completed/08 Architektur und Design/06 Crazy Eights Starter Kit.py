# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Crazy Eights Starter Kit</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# - Die Implementierung in Notebooks wird unübersichtlich
# - Wir wechseln in eine IDE
# - Ich verwende PyCharm, aber jede andere IDE ist auch möglich

# %% [markdown]
#
# - Drei Projekte für Crazy Eights:
#   - `CrazyEightsSk`: Starter Kit
#   - `CrazyEightsSimple`: Einfache Implementierung
#   - `CrazyEights`: Vollständige Implementierung

# %% [markdown]
#
# ## Aufbau der Projekte
#
# - `src`: Quellcode
#   - `src/crazyeights{_sk,_simple}`: Package für die Implementierung
# - `tests`: Tests
# - `pyproject.toml`: Festlegen des Build-Systems (setuptools)
# - `setup.cfg`: Konfiguration des Build-Systems
# - `pytest.ini`: Konfiguration für `pytest`
# - `tox.ini`: Automatisierung der Tests für verschiedene Python-Versionen
# - `.bumpversion.cfg`: Inkrementieren der Versionsnummer mit `bumpversion`
# - `.gitignore`: Dateien, die nicht in Git aufgenommen werden sollen

# %% [markdown]
#
# ### Erstellen eines installierbaren Wheels
#
# ```bash
# $ cd CrazyEightsSimple
# $ python -m build
# ```
#
# Das Wheel wird in `dist` abgelegt:
#
# ```bash
# $ ls dist
# crazyeights_simple-0.0.1-py3-none-any.whl
# ```

# %% [markdown]
#
# ### Installation des Wheels
#
# ```bash
# $ cd CrazyEightsSimple
# $ python -m pip install dist/crazyeights_simple-0.0.1-py3-none-any.whl
# ```
#
# Das Package ist jetzt installiert:
#
# ```bash
# $ python -m pip list | grep crazy  # Linux/Mac
# crazyeights-simple 0.0.1
# ```
#
# ```powershell
# > python -m pip list | Select-String crazy  # Windows PowerShell
# crazyeights-simple 0.0.1
# C:\Users\tc\Python\crazyeights-simple
# ```

# %% [markdown]
#
# ### Verwenden des installierten Pakets (1)
#
# Das Wheel enthält ein ausführbares Skript, das das Package verwendet:
#
# ```bash
# $ crazyeights-simple
# Crazy Eights with 2 players:
#   Computer 1 (A♠, 3♥, 3♦, T♣, 8♠, 8♥, 2♠)
#   Computer 2 (5♥, 8♣, 2♦, K♠, Q♠, J♥, 8♦)
# ```
#
# ```bash
# $ crazy-eights-simple --help
# Usage: crazy-eights-simple [OPTIONS]
# ...
# ```

# %% [markdown]
#
# ### Verwenden des installierten Pakets (2)
#
# ```python
# >>> from crazyeights_simple import Card, Deck, Player
# >>> deck = Deck()
# >>> player = Player("Alice")
# >>> player.draw_n_cards(deck, 7)
# >>> player
# Player('Alice')
# >>> player.hand[0]
# Card('♥', '5')
# ```


# %% [markdown]
#
# ### Ausführen der Tests mit Pytest
#
# ```bash
# $ cd CrazyEightsSimple
# $ python -m pytest
# ```
#
# oder
#
# ```bash
# $ cd CrazyEightsSimple
# $ pytest
# ```

# %% [markdown]
#
# ### Ausführen der Tests mit Tox
#
# ```bash
# $ cd CrazyEightsSimple
# $ python -m tox
# ```
#
# oder
#
# ```bash
# $ cd CrazyEightsSimple
# $ tox
# ```

# %% [markdown]
#
# ### Inkrementieren der Versionsnummer
#
# ```bash
# $ cd CrazyEightsSimple
# $ crazyeights-simple --version
# crazyeights-simple, version 0.0.1
# $ python -m bumpversion patch
# $ crazyeights-simple --version
# crazyeights-simple, version 0.0.2
# ```

# %% [markdown]
#
# ### Verwenden des Pakets in PyCharm
#
# - Markieren Sie das Verzeichnis `CrazyEightsSimple/src` als Source Root
# - Markieren Sie das Verzeichnis `CrazyEightsSimple/tests` als Test Root

# %% [markdown]
#
# ### Erstellen der Package-Struktur für eigene Projekte
#
# ```bash
# $ cookiecutter https://github.com/hoelzl/trivial_python_project
# ```
#
# Die Template stellt einige Fragen zum Projekt und legt dann die Struktur an.
