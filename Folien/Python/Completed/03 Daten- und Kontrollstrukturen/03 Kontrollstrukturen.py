# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Kontrollstrukturen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# # `if`-Anweisungen
#
# - Wir wollen ein Programm schreiben, das bestimmt ob eine Zahl eine Glückszahl
#   ist oder nicht:
#     - 7 ist eine Glückszahl
#     - Alle anderen Zahlen sind es nicht.
# - Wir benötigen dazu die `if`-Anweisung:

# %%
def ist_glückszahl(zahl):
    if zahl == 7:
        print("Glückszahl")
    else:
        print("Keine Glückszahl")


# %%
ist_glückszahl(1)

# %%
ist_glückszahl(7)


# %%
def ist_glückszahl_1(zahl):
    print("Ist", zahl, "eine Glückszahl?")

    if zahl == 7:
        print("Ja!")
    else:
        print("Leider nein.")

    print("Wir wünschen Ihnen alles Gute.")


# %%
ist_glückszahl_1(1)

# %%
ist_glückszahl_1(7)


# %%
def ist_glückszahl_2(zahl):
    if zahl == 7:
        print(zahl, "ist eine Glückszahl!")
        print("Sie haben sicher einen super Tag!")
    else:
        print(zahl, "ist leider keine Glückszahl.")
        print("Vielleicht sollten Sie heute lieber im Bett bleiben.")
        print("Wir wünschen Ihnen trotzdem alles Gute.")


# %%
ist_glückszahl_2(1)

# %%
ist_glückszahl_2(7)


# %% [markdown]
# ## Struktur einer `if`-Anweisung (unvollständig):
#
# ```python
# if <Bedingung>:
#     Rumpf, der ausgeführt wird, wenn <Bedingung> wahr ist
# else:
#     Rumpf, der ausgeführt wird, wenn <Bedingung> falsch ist
# ```
# - Nur das `if` und der erste Rumpf sind notwendig
# - Falls ein `else` vorhanden ist, so darf der entsprechende Rumpf nicht leer sein
#

# %% [markdown]
#
# ## Mini-Workshop: Volljährig

# %% [markdown]
#
# Schreiben Sie eine Funktion `drucke_volljährig(alter)`, die `Volljährig`
# auf dem Bildschirm ausgibt, wenn `alter >= 18` ist und `Minderjährig` sonst.

# %%
def drucke_volljährig(alter):
    if alter < 18:
        print("Minderjährig")
    else:
        print("Volljährig")


# %% [markdown]
# Testen Sie `drucke_volljährig(alter)` mit den Werten 17 und 18.

# %%
drucke_volljährig(17)
drucke_volljährig(18)

# %% [markdown]
#
# ## Mini-Workshop: Gerade Zahl


# %% [markdown]
#
# Schreiben Sie eine Funktion `ist_gerade(zahl)`, die `True` zurückgibt,
# falls `zahl` gerade ist und `False`, falls `zahl` ungerade ist.

# %%
def ist_gerade(zahl):
    return zahl % 2 == 0


# %% [markdown]
#
# Schreiben Sie Assertions, die testen ob `ist_gerade()` für die Argumente 0, 1
# und 8 das korrekte Ergebnis liefert.

# %%
assert ist_gerade(0)
assert not ist_gerade(1)
assert ist_gerade(8)


# %% [markdown]
# Schreiben Sie eine Funktion `drucke_ist_gerade(zahl)`, die
#
# - `{zahl} ist gerade.` auf dem Bildschirm ausgibt, falls `zahl` gerade ist und
# - `{zahl} ist ungerade.` auf dem Bildschirm ausgibt, falls `zahl` nicht
#   gerade ist.
#
# Verwenden Sie dabei dei Funktion `ist_gerade()` um zu überprüfen, ob `zahl`
# gerade ist.

# %%
def drucke_ist_gerade(zahl):
    if ist_gerade(zahl):
        print(f"{zahl} ist gerade.")
    else:
        print(f"{zahl} ist ungerade.")


# %% [markdown]
# Testen Sie `drucke_ist_gerade(zahl)` mit den Werten 0, 1 und 8.

# %%
drucke_ist_gerade(0)
drucke_ist_gerade(1)
drucke_ist_gerade(8)

# %% [markdown]
#
# ## Mini-Workshop: Verkürzte Ausgabe


# %% [markdown]
#
# Schreiben Sie eine Funktion `fits_in_line(text: str, line_length: int = 72)`,
# die `True` oder `False` zurückgibt, je nachdem ob `text` in einer Zeile der
# Länge `line_length` ausgegeben werden kann oder nicht:
# ```python
# >>> fits_in_line("Hallo")
# True
# >>> fits_in_line("Hallo", 3)
# False
# ```
#
# *Hinweis:* Sie können die Länge eines Strings mit der Funktion `len()` bestimmen:
# ```python
# >>> len("abcd")
# 4
# ```


# %%
def fits_in_line(text: str, line_length: int = 72):
    return len(text) <= line_length


# %%
fits_in_line("Hello")

# %%
fits_in_line("Hello", 3)


# %% [markdown]
#
# Schreiben Sie eine Funktion `print_line(text: str, line_length:int = 72)`,
# die
# * `text` auf dem Bildschirm ausgibt, falls das in einer Zeile der Länge
#   `line_length` möglich ist
# * `...` ausgibt, falls das nicht möglich ist.
#
# ```python
# >>> print_line("Hallo")
# Hallo
# >>> print_line("Hallo", 3)
# ...
# >>>
# ```

# %%
def print_line(text: str, line_length: int = 72):
    if fits_in_line(text, line_length=line_length):
        print(text)
    else:
        print("...")


# %%
print_line("Hallo")

# %%
print_line("Hallo", 3)

