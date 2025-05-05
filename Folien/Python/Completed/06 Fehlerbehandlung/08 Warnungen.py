# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Warnungen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Das Warnungssystem in Python
#
# Warnungen, um robuste und wartbare Software zu schreiben

# %% [markdown]
#
# ## Was ist das `warnings`-Modul?
#
# - Signalisiert potenzielle Probleme oder Bedingungen, die *nicht* unbedingt
#   das Stoppen des Programms erfordern (im Gegensatz zu Ausnahmen).
# - Informiert Entwickler/Benutzer über nicht fatale Probleme:
#   - Veraltete ("deprecated") Funktionen.
#   - Potenziell problematische Verwendung.
#   - Veraltete Praktiken.
# - Standardverhalten: Gibt Nachrichten an `sys.stderr` aus und setzt die
#   Ausführung fort.
# - Konfigurierbar: Verhalten kann geändert werden (ignorieren, anzeigen,
#   protokollieren, als Fehler behandeln).

# %% [markdown]
#
# ## Warnungen vs. Ausnahmen
#
# - **Ausnahmen (`Exception`):**
#   - Signalisieren *Fehler* oder Bedingungen, die den normalen Betrieb
#     verhindern.
#   - *Stoppen* den Programmfluss, wenn sie nicht behandelt werden (z.B.
#     `TypeError`, `ValueError`).
#   - Erfordern eine explizite Behandlung (`try...except`), um ein elegantes
#     Scheitern zu ermöglichen.
# - **Warnungen (`Warning`):**
#   - Deuten auf *potenzielle* Probleme, veralteten Code, oder nicht
#     standardmäßige Verwendung hin.
#   - *Stoppen* den Programmfluss standardmäßig *nicht*.
#   - Bieten strukturierte, filterbare Warnungen.
# - **Vererbung:**
#   - `Warning` ist eine Unterklasse von `Exception`.
#   - Dies ermöglicht es, Warnungen *als* Fehler zu behandeln, wenn sie
#     entsprechend konfiguriert sind.

# %% [markdown]
#
# ## III. Wann Warnungen verwenden?
#
# - **Veraltete Funktionen:**
#   - Häufigster Anwendungsfall.
#   - Informiert Entwickler über bevorstehende API-Entfernungen
#     (`DeprecationWarning`, `PendingDeprecationWarning`).
#   - Ermöglicht einen sanften Übergang, ohne den Code sofort zu zerstören.
# - **Potenzielle Laufzeitprobleme:**
#   - Situationen, die *Probleme* verursachen *könnten* (z.B. numerische
#     Instabilität, Ressourcenprobleme).
#   - `RuntimeWarning`, `ResourceWarning`.
# - **Vorschläge für Alternativen/Beste Praktiken:**
#   - Hervorhebung ineffizienter oder nicht empfohlener Muster (`UserWarning`).
# - **Zweifelhafte Syntax/Importe:**
#   - Code, der gültig, aber potenziell falsch ist (`SyntaxWarning`,
#     `ImportWarning`).
# - **Warum nicht `print()`?**
#   - Warnungen sind filterbar, kategorisierbar, gehen standardmäßig an `stderr`
#     und enthalten Quellinformationen.

# %% [markdown]
#
# ## Workshop: Warnung oder Ausnahme?
#
# Entscheiden Sie für jedes Szenario, ob eine `Warning` oder eine `Exception`
# geeigneter ist:
#
# 1. Eine Funktion `calculate_average(numbers)` erhält eine leere Liste. Es
#    tritt eine Division durch Null auf.
# 2. Eine Bibliotheksfunktion `old_style_connect()` funktioniert weiterhin, wird
#    aber in zwei Versionen entfernt. Eine neue Funktion `connect()` wird
#    bevorzugt.
# 3. Eine Konfigurationsdatei ist lesbar, enthält jedoch eine Einstellung
#    (`timeout=0`), die in Grenzfällen zu unerwartetem Verhalten führen kann.
# 4. Eine Funktion `read_data(filename)` kann die angegebene Datei nicht finden.
# 5. Eine Funktion zur numerischen Simulation erkennt einen möglichen Verlust
#    der Genauigkeit aufgrund von Gleitkomma-Beschränkungen, aber die Berechnung
#    kann weiterhin abgeschlossen werden


