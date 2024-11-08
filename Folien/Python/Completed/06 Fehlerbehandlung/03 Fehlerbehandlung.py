# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Fehlerbehandlung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Behandeln von Exceptions
#
# Wir haben die folgende Funktion zur Berechnung ganzzahliger Quadratwurzeln
# definiert, die einen `ValueError` auslöst, falls `n` keine Quadratzahl ist:

# %%
def int_sqrt(n: int) -> int:
    for m in range(n + 1):
        if m * m == n:
            return m
    raise ValueError(f"{n} is not a square number.")


# %% [markdown]
#
# Wir konnten diese Funktion dann so verwenden:

# %%
def print_int_sqrt_v1(n):
    root = int_sqrt(n)
    print(f"The root of {n} is {root}.")


# %%
print_int_sqrt_v1(9)


# %%
# print_int_sqrt_v1(8)


# %% [markdown]
#
# Wie schreiben wir damit eine `print_int_sqrt()`-Funktion, die keinen Fehler auslöst,
# wenn `n` keine Quadratzahl ist?

# %%
def print_int_sqrt(n):  # type: ignore
    try:
        root = int_sqrt(n)
        print(f"The root of {n} is {root}.")
    except ValueError as error:
        print(error)


# %%
print_int_sqrt(9)


# %%
# print_int_sqrt(8)

# %% [markdown]
#
# ## Ausnahmebehandlung
#
# - Ausnahmen können mit einem `try`/`except`-Block behandelt werden
# - Alle "passenden" Ausnahmen, die während der Ausführung des `try`-Blocks
#   ausgelöst werden, führen zur Ausführung des `except`-Blocks
# - Wir sagen, die Ausnahme wurde behandelt
# - Nach der Behandlung der Ausnahme wird das Programm nach dem `try`/`except`-Block
#   weiter ausgeführt

# %%
def print_int_sqrt(n):  # type: ignore
    try:
        root = int_sqrt(n)
        print(f"The root of {n} is {root}.")
    except ValueError as error:
        print(error)
    print("Done!")


# %%
print_int_sqrt(9)


# %%
print_int_sqrt(8)


# %% [markdown]
#
# ## Workshop: Bank Account (Teil 2)
#
# Wir haben eine Klasse `BankAccount` definiert, die in folgenden Fällen einen
# `ValueError` auslöst:
#
# - Wenn ein neuer `BankAccount` mit negativer `balance` angelegt werden soll.
# - Wenn `deposit` mit einem negativen Wert aufgerufen wird.
# - Wenn `withdraw` mit einem negativen Wert aufgerufen wird oder durch das
#   Abheben des Betrags die `balance` des Kontos negativ werden würde.

# %% [markdown]
#
# Testen Sie die Funktionalität der Klasse sowohl für erfolgreiche
# Transaktionen, als auch für Transaktionen, die Exceptions auslösen.
# Behandeln Sie dabei die Ausnahmen, die ausgelöst werden und geben Sie
# eine sinnvolle Nachricht aus.

# %%
class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError(
                f"Cannot create an account with negative balance: {balance}."
            )
        self.balance = balance

    def __repr__(self):
        return f"BankAccount({self.balance:.2f})"

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError(f"Cannot deposit a negative amount: {amount}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError(f"Cannot withdraw a negative amount: {amount}")
        if amount > self.balance:
            raise ValueError(
                f"Cannot withdraw {amount} because it exceeds "
                f"the current balance of {self.balance}."
            )
        self.balance -= amount


# %%
try:
    BankAccount(100.0)
except ValueError as error:
    print("ERROR:", error)

# %%
try:
    BankAccount(-100)
except ValueError as error:
    print("ERROR:", error)

# %%
b = BankAccount(100.0)
b

# %%
try:
    b.deposit(200.0)
    b
except ValueError as error:
    print("ERROR:", error)

# %%
try:
    b.deposit(-100.0)
    b
except ValueError as error:
    print("ERROR:", error)

# %%
try:
    b.withdraw(50.0)
    b
except ValueError as error:
    print("ERROR:", error)

# %%
try:
    b.withdraw(-200.0)
    b
except ValueError as error:
    print("ERROR:", error)

# %%
try:
    b.withdraw(1000.0)
    b
except ValueError as error:
    print("ERROR:", error)
