# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Arbeiten mit Jupyter Notebooks</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ## Arbeiten mit Notebooks
#
# - Notebooks sind in Zellen aufgeteilt
# - Zellen können entweder Text oder Python Code enthalten.
# - Es gibt zwei Modi: Kommando- und Edit-Modus (`Esc` / `Enter`)
# - Einige Tastaturkürzel: `Strg`-`Enter`, `Shift`-`Enter`, `Tab`, `Shift-Tab`

# %%
def say_hello(name):
    """Greet the user."""
    print(f"Hello, {name}.")


# %%
say_hello("World")

# %%
say_hello("you")

# %%
123

# %%
17 + 4

# %%
answer = 42
answer

# %%
# fmt: off
answer;
# fmt: on
