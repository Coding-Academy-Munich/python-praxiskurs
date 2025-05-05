# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Test Doubles</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Test Doubles
#
# - Test Double: Vereinfachte Version einer Abhängigkeit im System
#   - z.B. Ersetzen einer Datenbankabfrage durch einen fixen Wert
# - Test Doubles sind wichtig zum Vereinfachen von Tests
# - Sie benötigen typischerweise ein Interface, das sie implementieren
# - Aber: zu viele oder komplexe Test Doubles machen Tests unübersichtlich
#   - Was wird von einem Test eigentlich getestet?

# %% [markdown]
#
# ## Arten von Test Doubles
#
# - Ausgehende Abhängigkeiten ("Mocks")
#   - Mocks
#   - Spies
# - Eingehende Abhängigkeiten ("Stubs")
#   - Dummies
#   - Stubs
#   - Fakes

# %% [markdown]
#
# ## Dummy
#
# - Objekt, das nur als Platzhalter dient
# - Wird übergeben, aber nicht verwendet
# - In Python manchmal `None`
# - Auch für ausgehende Abhängigkeiten

# %% [markdown]
#
# ## Stub
#
# - Objekt, das eine minimale Implementierung einer Abhängigkeit bereitstellt
# - Gibt typischerweise immer den gleichen Wert zurück
# - Wird verwendet um
#  - komplexe Abhängigkeiten zu ersetzen
#  - Tests deterministisch zu machen

# %% [markdown]
#
# ## Fake
#
# - Objekt, das eine einfachere Implementierung einer Abhängigkeit bereitstellt
# - Kann z.B. eine In-Memory-Datenbank sein
# - Wird verwendet um
#   - Tests zu beschleunigen
#   - Konfiguration von Tests zu vereinfachen

# %% [markdown]
#
# ## Spy
#
# - Objekt, das Informationen über die Interaktion mit ihm speichert
# - Wird verwendet um
#   - zu überprüfen, ob eine Abhängigkeit korrekt verwendet wird

# %% [markdown]
#
# ## Mock
#
# - Objekt, das Information über die erwartete Interaktion speichert
# - Typischerweise deklarativ konfigurierbar
# - Automatisierte Implementierung von Spies
# - Wird verwendet um
#   - zu überprüfen, ob eine Abhängigkeit korrekt verwendet wird

# %%
from abc import ABC, abstractmethod

# %%
class DataSource(ABC):
    @abstractmethod
    def get_value(self) -> int:
        ...

# %%
class DataSink(ABC):
    @abstractmethod
    def set_value(self, value: int) -> None:
        ...

# %%
class Processor:
    def __init__(self, source: DataSource, sink: DataSink) -> None:
        self.source = source
        self.sink = sink

    def process(self) -> None:
        value = self.source.get_value()
        self.sink.set_value(value)

# %%
class DataSourceStub(DataSource):
    def get_value(self) -> int:
        return 42


# %%
class DataSinkSpy(DataSink):
    def __init__(self):
        self.values = []

    def set_value(self, value: int) -> None:
        self.values.append(value)

# %%
def test_processor():
    source = DataSourceStub()
    sink = DataSinkSpy()
    processor = Processor(source, sink)

    processor.process()

    assert len(sink.values) == 1
    assert sink.values[0] == 42
    print("Test passed")


# %%
test_processor()

# %% [markdown]
#
# ## Typischer Einsatz von Test Doubles
#
# - Zugriff auf Datenbank, Dateisystem
# - Zeit, Zufallswerte
# - Nichtdeterminismus
# - Verborgener Zustand

# %% [markdown]
#
# ## Workshop: Test Doubles
#
# Wir haben die folgenden Interfaces, die von der Funktion `test_me()`
# verwendet werden:

# %%
class Service1(ABC):
    @abstractmethod
    def get_value(self) -> int:
        ...

# %%
class Service2(ABC):
    @abstractmethod
    def set_value(self, value: int) -> None:
        ...

# %%
def test_me(i: int, j: int, service1: Service1, service2: Service2) -> None:
    value = 0
    if i > 0:
        value = service1.get_value()
    if j > 0:
        service2.set_value(value)

# %% [markdown]
#
# Welche Arten von Test-Doubles brauchen Sie um die Funktion `test_me()` für
# die angegebenen Werte von `i` und `j` zu testen?
#
# | i | j | Service1 | Service2 |
# |---|---|----------|----------|
# | 0 | 0 |          |          |
# | 0 | 1 |          |          |
# | 1 | 0 |          |          |
# | 1 | 1 |          |          |

# %% [markdown]
#
# | i | j | Service1 | Service2 |
# |---|---|----------|----------|
# | 0 | 0 | Dummy    | Dummy    |
# | 0 | 1 | Dummy    | Spy/Mock |
# | 1 | 0 | Stub     | Dummy    |
# | 1 | 1 | Stub     | Spy/Mock |

# %% [markdown]
#
# Implementieren Sie die entsprechenden Doubles und schreiben Sie die Tests

# %%
class Service1Stub(Service1):
    def get_value(self) -> int:
        return 42

# %%
class Service2Spy(Service2):
    def __init__(self):
        self.values = []

    def set_value(self, value: int) -> None:
        self.values.append(value)

# %%
def test_test_me_0_0():
    test_me(0, 0, None, None) # type: ignore
    print("Test passed")

# %%
test_test_me_0_0()

# %%
def test_test_me_0_1():
    service2 = Service2Spy()
    test_me(0, 1, None, service2) # type: ignore
    assert len(service2.values) == 1
    assert service2.values[0] == 0
    print("Test passed")

# %%
test_test_me_0_1()


# %%
def test_test_me_1_0():
    service1 = Service1Stub()
    test_me(1, 0, service1, None) # type: ignore
    print("Test passed")

# %%
test_test_me_1_0()


# %%
def test_test_me_1_1():
    service1 = Service1Stub()
    service2 = Service2Spy()
    test_me(1, 1, service1, service2)
    assert len(service2.values) == 1
    assert service2.values[0] == 42
    print("Test passed")

# %%
test_test_me_1_1()