# %% [markdown]
#
# ## Workshop 1: Lösungen
#
# 1.  **Ausnahme** (`ZeroDivisionError` oder `ValueError`): Die Operation kann
#      nicht erfolgreich abgeschlossen werden.
# 2.  **Warnung** (`DeprecationWarning`): Informieren Sie die Benutzer über die
#      Migration, aber lassen Sie vorhandenen Code weiterhin funktionieren.
# 3.  **Warnung** (`UserWarning` oder `RuntimeWarning`): Warnen Sie den Benutzer
#     vor einem potenziellen Problem, ohne das Programm zu stoppen.
# 4.  **Ausnahme** (`FileNotFoundError`): Die Funktion kann ihre Kernaufgabe
#     nicht ausführen.
# 5.  **Warnung** (`RuntimeWarning`): Signalisieren Sie ein potenzielles Problem,

# %% [markdown]
#
# ## Warnungen auslösen: `warnings.warn()`
#
# - `warnings.warn(message, category=UserWarning, stacklevel=1)`
# - `message`: Der Text der Warnung (String).
# - `category`: Der Typ der Warnung (Unterklasse von `Warning`). Standardmäßig
#   `UserWarning`.
# - `stacklevel`: Wichtig, um auf den Code des *Aufrufers* zu verweisen, nicht
#   auf die `warn()`-Zeile selbst.
#   - `stacklevel=1` (Standard): Verweist auf die Zeile, in der `warn()`
#     aufgerufen wird.
#   - `stacklevel=2`: Verweist auf die Zeile, die die Funktion mit `warn()`
#     aufgerufen hat.
#   - Passen Sie es je nach Tiefe des Aufrufstapels an.

# %%
import warnings


# %%
def risky_operation(value):
    if value < 0:
        # Default category (UserWarning), default stacklevel (1)
        warnings.warn("Negative value encountered!")
    # ... proceed...
    return value * 10


# %%
risky_operation(-5)

# %% [markdown]
#
# ### Die Bedeutung von `stacklevel`
#
# - Sorgen dafür, das hilfreiche Warnungen ausgegeben werden, insbesondere bei
#   `DeprecationWarning`.

# %%
import warnings


# %%
def new_function(arg):
    print(f"Using new function with {arg}")
    return arg * 2


# %%
def old_deprecated_function(arg):
    # stacklevel=1 (default) points HERE - less helpful
    # warnings.warn("Use new_function() instead", DeprecationWarning, stacklevel=1)
    # stacklevel=2 points to the CALLER - more helpful!
    warnings.warn("Use new_function() instead", DeprecationWarning, stacklevel=2)
    return new_function(arg)


# %%
old_deprecated_function(10)  # Warning should point HERE

# %% [markdown]
#
# - `stacklevel=2` identifiziert korrekt die Zeile, die die veraltete Funktion
#   aufruft.

# %% [markdown]
#
# ## Workshop: Auslösen einer Warnung vor Veraltung (Deprecation Warning)
#
# 1. Erstellen Sie eine Funktion `old_printer(text)`, die den gegebenen `text`
#    ausgibt.
# 2. Geben Sie innerhalb von `old_printer` eine `DeprecationWarning` aus, die
#    besagt, dass `new_printer(text)` stattdessen verwendet werden sollte.
# 3. Stellen Sie sicher, dass die Warnmeldung korrekt auf die Zeile verweist,
#    die `old_printer` *aufruft*, nicht auf die Zeile `warnings.warn` selbst.
# 4. Rufen Sie `old_printer("Hallo")` auf und beobachten Sie die
#    Warnungsausgabe.

# %%
import warnings


# %%
def old_printer(text):
    warnings.warn(
        "'old_printer' is deprecated, use 'new_printer' instead.",
        DeprecationWarning,
        stacklevel=2,  # Point to the caller
    )
    print(f"Old printer: {text}")


# %%
old_printer("Hello Deprecation!")

