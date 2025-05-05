# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Schreiben von guten Unit-Tests</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Welche Form hat ein Unit Test?
# - Arrange
# - Act
# - Assert

# %%
def test_the_extend_method_of_the_built_in_list_type():
    x = [1, 2, 3]  # arrange
    y = [10, 20]

    x.extend(y)  # act

    assert x == [1, 2, 3, 10, 20]  # assert


# %% [markdown]
#
# ## Wie finden wir gute Tests?

# %% [markdown]
#
# ## Versuch: Erschöpfendes Testen
#
# - Wir schreiben erschöpfende Tests, d.h. Tests, die alle möglichen Eingaben eines
#   Programms abdecken

# %% [markdown]
#
# - Erschöpfendes Testen ist nicht möglich
# - Beispiel Passworteingabe:
#   - Angenommen, Passwörter mit maximal 20 Zeichen sind zulässig,
#     80 Eingabezeichen sind erlaubt (große und kleine Buchstaben, Sonderzeichen)
#   - Das ergibt $80^{20}$ = 115.292.150.460.684.697.600.000.000.000.000.000.000
#     mögliche Eingaben
#   - Bei 10ns für einen Test würde man ca. $10^{24}$ Jahre brauchen, um alle Eingaben
#     zu testen
#   - Das Universum ist ungefähr $1.4 \times 10^{10}$ Jahre alt

# %% [markdown]
#
# ## Effektivität und Effizienz von Tests
#
# - Unit-Tests sollen effektiv und effizient sein
#   - Effektiv: Die Tests sollen so viele Fehler wie möglich finden
#   - Effizient: Wir wollen die größte Anzahl an Fehlern mit der geringsten Anzahl
#     an möglichst einfachen Tests finden
# - Effizienz ist wichtig, da Tests selbst Code sind, der gewartet werden muss und
#   Fehler enthalten kann

# %% [markdown]
#
# ## Eigenschaften von guten Unit-Tests
#
# Unit-Tests sollen
# - automatisiert sein: keine manuelle Interaktion
# - selbsttestend sein: Pass/Fail
# - feingranular sein
# - isoliert sein
# - zu jedem Zeitpunkt erfolgreich ausführbar sein
# - effektiv und effizient sein
#   - nicht viel Zeit zur Ausführung benötigen
#   - für alle wichtigen Systembestandteile geschrieben werden
#   - alle wichtigen Zustände jedes getesteten Elements abdecken

# %% [markdown]
#
# ## Wie schreibt man gute Unit-Tests?
#
# - Teste beobachtbares Verhalten, nicht Implementierung
# - Teste kleine Einheiten
# - Verwende Test-Doubles dann (aber auch nur dann), wenn eine Abhängigkeit
#   "eine Rakete abfeuert"
# - Bevorzuge Tests von Werten gegenüber Tests von Zuständen
# - Bevorzuge Tests von Zuständen gegenüber Tests von Verhalten
# - (Diese Regeln setzen voraus, dass der Code solche Tests erlaubt)

# %% [markdown]
#
# ### Warum Tests von beobachtbarem Verhalten, nicht Implementierung?
#
# Beobachtbares Verhalten
# - ist leichter zu verstehen
# - ist stabiler als Implementierung
# - entspricht eher dem Kundennutzen

# %% [markdown]
#
# ## Teste beobachtbares Verhalten, nicht Implementierung
#
# - Abstrahiere so weit wie möglich von Implementierungsdetails
#   - Auch auf Unit-Test Ebene
# - Oft testen sich verschiedene Methoden gegenseitig
# - Dies erfordert manchmal die Einführung von zusätzlichen Methoden
#     - Diese Methoden sollen für Anwender sinnvoll sein, nicht nur für Tests
#     - Oft "abstrakter Zustand" von Objekten
#     - **Nicht:** konkreten Zustand öffentlich machen

# %%
class Stack:  # type: ignore
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def push(self, new_item):
        self._items.append(new_item)

    def pop(self):
        return self._items.pop()


