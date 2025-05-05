# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Docstrings</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Docstrings
#
# Jede Funktion in Python kann dokumentiert werden, indem ein String-Literal als
# erstes Element im Rumpf angegeben wird. Meistens wird dafür ein `"""`-String
# verwendet:

# %%
def my_fun(x):
    """
    Zeigt dem Benutzer den Wert von x an.

    Verwendung:

    >>> my_fun(123)
    Das Argument x hat den Wert 123
    """
    print("Das Argument x hat den Wert", x)


# %%
my_fun(123)

# %% [markdown]
#
# Konventionen für Docstrings finden sich in
# [PEP 257](https://www.python.org/dev/peps/pep-0257/).

# %% [markdown]
#
# Der Docstring einer Funktion kann mit `help()` ausgegeben werden:

# %%
help(my_fun)

# %% [markdown]
#
# In Jupyter kann man den Docstring einer Funktion durch ein vorangestelltes
# oder nachgestelltes Fragezeichen anzeigen lassen:

# %%
# # ?my_fun


# %%
# # my_fun?


# %% [markdown]
#
# Oft verwendet man statt dessen Shift-Tab:

# %%
my_fun

# %% [markdown]
#
# Bei Funktionen mit langen Docstrings kann man durch zweimaliges Drücken von
# `Shift-Tab` auf die ausführliche Anzeigeform umschalten:

# %%
my_fun

# %%
print
