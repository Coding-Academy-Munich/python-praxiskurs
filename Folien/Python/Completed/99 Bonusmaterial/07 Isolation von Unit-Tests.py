# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Isolation von Unit-Tests</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Unit-Test
#
# - Testet einen kleinen Teil des Codes (eine "Unit")
# - Hat kurze Laufzeit
# - *Ist isoliert*

# %% [markdown]
#
# ## Was bedeutet "isolierter" Test?
#
# - Keine Interaktion zwischen Tests?
#   - Isolierte Testfälle
#   - Klassische Unit-Tests (Detroit School, Kent Beck)
# - Keine Interaktion zwischen getesteter Einheit und dem Rest des Systems?
#   - Externe Subsysteme werden durch einfache Simulationen ersetzt (Mocks)
#   - London School

# %% [markdown]
#
# ## Isolierte Testfälle
#
# - Jeder Testfall ist unabhängig von den anderen
# - Tests können in beliebiger Reihenfolge ausgeführt werden
# - Tests können parallel ausgeführt werden

# %% [markdown]
#
# ### Gegenbeispiel: Nicht isolierte Testfälle

# %%
import time

# %%
global_time = time.time()


# %%
def test_1():
    assert time.time() > global_time


# %%
def test_2():
    global global_time
    global_time = time.time() + 1000
    assert time.time() < global_time


# %%
test_1()
test_2()


# %%
# test_2()
# test_1()

# %% [markdown]
#
# ## Gründe für nicht isolierte Testfälle
#
# - Veränderlicher globaler Zustand
# - Veränderliche externe Resourcen (Dateien, Datenbanken, Netzwerk, ...)

# %% [markdown]
#
# ## Isolation der getesteten Unit
#
# - Die getestete Unit wird von allen anderen Units isoliert
# - Test-Doubles für alle Abhängigkeiten

# %% [markdown]
#
# ### Gegenbeispiel: Nicht isolierte Unit

# %%
class Event:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def reserve(self, num_tickets):
        if num_tickets > self.capacity:
            raise ValueError("Not enough capacity")
        self.capacity -= num_tickets


# %%
class TicketOffice:
    def __init__(self):
        self.events = {}

    def add_event(self, event):
        self.events[event.name] = event

    def purchase_tickets(self, event_name, num_tickets):
        try:
            self.events[event_name].reserve(num_tickets)
            return True
        except ValueError:
            return False


# %%
def test_purchase_tickets():
    ticket_office = TicketOffice()
    event = Event("PyCon", 100)
    ticket_office.add_event(event)

    result = ticket_office.purchase_tickets("PyCon", 10)

    assert result is True
    assert event.capacity == 90


# %%
test_purchase_tickets()

# %% [markdown]
#
# - Die getestete Unit ist nicht isoliert
# - Wir verwenden die "echte" Klasse `Event`
#   - Damit wird z.B. auch die `reserve()`-Methode von `Event` getestet
#   - Bugs in der `reserve()` Methode führen zu Fehlern in diesem Test

# %% [markdown]
#
# ## Vorteile der Isolation der getesteten Unit
#
# - Einfache Struktur der Tests
#   - Jeder Test gehört zu genau einer Unit
# - Genaue Identifikation von Fehlern
# - Aufbrechen von Abhängigkeiten/des Objektgraphen

# %% [markdown]
#
# ## Nachteile der Isolation der getesteten Unit
#
# - Potenziell höherer Aufwand (z.B. Mocks)
# - Fehler in der Interaktion zwischen Units werden nicht gefunden
# - Verleiten zum Schreiben von "Interaktionstests"
# - **Risiko von Kopplung an Implementierungsdetails**
#
# ```python
# def purchase_tickets(self, event_name, num_tickets):
#     # Exception handling..., dict lookup for `event`
#     event.reserve(num_tickets)
#     return True
# ```

# %% [markdown]
#
# ## Empfehlung
#
# - Verwenden Sie isolierte Unit-Tests (Detroit School)
# - Isolieren Sie Abhängigkeiten, die "eine Rakete starten"
#   - nicht-deterministisch (z.B. Zufallszahlen, aktuelle Zeit, aktuelles Datum)
#   - langsam
#   - externe Systeme (z.B. Datenbank)
# - Isolieren Sie Abhängigkeiten, die ein komplexes Setup benötigen