# %%
my_stack = Stack()
my_stack.push(5)

# %%
assert len(my_stack) == 1
assert my_stack.pop() == 5


# %% [markdown]
#
# ## Teste kleine Einheiten (bei Unit-Tests)
#
# - Test von kleinen Einheiten
#   - spezifizieren das Verhalten der getesteten Einheit besser
#   - erleichtern die Lokalisierung von Fehlern
#   - sind leichter zu pflegen
# - Tests größerer Einheiten oder des Gesamtsystems sind wichtig als
#   - Integrationstests
#   - Systemtests
#   - Akzeptanztests

# %% [markdown]
#
# ## Test Doubles
#
# - Test Double: Vereinfachte Version einer Abhängigkeit im System
#   - z.B. Ersetzen einer Datenbankabfrage durch einen fixen Wert
# - Test Doubles sind wichtig zum Vereinfachen von Tests
# - Aber: zu viele oder komplexe Test Doubles machen Tests unübersichtlich
#   - Was wird von einem Test eigentlich getestet?
# - Test Doubles: Dummies, Stubs, Fakes, Mocks, Spies
#   - Dummies, Stubs, Fakes: eingehende Abhängigkeiten
#   - Mocks, Spies: ausgehende Abhängigkeiten


# %% [markdown]
#
# ## Typischer Einsatz von Test Doubles
#
# - Zugriff auf Datenbank, Dateisystem
# - Zeit, Zufallswerte
# - Nichtdeterminismus
# - Verborgener Zustand (`AdderSpy`)

# %% [markdown]
#
# ## Werte > Zustand > Kommunikation
#
# - Verständlicher
# - Leichter zu testen
# - Oft stabiler gegenüber Refactorings
#
# Ausnahme: Testen von Protokollen


# %% [markdown]
#
# ### Wert

# %%
def add(x, y):
    return x + y


# %%
assert add(2, 3) == 5


# %% [markdown]
#
# ### Zustand

# %%
class Adder:
    def __init__(self):
        self.result = None

    def add(self, x, y):
        self.result = x + y


# %%
my_adder = Adder()
my_adder.add(2, 3)
assert my_adder.result == 5


# %% [markdown]
#
# ### Verhalten

# %%
def call_fun(fun):
    _hidden_result = fun(2, 3)
    # Presumably do something with _hidden_result...
    return "How do you test that fun was called?"


# %%
call_fun(lambda x, y: x + y)


# %%
class AdderSpy:
    def __init__(self):
        self.was_called = False
        self.result = None

    def __call__(self, x, y):
        self.was_called = True
        self.result = x + y
        return self.result


# %%
spy = AdderSpy()
assert not spy.was_called

# %%
assert spy(2, 3) == 5

# %%
assert spy.was_called
assert spy.result == 5

# %%
adder_spy = AdderSpy()
call_fun(adder_spy)
assert adder_spy.was_called
assert adder_spy.result == 5

# %% [markdown]
#
# ## Wie schreibt man testbaren Code?
#
# - Keine globalen oder statischen Daten
# - Techniken aus der funktionalen Programmierung (Iterables, Higher-order Funktionen,
#   etc.)
# - Funktionale Datenstrukturen (Immutability)
# - Gutes objektorientiertes Design
#   - Hohe Kohärenz
#   - Geringe Kopplung, Management von Abhängigkeiten
# - Etc.
#
# Hilfsmittel: Test-Driven Development


# %% [markdown]
#
# ## Mini-Workshop: Tests für die Einkaufslisten-Implementierung
#
# Fügen Sie zur Implementierung einer Einkaufsliste in `examples/ShoppingListPytestSK`
# geeignete Unit-Tests hinzu.
#
# Beachten Sie, dass Sie manche der Tests auch als Doctests schreiben können.
#
# (Falls Sie die Einkaufsliste in einem vorherigen Workshop bereits implementiert haben,
# ist es besser, Sie verwenden stattdessen Ihre eigene Implementierung.)
