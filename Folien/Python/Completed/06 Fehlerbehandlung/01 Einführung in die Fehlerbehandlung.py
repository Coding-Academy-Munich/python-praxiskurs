# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Einführung in die Fehlerbehandlung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Fehlerbehandlung
#
# Wir wollen eine Funktion `int_sqrt(n: int) -> int` schreiben, die die
# "Ganzzahlige Wurzel" berechnet:
# - Wenn `n` eine Quadratzahl ist, also die Form `m * m` hat, dann soll `m`
#   zurückgegeben werden.
# - Was machen wir, falls `n` keine Quadratzahl ist?
# - Um den Mechanismus, den Python verwendet, zu motivieren, besprechen wir erst
#   zwei andere Möglichkeiten Fehler zu behandeln


# %% [markdown]
#
# - Wir können versuchen, einen "Fehlerwert" zurückzugeben, der kein gültiges
#   Ergebnis ist.
# - Hier z.B. eine negative Zahl

# %%
def int_sqrt_with_negative_value(n: int) -> int:
    for m in range(n + 1):
        if m * m == n:
            return m
    return -1


# %%
int_sqrt_with_negative_value(9)

# %%
int_sqrt_with_negative_value(8)


# %% [markdown]
#
# - Diese Version ist einfach zu verwenden, aber fehleranfällig:

# %%
def print_int_sqrt_1(n):
    root = int_sqrt_with_negative_value(n)
    print(f"The root of {n} is {root}.")


# %%
print_int_sqrt_1(9)

# %%
print_int_sqrt_1(8)


# %% [markdown]
#
# - Code zur Fehlerbehandlung ist mit dem "Erfolgsfall" verwoben

# %%
def print_int_sqrt_1_better(n):
    root = int_sqrt_with_negative_value(n)
    if root < 0:
        print(f"{n} does not have a root!")
    else:
        print(f"The root of {n} is {root}.")


# %%
print_int_sqrt_1_better(9)

# %%
print_int_sqrt_1_better(8)


# %% [markdown]
#
# - Wir können auch zwei Werte zurückgeben: Ergebnis und ein Erfolg/Fehler Flag

# %%
def int_sqrt_with_pair(n: int) -> tuple[int, bool]:
    for m in range(n + 1):
        if m * m == n:
            return m, True
    return 0, False


# %%
int_sqrt_with_pair(9)

# %%
int_sqrt_with_pair(8)


# %% [markdown]
#
# - Die Probleme bei dieser Lösung sind ähnlich wie bei der vorhergehenden.

# %%
def print_int_sqrt_2(n):
    root, is_valid = int_sqrt_with_pair(n)
    print(f"The root of {n} is {root}.")


# %%
print_int_sqrt_2(9)

# %%
print_int_sqrt_2(8)


# %% [markdown]
#
#  Beide Ansätze haben mehrere Probleme:
#  - Die Fehlerbehandlung ist optional. Wird sie nicht durchgeführt, so wird mit
#    einem falschen Wert weitergerechnet.
#  - Kann der Aufrufer den Fehler nicht selber behandeln, so muss der Fehler über
#    mehrere Ebenen von Funktionsaufrufen "durchgereicht" werden.
#  - Das führt zu
#    unübersichtlichem Code, da der "interessante" Pfad nicht vom Code zur
#    Fehlerbehandlung getrennt ist.

# %% [markdown]
#
# ## Gewünschte Eigenschaften
#
# - Normale Programmlogik wird nicht beeinträchtigt
# - Behandlung von Fehlern wird erzwungen
# - Entdecken eines Fehlers ist entkoppelt von seiner Behandlung
# - Information über den Fehler kann leicht zum Handler kommuniziert werden
