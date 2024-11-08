# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>String-Interpolation</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# # String Interpolation: F-Strings
#
# Python bietet die Möglichkeit, Werte in Strings einzusetzen:

# %%
name = "Hans"
zahl = 12
f"Hallo, {name}, die Zahl ist {zahl + 1}."

# %%
spieler_name = "Hans"
anzahl_spiele = 10
anzahl_gewinne = 2

ausgabe = f"Hallo {spieler_name}!\nSie haben {anzahl_spiele}-mal gespielt und dabei {anzahl_gewinne}-mal gewonnen."
print(ausgabe)

# %%
ausgabe = f"""\
Hallo {spieler_name}!
Sie haben {anzahl_spiele}-mal gespielt \
und dabei {anzahl_gewinne}-mal gewonnen.\
"""
print(ausgabe)

# %%
ausgabe = (
    f"Hallo {spieler_name}!\n"
    f"Sie haben {anzahl_spiele}-mal gespielt "
    f"und dabei {anzahl_gewinne}-mal gewonnen."
)
print(ausgabe)


# %% [markdown]
#
# ## Mini-Workshop: Begrüßung
#
# Schreiben Sie eine Funktion `drucke_begrüßung(name)`, die eine personalisierte
# Begrüßung ausgibt, z.B.
# ```
# Hallo, Hans!
# Schön Sie heute wieder bei uns begrüßen zu dürfen.
# Wir wünschen Ihnen viel Spaß, Hans.
# ```
# Verwenden Sie dazu String-Interpolation.

# %%
def drucke_begrüßung(name):
    print(
        f"Hallo, {name}!\n"
        f"Schön Sie heute wieder bei uns begrüßen zu dürfen.\n"
        f"Wir wünschen Ihnen viel Spaß, {name}."
    )


# %%
drucke_begrüßung("Hans")

# %%
