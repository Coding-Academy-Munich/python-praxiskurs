# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Kontrollstrukturen (Teil 3)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
#  ## Bessere Klassifizierung
#
# In einem der letzten Videos hatten wir die folgende Funktion zur Klassifizierung
# von Zahlen eingeführt:

# %%
def klassifiziere_zahl(geratene_zahl, lösung):
    if geratene_zahl < lösung:
        print("Die geratene Zahl ist zu klein!")
    elif geratene_zahl > lösung:
        print("Die geratene Zahl ist zu groß!")
    else:
        print("Sie haben gewonnen!")


# %%
klassifiziere_zahl(10, 12)

# %%
klassifiziere_zahl(14, 12)

# %%
klassifiziere_zahl(12, 12)


# %% [markdown]
#
# Wir wollen dem Spieler jetzt etwas mehr Information geben, wie nahe er an der
# richtigen Lösung ist:
#
# - Teile dem Spieler mit, wenn die geratene Zahl sehr weit von der gesuchten Zahl
#   entfernt ist
# - Ausgabe: "Die geratene Zahl ist viel zu klein/zu groß!", wenn der Unterschied
#   größer als 10 ist

# %%
def klassifiziere_zahl_2(geratene_zahl, lösung):
    if geratene_zahl < lösung - 10:
        print("Die geratene Zahl ist viel zu klein!")
    elif geratene_zahl < lösung:
        print("Die geratene Zahl ist zu klein!")
    elif geratene_zahl > lösung + 10:
        print("Die geratene Zahl ist viel zu groß!")
    elif geratene_zahl > lösung:
        print("Die geratene Zahl ist zu groß!")
    else:
        print("Sie haben gewonnen!")


# %%
klassifiziere_zahl_2(1, 12)

# %%
klassifiziere_zahl_2(10, 12)

# %%
klassifiziere_zahl_2(14, 12)

# %%
klassifiziere_zahl_2(24, 12)

# %%
klassifiziere_zahl_2(12, 12)


# %% [markdown]
#
#  Die Reihenfolge der `if`- und `elif`-Zweige ist wichtig:

# %%
def klassifiziere_zahl_3(geratene_zahl, lösung):
    if geratene_zahl < lösung:
        print("Die geratene Zahl ist zu klein!")
    elif geratene_zahl < lösung - 10:
        print("Die geratene Zahl ist viel zu klein!")
    elif geratene_zahl > lösung:
        print("Die geratene Zahl ist zu groß!")
    elif geratene_zahl > lösung + 10:
        print("Die geratene Zahl ist viel zu groß!")
    else:
        print("Sie haben gewonnen!")


# %%
klassifiziere_zahl_3(1, 12)

# %%
klassifiziere_zahl_3(100, 12)


# %% [markdown]
#
#  ## Return aus einem `if`-Statement
#
#  Die Zweige eines `if`-Statements können `return` Anweisungen enthalten um
#  einen Wert aus einer Funktion zurückzugeben:

# %%
def klassifiziere_zahl_4(zahl):
    if zahl > 100:
        return "groß"
    else:
        return "klein"


# %%
klassifiziere_zahl_4(1)

# %%
klassifiziere_zahl_4(200)


# %% [markdown]
#
# ## Mini-Workshop: Signum
#
# Schreiben Sie eine Funktion `signum(zahl)`, die
#
# - 1 zurückgibt, falls `zahl > 0` ist,
# - 0 zurückgibt, falls `zahl == 0` ist,
# - -1 zurückgibt, falls `zahl < 0` ist.

# %%
def signum(zahl):
    if zahl > 0:
        return 1
    elif zahl == 0:
        return 0
    else:
        return -1


# %% [markdown]
# Testen Sie die Funktion für repräsentative Werte.

# %%
assert signum(-10) == -1

# %%
assert signum(0) == 0

# %%
assert signum(2) == 1
