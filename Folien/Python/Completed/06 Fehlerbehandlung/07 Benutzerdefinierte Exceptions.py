# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Benutzerdefinierte Exceptions</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Benutzerdefinierte Exceptionklassen
#
# - Es ist möglich, eigenen Exceptionklassen zu definieren.
# - Dazu genügt es, von `Exception` oder einer Unterklasse von `Exception` zu
#   erben.

# %%
class MyValueError(ValueError):
    pass


# %% [markdown]
#
# - Benutzerdefinierte Exceptions können wie alle anderen Exceptions erzeugt und
#   behandelt werden.

# %%
error = MyValueError("Oops!")
error

# %%
print(error)

# %% [markdown]
#
# - Exceptions können mit beliebig vielen Argumenten initialisiert werden.
# - Die Werte der Argumente können mit `args` abgefragt werden.

# %%
error = MyValueError("Oops!", 1, 2, 3)

# %%
print(error)

# %%
error.args

# %% [markdown]
#
# - Benutzerdefinierte Exceptions können genau wie alle anderen Exceptions
#   ausgelöst und behandelt werden.

# %%
# raise MyValueError("Oops!")

# %%
try:
    raise MyValueError("Oops!")
except MyValueError as error:
    print(f"Caught {type(error).__name__}: {error}")


# %% [markdown]
#
# ## Behandeln von Unterklassen einer Exception
#
# - Eine `except`-Klausel für eine Klasse `A` behandelt auch alle Unterklassen von `A`
# - Das gilt auch für benutzerdefinierte Exceptions

# %%
try:
    raise MyValueError("Oops!")
except ValueError as error:
    print(f"Caught {type(error).__name__}: {error}")

# %% [markdown]
#
# ## Wann eigene Exceptions definieren?
#
# Betrachte das Problem aus der Sicht des Benutzers:
#
# - Ist es sinnvoll spezifisch auf das Problem zu reagieren?
# - Ist eine bessere Fehlermeldung möglich?
# - Beispiele:
#   - `FileNotFoundError` statt `OSError`
#   - `DimensionMismatchError` statt `ValueError` für physikalische Berechnungen

# %% [markdown]
#
# ## Workshop: Benutzerdefinierte Exceptions
#
# - Schreiben Sie eine Funktion `read_email_from_user()`, die eine E-Mail-Adresse
#   vom Benutzer einliest.
# - Die Funktion soll eine benutzerdefinierte Exception `InvalidEmailError`
#   auslösen, wenn die E-Mail-Adresse nicht in der Liste `valid_mail_addresses`
#   enthalten ist.

# %%
valid_mail_addresses = [
    "joe@example.com",
    "jane@example.com",
    "jill@example.com",
]


# %%
class InvalidEmailError(ValueError):
    pass


# %%
def read_email_from_user():
    email = input("Enter your email address: ")
    if email not in valid_mail_addresses:
        raise InvalidEmailError(f"Invalid email address {email!r}.")
    return email


# %%
# read_email_from_user()