# %% [markdown]
#
# ## Warnungskategorien
#
# - Warnungen sind in Kategorien organisiert (Klassen, die von `Warning` erben).
# - Ermöglicht selektives Filtern.
# - **Eingebaute Kategorien**:
#   - `Warning`: Basisklasse.
#   - `UserWarning`: Standard für `warn()`; Probleme im Benutzercode.
#   - `DeprecationWarning`: Für Entwickler; veraltete Funktionen (oft
#     standardmäßig ignoriert).
#   - `PendingDeprecationWarning`: Zukünftige Veraltung (standardmäßig
#     ignoriert).
#   - `RuntimeWarning`: Zweifelhafte Laufzeitverhalten (z.B. numerische
#     Probleme).
#   - `SyntaxWarning`: Zweifelhafte Syntax (z.B. `is` mit Literalen).
#   - `ImportWarning`: Probleme beim Import (standardmäßig ignoriert).
#   - `BytesWarning`: Probleme mit `bytes`/`bytearray` vs `str` (standardmäßig
#      ignoriert).
#   - `ResourceWarning`: Mögliche Ressourcenlecks (z.B. nicht geschlossene
#      Dateien) (standardmäßig ignoriert).
# - **Benutzerdefinierte Kategorien:** Definieren Sie Ihre eigenen, indem Sie
#   `Warning` oder andere Klassen erweitern.


# %% [markdown]
#
# ## Warnungskategorien: Beispiele

# %%
import warnings


# %%
def check_config(settings):
    if settings.get("legacy_mode", False):
        warnings.warn(
            "Legacy mode is active and may be removed soon.",
            FutureWarning, # Target end-users
            stacklevel=2
        )
    if settings.get("precision", "high") == "low":
        warnings.warn(
            "Low precision setting may impact results.",
            RuntimeWarning, # Dubious runtime behavior
            stacklevel=2
        )
    print("Config checked.")


# %%
config1 = {"legacy_mode": True, "precision": "high"}
print("Checking config1...")
check_config(config1)

# %%
config2 = {"precision": "low"}
print("Checking config2...")
check_config(config2)

# %% [markdown]
#
# ### Workshop: Verwendung spezifischer Kategorien
#
# 1. Schreiben Sie eine Funktion `process_data(data, version)`, die ein
#    Dictionary `data` und eine Versionsnummer `version` erhält.
# 2. Wenn `version < 2`, geben Sie eine `DeprecationWarning` aus, dass Versionen
#    unter 2 veraltet sind und die Unterstützung enden wird. Verwenden Sie
#    `stacklevel=2`.
# 3. Wenn das `data`-Dictionary einen erforderlichen Schlüssel `'id'` fehlt,
#    geben Sie eine `RuntimeWarning` aus, dass der Schlüssel fehlt, aber
#    versucht wird, mit der Ausführung fortzufahren. Verwenden Sie
#    `stacklevel=2`.
# 4. Rufen Sie die Funktion mit verschiedenen Eingaben auf, um jede Warnung
#    auszulösen.


# %%
import warnings


# %%
def process_data(data, version):
    print(f"Processing data with version {version}...")
    if version < 2:
        warnings.warn(
            f"Version {version} is deprecated. Use version 2 or higher.",
            DeprecationWarning,
            stacklevel=2,
        )

    if "id" not in data:
        warnings.warn(
            "Required key 'id' missing in data. Attempting to proceed.",
            RuntimeWarning,
            stacklevel=2,
        )
    # ... actual data processing logic...
    print("Processing complete.")


# %%
print("Test Case 1: Deprecated Version")
process_data({"id": 123, "value": "abc"}, version=1)

# %%
print("Test Case 2: Missing ID")
process_data({"value": "xyz"}, version=2)

# %%
print("Test Case 3: Both Warnings")
process_data({"value": "xyz"}, version=1)

# %%
print("Test Case 4: No Warnings")
process_data({"id": 456, "value": "def"}, version=3)

# %% [markdown]
#
#  ## Warnungen kontrollieren: Die Filter
#
# - Python verwendet einen **Warnungsfilter**: eine geordnete Liste von Regeln.
# - Jede Warnung wird gegen die Regeln überprüft; das *erste Match* bestimmt die
#   Aktion.

