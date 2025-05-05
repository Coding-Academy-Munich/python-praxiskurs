# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Dictionaries</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Dictionaries
#
# - Dictionaries sind eine Datenstruktur, die Schlüssel (Keys) auf Werte abbildet
# - Für Keys sind viele Typen möglich:
#   - Integer-Werte
#   - Strings
#   - Tupel
#   - ...
# - Modifizierbare Objekte, wie z.B. Listen, können nicht als Schlüssel verwendet werden
# - Werte können beliebige Python Objekte sein
# - Die Einträge in einem Dictionary sind nicht in einer bestimmten Reihenfolge
#   angeordnet
# - Einträge können hinzugefügt, gelöscht und modifiziert werden.

# %% [markdown]
#
# ### Leeres Dictionary:

# %%
{}

# %%
type({})

# %% [markdown]
#
# ## Dictionary mit String-Keys:

# %%
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Hose"}
translations

# %%
translations["snake"]

# %%
# translations["monkey"]

# %% [markdown]
#
# ### Zugriff mit Default-Wert

# %%
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Hose"}

# %%
translations.get("snake")

# %%
translations.get("monkey")

# %%
translations

# %%
translations.get("monkey", "<unbekannt>")

# %%
translations

# %% [markdown]
#
# ### Modifikation von Elementen

# %%
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Hose"}
translations

# %%
translations["horse"] = "Pferd"

# %%
translations

# %% [markdown]
#
# ### Update mit Default-Wert

# %%
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Pferd"}
translations

# %%
translations.get("bird", "Vogel")

# %%
translations

# %%
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Pferd"}
translations

# %%
translations.setdefault("bird", "Vogel")

# %%
translations

# %%
translations.setdefault("bird", "<unbekannt>")

# %%
translations


# %% [markdown]
#
# ## Mini-Workshop: Secondhand Verkauf
#
# Sie beschließen nicht mehr benötigte Kleidung bei einem Secondhand-Shop zu verkaufen.
# Um zu berechnen, wie hoch die Einnahmen sein werden,
# schreiben Sie eine Funktion
# `gesamtpreis(kleidungsstücke: list, preise: dict) -> float`:
#
# - `kleidungsstücke` ist eine Liste mit allen Kleidungsstücken, die Sie verkaufen
#   wollen, z.B.
#   ```python
#   ["Wintermantel", "Cordhose", "Smoking"]
#   ```
# - `preise` ist ein Dictionary mit den Preisen, die der Händler für jedes
#   Kleidungsstück bezahlt, z.B.
#   ```python
#   {"Wintermantel": 80, "Smoking": 40}
#   ```
# - Die Funktion `gesamtpreis()` gibt den Betrag zurück, den Ihnen der Händler für
#   die Kleidungsstücke in `kleidungsstücke` bezahlt.
# - Wenn in `kleidungsstücke` Einträge sind, die nicht in `preise` vorkommen,
#   dann kauft der Händler diese Kleidungsstücke nicht und Sie bekommen 0 Euro dafür.

# %%
def gesamtpreis(kleidungsstücke: list, preise: dict) -> float:
    ergebnis = 0
    for k in kleidungsstücke:
        ergebnis += preise.get(k, 0)
    return ergebnis


# %%
alte_kleidung = ["Wintermantel", "Cordhose", "Smoking"]
secondhand_preise = {"Wintermantel": 80, "Smoking": 40}

# %%
assert gesamtpreis(alte_kleidung, secondhand_preise) == 120
assert gesamtpreis(alte_kleidung + ["Smoking"], secondhand_preise) == 160

# %% [markdown]
# ## Vorbereitung für den nächsten Workshop

# %%
advice = "Don't worry be happy"

# %%
words = advice.split()

# %%
" ".join(words)

# %%
smileys = {"worry": "\U0001f61f", "happy": "\U0001f600"}


# %% [markdown]
# ## Mini-Workshop
#
# Schreiben Sie eine Funktion `replace_words(text: str, replacements: dict)`, die alle
# Wörter, die in `dict` als Key vorkommen durch ihren Wert in `dict` ersetzen.
#
# ```python
# >>> replace_words(advice, smileys)
# "Don't 😟 be 😀"
# ```

# %% [markdown]
#
# ### Hinweise
#
# - Splitten Sie `text` in eine Liste `words` aus einzelnen Wörtern
#
# - Erzeugen Sie eine neue leere Liste `new_words`
#
# - Iterieren Sie über `words` und fügen Sie jedes Wort, das nicht im Wörterbuch
#   vorkommt unverändert an `new_words` an; fügen Sie für jedes Wort, das im Wörterbuch
#   vorkommt seine Übersetzung an
#
# - Fügen Sie `new_words` mit der `join()`-Methode zu einem String zusammen

# %%
def replace_words(text: str, replacements: dict):
    new_words = []
    for word in text.split():
        new_words.append(replacements.get(word, word))
    return " ".join(new_words)


# %%
assert replace_words(advice, smileys) == "Don't 😟 be 😀"

# %%
assert replace_words("happy happy", smileys) == "😀 😀"


# %%
def replace_words_2(text: str, replacements: dict):
    return " ".join(replacements.get(word, word) for word in text.split())


# %%
assert replace_words_2(advice, smileys) == "Don't 😟 be 😀"
assert replace_words_2("happy happy", smileys) == "😀 😀"

# %% [markdown]
#
# ## Mini-Workshop "Inverser Index"
#
# Schreiben Sie eine Funktion `first_index(a_list: list) -> dict`, die ein Dictionary
# `d` zurückgibt, für das gilt:
#
# - Die Schlüssel in `d` sind alle in `a_list` vorkommenden Werte
# - Für jeden Wert `elt`, der in `a_list` enthalten ist, ist der Wert von `d[elt]`
#   der erste Index, an dem `elt` in `a_list` vorkommt
#
# ```python
# >>> first_index(["a", "b", "b"])
# {'a': 0, 'b': 1}
# ```
#
# *Hinweis:* Eine einfache Lösung verwendet die Funktion `enumerate()`.
#
# Stellen Sie sicher, dass Ihre Lösung die vorgegebenen Tests erfüllt.

# %%
def first_index(a_list: list):
    result = {}
    for index, elt in enumerate(a_list):
        result.setdefault(elt, index)
    return result


# %%
example_values = ["a", "b", "c", "b", "a", "c", "a"]

# %%
ii = first_index(example_values)

# %%
assert ii["a"] == 0

# %%
assert ii["b"] == 1

# %%
assert ii["c"] == 2

# %%
assert ii.get("d") is None

# %% [markdown]
#
# Schreiben Sie eine Funktion `inverse_index(a_list: list) -> dict`, die ein Dictionary
# `d` zurückgibt, für das gilt:
#
# - Die Schlüssel in `d` sind alle in `a_list` vorkommenden Werte
# - Für jeden Wert `elt`, der in `a_list` enthalten ist, ist der Wert von `d[elt]`
#   die Liste mit allen Indizes, an dem `elt` in `a_list` vorkommt
#
# ```python
# >>> inverse_index(["a", "b", "b"])
# {'a': [0], 'b': [1, 2]}
# ```


# %%
def inverse_index(a_list: list):
    result = {}
    for index, elt in enumerate(a_list):
        indices = result.setdefault(elt, [])
        indices.append(index)
    return result


# %%
example_values = ["a", "b", "c", "b", "a", "c", "a"]

# %%
ii = inverse_index(example_values)

# %%
assert ii["a"] == [0, 4, 6]

# %%
assert ii["b"] == [1, 3]

# %%
assert ii["c"] == [2, 5]

# %%
assert ii.get("d") is None

