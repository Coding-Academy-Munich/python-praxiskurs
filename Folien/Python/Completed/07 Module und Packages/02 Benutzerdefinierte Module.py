# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Benutzerdefinierte Module</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Benutzerdefinierte Module
#
# Ein benutzerdefiniertes Modul ist eine Datei mit Python-Code.
#
# - Wenn sich ein Python-Modul im Suchpfad befindet, kann es mit `import`
#   geladen werden.
# - Standardmäßig ist das aktuelle Verzeichnis im Suchpfad enthalten.
#  - Jupyter Notebooks lassen sich nicht (ohne zusätzliche Pakete) als Module laden.

# %%
import os

# %% [markdown]
#
# Aktuelles Verzeichnis:

# %%
os.getcwd()

# %% [markdown]
#
# Welche Dateien befinden sich im aktuellen Verzeichnis?

# %%
for filename in os.listdir(os.getcwd()):
    if filename[-3:] == ".py":
        print(filename)

# %% [markdown]
#
# Anzeigen des Quellcodes von `my_test_module.py`

# %%
# # %pycat my_test_module.py

# %% [markdown]
#
# ## Laden von Modulen
#
# - Die `import`-Anweisung lädt die zum Modul gehörige Datei
# - Top-Level Code wird ausgeführt
# - Das Modul wird in einem Cache gespeichert

# %%
import my_test_module

# %%
my_test_module.add1(2)


# %%
# add1

# %% [markdown]
#
# ## Top-Level Code
#
# - Der Top-Level Code wird beim Laden des Moduls ausgeführt
# - In der Regel werden hier Funktionen, Klassen und Variablen definiert
#   - Python definiert einige Variablen automatisch, z.B. `__name__` mit dem
#     Namen des Moduls
# - Der Top-Level Code wird nur einmal ausgeführt
#   - Beim erneuten Import des Moduls verwendet der Interpreter die Version aus dem
#     Cache
# - Die Funktionen, Klassen und Variablen werden in den Namespace des Moduls
#   eingefügt

# %%
__name__

# %%
import my_test_module

# %% [markdown]
#
# ## Workshop: Modul
#
# Definieren Sie ein Modul `workshop_module`, das folgende Funktionen enthält:
#
# - `say_hello()`: Gibt `"Hello"` aus
# - `say_bye()`: Gibt `"Bye"` aus
#
# Importieren Sie das Modul und rufen Sie die Funktionen auf.


# %%
import workshop_module_solution

# %%
workshop_module_solution.say_hello()

# %%
workshop_module_solution.say_bye()
