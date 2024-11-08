# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Importieren von Modulen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# - `import` Anweisung
# - `from`-`import` Anweisung
# - Umbenennen mit `as`

# %% [markdown]
#
# ### Importieren mit `from`-`import`
#
# - Statt das gesamte Modul zu importieren, können wir auch einzelne Funktionen
#   importieren
# - Syntax: `from <modulname> import <funktionsname>`
# - Damit ist nur die importierte Funktion verfügbar
# - Ihr Name kann direkt verwendet werden, ohne den Modulnamen voranzustellen

# %%
# import my_test_module

# %%
from my_test_module import multiply_by_2

# %%
multiply_by_2(2)

# %%
from my_test_module import add1

# %%
# add1(2)

# %% [markdown]
#
# - Wenn wir mehrere Funktionen aus einem Modul importieren, können wir sie
#   mit Kommas trennen

# %%
from my_test_module import add1, multiply_by_2, perform_complex_computation

# %%
add1(2)

# %%
multiply_by_2(2)

# %%
perform_complex_computation(10)

# %% [markdown]
#
# ### Umbenennen mit `as`
#
# - Manchmal ist der Name eines Moduls zu lang oder nicht aussagekräftig
# - Dann können wir das Modul mit `as` umbenennen

# %%
import my_test_module as mm

# %%
mm.add1(1)

# %%
mm.perform_complex_computation(17)

# %% [markdown]
#
# - Wir können auch Funktionen umbenennen

# %%
from my_test_module import multiply_by_2 as mult2


# %%
mult2(4)

# %% [markdown]
#
# ### Importieren aller Namen mit `*`
#
# - Wir können alle Namen eines Moduls mit `*` importieren
# - Syntax: `from <modulname> import *`
# - Damit werden (fast) alle im Modul definierten Namen importiert
#   - Ausnahme: Namen, die mit `_` beginnen
# - Der Name des Moduls wird nicht importiert
# - Außer zum interaktiven Experimentieren sollten wir dies vermeiden

# %%
from my_test_module import *


# %%
multiply_by_2(3)


# %%
add1(3)

# %% [markdown]
#
# ## Workshop: Importieren von Modulen
#
# - Importieren Sie das Modul `workshop_module`, das Sie im vorherigen Workshop
#   erstellt haben unter dem Namen `wm`
# - Rufen Sie die Funktionen `say_hello()` und `say_bye()` auf

# %%
import workshop_module_solution as wm

# %%
wm.say_hello()

# %%
wm.say_bye()

# %% [markdown]
#
# - Importieren Sie die Funktion `say_hello()` aus dem Modul `workshop_module`.
# - Importieren Sie die Funktion `say_bye()` aus dem Modul `workshop_module` unter
#   dem Namen `goodbye`.
# - Rufen Sie die Funktionen auf.
# - Was passiert, wenn Sie `say_bye()` aufrufen?

# %%
from workshop_module_solution import say_hello

# %%
say_hello()

# %%
from workshop_module_solution import say_bye as goodbye

# %%
goodbye()

# %%
# say_bye()
