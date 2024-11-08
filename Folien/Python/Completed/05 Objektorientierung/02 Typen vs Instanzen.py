# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Typen vs. Instanzen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Typen vs. Instanzen
#
# In Python können benutzerdefinierte Datentypen (Klassen) definiert werden.
#
# Um uns darauf vorzubereiten, wollen wir uns den Unterschied zwischen Typen
# und Instanzen von Typen (Objekten) in [Python Tutor](https://tinyurl.com/yc8r5d45)
# ansehen.

# %%
list_instance = list("abc")


# %%
def my_fun(arg: list):
    pass


# %%
my_fun(list_instance)

# %%
my_fun(list("xyz"))

# %%
my_fun(list)
