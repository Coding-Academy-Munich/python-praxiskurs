# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Aufräumarbeiten mit Finally</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Aufräumarbeiten mit `finally`
#
# - Manchmal ist es nötig, Anweisungen auszuführen, egal ob eine Ausnahme ausgelöst
#   wurde, oder nicht
# - Z.B. wenn Betriebssystem-Ressourcen angefordert wurden, die freigegeben werden
#   müssen

# %%
def process_data_from_file(file_name):  # type: ignore
    print(f"Opening file {file_name}")
    try:
        print(f"Processing data from {file_name}...")
        if file_name == "bad.data":
            raise ValueError("Bad data! But recoverable.")
        if file_name == "worse.data":
            raise TypeError("Very bad data! Cannot recover.")
        print("Done.")
    except ValueError as err:
        print(err)
    finally:
        print(f"Closing {file_name}.")


# %%
process_data_from_file("good.data")

# %%
# process_data_from_file("bad.data")

# %%
# process_data_from_file("worse.data")

# %% [markdown]
#
# ## Mini-Workshop: Freigeben von Ressourcen
#
# Ihr Programm enthält die folgende Klasse, die eine Datenbankverbindung repräsentiert:


# %%
class Database:
    def __init__(self):
        self.id = f"db-{id(self) % 100}"
        self.connected = False

    def connect(self):
        print(f"Connecting to database {self.id}.")
        self.connected = True

    def disconnect(self):
        print(f"Disconnecting from database {self.id}.")
        self.connected = False

    def read_data(self):
        if self.connected:
            print(f"Reading data from database {self.id}.")
        else:
            raise RuntimeError("Not connected to database.")


# %% [markdown]
#
# Ihre Anwendung verwendet die Datenbank in einer Funktion `process_data(db: Database)`:

# %%
def process_data(db: Database):
    print(f"Processing data with database {db.id}.")
    db.read_data()


# %% [markdown]
#
# Da Datenbankverbindungen viele Ressourcen in der verwendeten Datenbank belegen, muss
# die Verbindung nach ihrer Verwendung wieder mit `disconnect()` freigegeben werden.
#
# Einer Ihrer Kollegen hat versucht das Problem folgendermaßen zu lösen:

# %%
def our_great_app():
    db = Database()
    db.connect()
    process_data(db)
    db.disconnect()


# %% [markdown]
#
# Nach einer Änderung der `process_data()` Funktion kommt es immer wieder
# vor, dass Ihr Programm die Datenbankverbindung nicht freigibt.
#
# - Welche Änderung kann zu diesem Verhalten geführt haben?
# - Ändern Sie `process_data()` entsprechend ab, und Testen Sie, dass
#   die Datenbankverbindung wirklich nicht freigegeben wird:


# %%
def process_data(db: Database):  # noqa
    print(f"Processing data with database {db.id}.")
    # db.read_data()
    raise ValueError("Error reading Data!")


# %%
# our_great_app()


# %% [markdown]
#
# - Modifizieren Sie `our_great_app()` so, dass dieser Fehler vermieden wird.
# - Implementieren Sie die Lösung so, dass sie das Problem auch bei zukünftigen
#   Änderungen vermeiden.
# - Testen Sie, dass die Datenbankverbindung jetzt wirklich freigegeben wird.

# %%
def our_great_app():  # noqa
    db = Database()
    db.connect()
    try:
        process_data(db)
    finally:
        db.disconnect()


# %%
# our_great_app()
