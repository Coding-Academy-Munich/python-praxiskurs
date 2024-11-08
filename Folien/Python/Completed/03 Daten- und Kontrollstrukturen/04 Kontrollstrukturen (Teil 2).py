# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Kontrollstrukturen (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Einseitiges `if`

# %%
def einseitiges_if(zahl):
    print("Vorher")
    if zahl == 7:
        print(zahl, "ist eine Glückszahl")
        print("Glückwunsch!")
    print("Nachher")


# %%
einseitiges_if(1)

# %%
einseitiges_if(7)


# %% [markdown]
#
#  ## Mehrere Zweige
#
#  - Wir wollen ein Spiel schreiben, in dem der Spieler eine Zahl zwischen 1 und
#    100 erraten muss.
#  - Nachdem er geraten hat, bekommt er die Information, ob seine Zahl zu hoch,
#    zu niedrig oder richtig war angezeigt.
#  - Später wollen wir dem Spieler mehrere Versuche erlauben.

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
#  ## Struktur einer `if`-Anweisung (vollständig):
#
# ```python
# if {Bedingung 1}:
#     Rumpf, der ausgeführt wird, wenn {Bedingung 1} wahr ist
# elif {Bedingung 2}:
#     Rumpf, der ausgeführt wird, wenn {Bedingung 2} wahr ist
# ...
# else:
#     Rumpf, der ausgeführt wird, wenn keine der Bedingungen wahr ist
# ```
# - Nur das `if` und der erste Rumpf sind notwendig
# - Falls ein `elif` oder ein `else` vorhanden ist, so darf der entsprechende
#   Rumpf nicht leer sein

# %% [markdown]
# ## Mini-Workshop: Positiv / Negativ
#
# Schreiben Sie eine Funktion `drucke_ist_positiv(zahl)`, die
#
# - `{zahl} ist positiv.` auf dem Bildschirm ausgibt, falls `zahl > 0` ist,
# - `{zahl} ist Null.` auf dem Bildschirm ausgibt, falls `zahl == 0` ist,
# - `{zahl} ist negativ.` auf dem Bildschirm ausgibt, falls `zahl < 0` ist.

# %%
def drucke_ist_positiv(zahl):
    if zahl > 0:
        print(f"{zahl} ist positiv.")
    elif zahl < 0:
        print(f"{zahl} ist negativ.")
    else:
        print("0 ist Null.")


# %% [markdown]
# Testen Sie `drucke_ist_positiv(zahl)` mit den Werten -3, 0 und 2.

# %%
drucke_ist_positiv(-3)
drucke_ist_positiv(0)
drucke_ist_positiv(2)
