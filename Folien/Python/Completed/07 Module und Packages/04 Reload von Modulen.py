# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Reload von Modulen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# - Module werden nur einmal geladen und dann im Speicher gehalten
# - Änderungen an der Datei werden nicht automatisch erkannt
# - Das ist beim Entwickeln vom Modulen etwas unpaktisch

# %%
# %load_ext autoreload
# %autoreload 0


# %%
import my_test_module

# %%
my_test_module.my_function()

# %%
my_test_module.my_variable

# %% [markdown]
#
# - Was passiert, wenn wir die Datei `my_test_module.py` ändern?

# %%
my_test_module.my_function()

# %%
my_test_module.my_variable

# %%
import my_test_module

# %%
my_test_module.my_function()

# %%
my_test_module.my_variable


# %% [markdown]
#
# ## Automatischer Reload von Modulen mit `importlib.reload`
#
# - Das Modul `importlib` bietet die Funktion `reload`
# - Damit kann ein Modul neu geladen werden

# %%
import importlib

# %%
importlib.reload(my_test_module)

# %%
my_test_module.my_function()

# %%
my_test_module.my_variable

# %% [markdown]
#
# ## Automatischer Reload von Modulen
#
# In IPython (und damit Jupyter Notebooks) ist es möglich das automatische Laden
# von modifizierten Modulen zu aktivieren:

# %%
# %load_ext autoreload
# %autoreload 2

# %%
import my_test_module


# %% [markdown]
#
# - Was passiert jetzt, wenn wir die Datei `my_test_module.py` ändern?

# %%
my_test_module.my_function()

# %%
my_test_module.my_variable


# %% [markdown]
#
# In Startup-Skripten kann man syntaktische Warnungen vermeiden, wenn man statt dessen
# schreibt:

# %%
try:
    get_ipython().run_line_magic("load_ext", "autoreload")  # noqa
    get_ipython().run_line_magic("autoreload", "2")  # noqa
except NameError:
    pass