# %% [markdown]
#
# - **Filterregel:** `(action, message, category, module, lineno)`.
#   - `action`: Was zu tun ist (String).
#   - `message`: Regex, die den Anfang der Warnmeldung matcht
#     (case-insensitive).
#   - `category`: Warnungsklasse, die gematcht werden soll (z.B. `UserWarning`).
#   - `module`: Regex, die den Modulnamen matcht (case-sensitive).
#   - `lineno`: Zeilennummer, die gematcht werden soll (0 für beliebig).

# %% [markdown]
#
# - **Aktionen**:
#   - `"ignore"`: Unterdrückt die Warnung.
#   - `"error"`: Wandelt die Warnung in eine Ausnahme um.
#   - `"always"`: Gibt die Warnung immer aus (überschreibt Unterdrückung von
#     Duplikaten).
#   - `"default"`: Gibt das erste Vorkommen pro Ort (Modul+Zeile) aus.
#   - `"module"`: Gibt das erste Vorkommen pro Modul aus.
#   - `"once"`: Gibt nur das allererste Vorkommen global aus.

# %% [markdown]
#
# ## Warnungen kontrollieren: Filtereinstellungen
#
# - **In Code:**
#   - `warnings.simplefilter(...)`: Einfache Filterung nach Kategorie/Zeile.
#   - `warnings.filterwarnings(...)`: Komplexere Filterung mit Regex für
#     Nachricht/Modul.
#   - `warnings.resetwarnings()`: Setzt Filter auf den Standardzustand zurück.

# %% [markdown]
#
# - **In der Befehlszeile (`-W`):**
#   - `python -W action:message:category:module:lineno script.py`.
#   - Teile können weggelassen werden. `message`/`module` sind hier literale
#      Substrings.
#   - Beispiele:
#     - `python -W ignore script.py`,
#     - `python -W error::RuntimeWarning script.py`.

# %% [markdown]
#
# - **Umgebungsvariable (`PYTHONWARNINGS`):**
#   - Komma-separierte Liste von Filter-Strings (wie `-W`-Argumente).
#   - `export PYTHONWARNINGS="ignore,error::ResourceWarning"`.

# %% [markdown]
#
# - **Kontextmanager (`catch_warnings`):**
#   - Temporäre Modifikation der Filter innerhalb eines `with`-Blocks.
#   - Ursprüngliche Filter werden beim Verlassen wiederhergestellt.
#   - `with warnings.catch_warnings(record=True) as w:`: Sammelt Warnungen in
#      Liste `w` (z.B. für Tests).
#
#

# %% [markdown]
#
# ## Beispiele für Filterung

# %%
import warnings

# %%
def func_a():
    warnings.warn("Warning from func_a", UserWarning, stacklevel=2)

# %%
def func_b():
    warnings.warn("Deprecated feature in func_b", DeprecationWarning, stacklevel=2)

# %% [markdown]
#
# Default-Verhalten:

# %%
func_a()

# %%
func_b()

# %% [markdown]
#
# Behandeln von `UserWarning` als Fehler:

# %%
warnings.simplefilter('error', UserWarning)

# %%
try:
    func_a()
except UserWarning as e:
    print(f"Caught UserWarning: {e}")

# %% [markdown]
#
# Ignorieren einer bestimmten `DeprecationWarning`-Nachricht:

# %%
warnings.resetwarnings()  # Reset for next example

# %%
warnings.filterwarnings('ignore', message=".*Deprecated feature.*", category=DeprecationWarning)

# %%
func_b() # This specific warning should now be ignored

# %% [markdown]
#
# Verwenden von `catch_warnings` zum Ignorieren einer Warnung:

# %%
warnings.resetwarnings() # Reset for next example


# %%
with warnings.catch_warnings():
    warnings.simplefilter("ignore", UserWarning)
    print("Inside context manager:")
    func_a() # Should be ignored here
print("Outside context manager:")
func_a() # Should appear again

# %% [markdown]
#
# Verwenden von `catch_warnings` zum Aufzeichnen von Warnungen:

# %%
with warnings.catch_warnings(record=True) as captured:
    warnings.simplefilter("always") # Make sure warnings are captured
    func_a()
    func_b()
    print(f"Captured {len(captured)} warnings.")
    for w in captured:
        print(f"- {w.category.__name__}: {w.message}")

