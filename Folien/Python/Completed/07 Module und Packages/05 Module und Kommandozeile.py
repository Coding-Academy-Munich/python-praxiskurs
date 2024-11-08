# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Module und Kommandozeile</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# - Wir können Python-Module auch direkt von der Kommandozeile ausführen
# - Dazu verwenden wir das Kommando `python -m <modulname>`
# - Im Gegensatz zu `python <modulname>.py` wird das Modul auch gefunden, wenn
#   es nicht im aktuellen Verzeichnis liegt

# %%
# !python my_test_module.py

# %%
# !python -m my_test_module

# %%
# !python -m pip --version

# %% [markdown]
#
# - Dabei ist es zweckmäßig, wenn das Modul eine `main()` Funktion enthält, die
#   ausgeführt wird
# - Das sollte aber nur passieren, wenn das Modul direkt ausgeführt wird
# - Dazu können wir die Variable `__name__` verwenden:
#   - Der Wert von `__name__` ist der String `"__main__"`, wenn das Modul direkt
#     ausgeführt wird (also nicht importiert wird)
#   - `__name__` ist der Modulname, wenn das Modul importiert wird

# %% [markdown]
#
# - Um die `main()` Funktion nur auszuführen, wenn das Modul direkt ausgeführt
#   wird, können wir folgenden Code verwenden:

# %%
def main():
    print("Hello from main()")


# %%
if __name__ == "__main__":
    main()


# %%
# !python -m main_test

# %%
import main_test

# %% [markdown]
#
# ## Workshop: Modul und Kommandozeile
#
# - Schreiben Sie ein Modul `cli_module`, das eine Funktion `main()` enthält
# - Die Funktion `main()` soll `CLI Module is starting...` ausgeben
# - Das Modul soll direkt von der Kommandozeile ausführbar sein und dann die
#   Funktion `main()` ausführen
# - Die Funktion `main()` soll **nur** ausgeführt werden, wenn das Modul direkt
#   ausgeführt wird
# - Wenn das Modul importiert wird, soll die Funktion `main()` **nicht**
#   ausgeführt werden


# %%
# !python -m cli_module_solution

# %%
import cli_module_solution
