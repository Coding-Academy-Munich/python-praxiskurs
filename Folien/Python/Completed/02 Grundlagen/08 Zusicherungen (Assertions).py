# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Zusicherungen (Assertions)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ### Zusicherungen
#
# Zusicherungen (Assertions) sind eine gute Möglichkeit sicherzustellen, dass
# eine Eigenschaft erfüllt ist. Wenn die getestete Eigenschaft erfüllt ist,
# macht die Assertion nichts:

# %%
assert 1 == 1

# %%
assert 1 != 2

# %% [markdown]
#
# Wenn die getestete Eigenschaft nicht erfüllt ist, wird ein Fehler ausgelöst:

# %%
# assert 1 == 2


# %% [markdown]
# ### Mini-Workshop
#
# Gegeben seien die folgenden Anweisungen:

# %%
my_int = 1
my_float = 1.0

# %% [markdown]
#
# Schreiben Sie für jede der folgenden Eigenschaften eine Assertion, die
# entweder die Eigenschaft oder ihre Negation zusichert und keinen Fehler
# auslöst:
#
# - `my_int == 1`
# - `my_float == my_int`
# - `my_float == "1.0"`

# %%
assert my_int == 1
assert my_float == my_int
assert my_float != "1.0"