# %% [markdown]
#
# ## Workshop: Filtern und Abfangen
#
# 1. Definieren Sie zwei Funktionen:
#    - `calculate_old(x)`: Gibt eine `DeprecationWarning` ("Use calculate_new")
#       mit `stacklevel=2` aus.
#    - `check_value(v)`: Gibt eine `RuntimeWarning` ("Value might be unstable")
#       aus, wenn `v > 100`, mit `stacklevel=2`.
# 2. **Teil A (Filtern):**
#    - Rufen Sie beide Funktionen auf.
#    - Fügen Sie Code hinzu, der `warnings.simplefilter` oder
#      `warnings.filterwarnings` verwendet, um:
#       - `RuntimeWarning` in einen Fehler zu verwandeln.
#       - Sicherzustellen, dass die `DeprecationWarning` *immer* angezeigt wird
#         (sie könnte standardmäßig ignoriert werden).
#    - Rufen Sie die Funktionen erneut innerhalb eines `try...except
#      RuntimeWarning`-Blocks auf.
# 3. **Teil B (Abfangen):**
#    - Setzen Sie die Warnfilter zurück (`warnings.resetwarnings()`).
#    - Verwenden Sie `warnings.catch_warnings(record=True)`, um beide Funktionen
#      (`calculate_old(10)` und `check_value(150)`) aufzurufen.
#    - Stellen Sie sicher, dass genau zwei Warnungen erfasst wurden.
#    - Geben Sie die Kategorie und die Nachricht jeder erfassten Warnung aus.

# %%
import warnings

# %%
def calculate_old(x):
    warnings.warn("Use calculate_new", DeprecationWarning, stacklevel=2)
    return x * 0.9


# %%
def check_value(v):
    if v > 100:
        warnings.warn("Value might be unstable", RuntimeWarning, stacklevel=2)
    return True


# %% [markdown]
#
# ### Teil A: Filterung

# %%
print("Initial calls:")
calculate_old(10)
check_value(150)

# %%
print("\nConfiguring filters...")
# Ensure DeprecationWarning is shown
warnings.simplefilter("always", DeprecationWarning)
# Turn RuntimeWarning into an error
warnings.simplefilter("error", RuntimeWarning)

# %%
print("Calling with filters active:")
try:
    calculate_old(10)
    check_value(150)  # This should raise RuntimeWarning
    print("RuntimeWarning was NOT raised as error!")
except RuntimeWarning as e:
    print(f"Successfully caught RuntimeWarning: {e}")
except Exception as e:
    print(f"Caught unexpected exception: {e}")

# %% [markdown]
#
# ### Teil B: Abfangen

# %%
warnings.resetwarnings()  # Reset filters from Part A

# %%
print("Calling within catch_warnings(record=True):")
with warnings.catch_warnings(record=True) as captured_warnings:
    # Optional: ensure warnings aren't ignored by default filters inside context
    warnings.simplefilter("default")  # Or 'always'

    calculate_old(10)
    check_value(150)

    print(f"Captured {len(captured_warnings)} warnings.")

    # Assertion (in real code, use testing framework like pytest)
    if len(captured_warnings) != 2:
        raise ValueError(f"Expected 2 warnings, but captured {len(captured_warnings)}")
    else:
        print("Assertion successful: Captured 2 warnings.")

    for w in captured_warnings:
        print(f"- Category: {w.category.__name__}, Message: {w.message}")

# %% [markdown]
#
# ## Fortgeschrittene Themen & Best Practices
#
# - **Anpassen der Ausgabe:**
#   - Ersetzen Sie `warnings.showwarning(...)`, um zu ändern, *wie/wo* Warnungen
#     angezeigt werden (z.B. an Logger senden).
#   - Ersetzen Sie `warnings.formatwarning(...)`, um das *Nachrichtenformat* zu
#     ändern.
# - **Testen (`pytest`):**
#   - `pytest` erfasst automatisch Warnungen.
#   - Verwenden Sie `pytest.warns(ExpectedWarning, match='regex')`-Kontextmanager,
#     um spezifische Warnungen zu überprüfen.
#   - `recwarn`-Fixture zeichnet alle Warnungen in einem Test auf.
#   - `pytest` hat eigene Filterung (`-W`, `pytest.ini`, `@pytest.mark.filterwarnings`).
# - **Protokollierungsintegration:**
#   - `logging.captureWarnings(True)` leitet die Ausgabe des Warnmoduls an das
#     `logging`-System um (Logger `py.warnings`, Ebene `WARNING`).
#   - Zentralisiert Diagnosen, ermöglicht persistente Protokollierung.

