# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Assertions</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Assertions
#
# Das Assert-Statement ist nur eine kompakte Schreibweise, um eine bestimmte Art von
# Fehler (einen `AssertionError`) auszulösen, wenn eine Bedingung falsch ist:

# %%
my_var = 1

# %%
assert my_var == 1

# %%
if my_var != 1:
    raise AssertionError()

# %%
# assert my_var == 2

# %% [markdown]
#
# Assert mit optionalem Fehler-Text:

# %%
assert my_var == 1, "my_var should be 1"

# %%
if my_var != 1:
    raise AssertionError("my_var should be 1")

# %%
# assert my_var == 2, "my_var should be 2"

# %% [markdown]
#
# - Assertions können mit dem `-O`-Flag deaktiviert werden.

# %%
# %pycat test_assert.py

# %%
# !python test_assert.py

# %%
# !python -O test_assert.py


# %% [markdown]
#
# - Assertions sind nützlich, um Annahmen über den Programmzustand zu dokumentieren.
# - Sie sind aber nicht dazu gedacht, Fehler in Eingaben abzufangen.

# %%
def bad_user_input():
    number = input("Please enter a number: ")
    assert number.isdigit(), "Input must be a number!"
    return int(number)


# %%
def better_user_input():
    number = input("Please enter a number: ")
    if not number.isdigit():
        raise ValueError("Input must be a number!")
    return int(number)


# %% [markdown]
#
# ## Workshop: Assertions
#
# Das Programm `valid_mail.py` fragt den Benutzer nach einer E-Mail-Adresse und
# gibt diese wieder aus, wenn sie in der Liste `valid_mail_addresses` enthalten
# ist.
#
# Bei ungültigen Eingaben wird eine Exception ausgelöst.
#
# - Führen Sie das Programm mit verschiedenen Eingaben aus und beobachten Sie das
#   Verhalten.
# - Wie können Sie das Programm dazu bringen, auch ungültige Eingaben zu akzeptieren?
# - Schreiben Sie das Programm so um, das dies nicht mehr möglich ist.

# %%
# # !python valid_mail.py

# %%
# # !python -O valid_mail.py