# %% [markdown]
#
# ### Testen mit `pytest.warns`

# %% [markdown]
#
# ```python
# # my_module.py
# import pytest
# import warnings
#
# def calculate_old(x):
#     warnings.warn("Use calculate_new", DeprecationWarning, stacklevel=2)
#     return x * 0.9
#
# def check_value(v):
#     if v > 100:
#         warnings.warn("Value might be unstable", RuntimeWarning, stacklevel=2)
#     return True
#
# # ...
# ```

# %% [markdown]
#
# ```python
# # test_my_module.py
#
# def test_calculate_old_warns():
#     """Verify calculate_old issues the correct DeprecationWarning."""
#     with pytest.warns(DeprecationWarning, match="Use calculate_new"):
#         calculate_old(50)
#
# def test_check_value_warns_if_high():
#     """Verify check_value issues RuntimeWarning for high values."""
#     with pytest.warns(RuntimeWarning, match="unstable"):
#         check_value(200)
# ```

# %% [markdown]
#
# ```python
# def test_check_value_does_not_warn_if_low():
#     """Verify check_value issues NO warning for low values."""
#     with warnings.catch_warnings(record=True) as captured:
#         # Ensure warnings aren't filtered out by other settings during test
#         warnings.simplefilter("always")
#         check_value(50)
#         # Assert no warnings were captured
#         assert len(captured) == 0, f"Expected no warnings, got {len(captured)}"
# ```

# %% [markdown]
#
# ## Best Practices
#
# - **Wählen Sie die richtige Kategorie:**
#   - Verwenden Sie den spezifischsten, semantisch korrekten Warnungstyp
#     (`DeprecationWarning`, `RuntimeWarning` usw.).
# - **Setzen Sie `stacklevel` korrekt:**
#   - Stellen Sie sicher, dass Warnungen auf den Code des Benutzers und nicht
#     auf interne Bibliothekszeilen verweisen.
# - **Schreiben Sie klare Nachrichten:**
#   - Erklären Sie das Problem und schlagen Sie Alternativen vor, wenn möglich.
# - **Dokumentieren Sie benutzerdefinierte Warnungen:**
#   - Wenn Sie benutzerdefinierte Kategorien erstellen, dokumentieren Sie diese.
# - **Testen Sie Ihre Warnungen:**
#   - Verwenden Sie `pytest.warns` oder `catch_warnings`, um zu überprüfen, ob
#     Warnungen korrekt ausgegeben werden.
# - **Behandeln Sie Warnungen in Entwicklung/CI:**
#   - Ignorieren Sie Warnungen nicht blind. Untersuchen Sie diese.
#  - Ziehen Sie in Betracht, `-W error` in CI für kritische Warnungstypen zu
#    verwenden.
# - **Verwenden Sie die Protokollierungsintegration:**
#   - Für bessere Überwachung in Anwendungen leiten Sie Warnungen an Ihr
#     Protokollierungssystem (Log) weiter.

# %% [markdown]
#
# ## Zusammenfassung
#
# - Das `warnings`-Modul ist ein leistungsstarkes Werkzeug für nicht-kritische
#   Kommunikation.
# - Unterscheidet sich von Ausnahmen, ist aber über Vererbung verbunden
#   (`Warning` ist eine Unterklasse von `Exception`).
# - Essentiell für die Evolution von Bibliotheken (Veraltung) und zur
#   - Hervorhebung potenzieller Probleme.
# - Hochgradig konfigurierbare Filterung ermöglicht maßgeschneidertes Verhalten
#   für verschiedene Umgebungen.
# - Integriert sich gut mit Test- (`pytest`) und Protokollierungsframeworks.
# - **Wichtigste Erkenntnis:** Verwenden Sie Warnungen durchdacht, konfigurieren
#   Sie sie angemessen und achten Sie während der Entwicklung darauf!
