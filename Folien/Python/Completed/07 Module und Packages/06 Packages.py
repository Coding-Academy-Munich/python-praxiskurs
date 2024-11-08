# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Packages</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# Packages (Pakete) erlauben es uns, verwandte Module zu organisieren

# %% [markdown]
#
# ### Beispiel: `html` Paket
#
# - `html` enthält Module, die für die Verarbeitung von HTML Dokumenten benötigt
#   werden
# - `html.entities` enthält eine Liste von HTML Entities
# - `html.parser` enthält einen HTML-Parser
# - `html` selber enthält nur Funktionen `escape()` und `unescape()`

# %%
import html

# %%
html.escape("<a href='test'>Test</a>")

# %%
html.unescape("&lt;a href=&#x27;test&#x27;&gt;Test&lt;/a&gt;")

# %%
import html.entities

# %%
html.entities.entitydefs["Psi"]

# %%
html.entities.html5["Psi;"]

# %%
from html.parser import HTMLParser


# %%
class PrintingHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag:  ", tag)

    def handle_data(self, data):
        print("Data:     ", data)


# %%
parser = PrintingHTMLParser()

# %%
parser.feed('<div class="my-class"><a href="test">Test</a></div>')


# %% [markdown]
#
#  ### Struktur von Packages
#
# - Packages sind Ordner im Dateisystem
# - Sie können Module und andere Packages enthalten
# - Um zu kennzeichnen, dass ein Ordner ein Package ist, enthält er typischerweise eine
#   `__init__.py` Datei
# - Die `__init__.py` Datei kann leer sein (und ist oft leer)

# %%
from dirtree import dir_tree

# %%
dir_tree("greetings")

# %% [markdown]
#
# ### Struktur des `greetings` Packages
#
# - Dateien für Module:
#   - [`formal.py`](greetings/formal.py)
#   - [`informal.py`](greetings/informal.py)
#   - [`generic.py`](greetings/generic.py)
# - Ordner für Sub-Packages:
#   - `intl` mit Datei [`generic.py`](greetings/intl/generic.py)

# %% [markdown]
#
# ## Namen von Packages
#
# - Namenskomponenten werden durch Punkte getrennt
#   - z.B. `<package>.<sub-package>.<sub-sub-package>.<module>`
# - Namenskonventionen:
#   - Namen sollten mit einem Kleinbuchstaben beginnen
#   - Namen sollten keine Unterstriche enthalten

# %% [markdown]
#
# ### Namen des `greetings` Packages
#
# - Dateien für Module:
#   - [`greetings.formal`](greetings/formal.py)
#   - [`greetings.generic`](greetings/generic.py)
#   - [`greetings.informal`](greetings/informal.py)
# - Ordner für Sub-Packages:
#   - `intl` mit Modul [`greetings.intl.generic`](greetings/intl/generic.py)

# %%
import greetings.formal

# %%
greetings.formal.say_greetings("John")

# %%
from greetings import informal

# %%
informal.say_hi("John")

# %%
from greetings.generic import say_hello, greet

# %%
say_hello("John")

# %%
greet("John")

# %%
greet("Judy")

# %%
greet("Mrs. Brown")

# %%
import greetings.intl.generic

# %%
greetings.intl.generic.say_hello("John", "de")

# %%
import greetings.intl.generic as gg

# %%
gg.say_hello("John", "de")

# %%
gg.say_hello("John", "pt")

# %% [markdown]
#
#  ### Finden von Packages
#
#  - Python sucht in `sys.path` nach dem Package-Verzeichnis.
#  - Dieser kann durch die Environment-Variable `PYTHONPATH` oder direkt von
#    Python aus beeinflusst werden.
#  - In den meisten Fällen ist es besser, keine komplizierten Operationen an
#    `sys.path` vorzunehmen.

# %%
import sys

# %%
sys.path

# %% [markdown]
#
#  ### Das `import` statement
#
#  `import a.b.c`:
#
#  - `a` und `b` müssen Packages (Verzeichnisse) sein
#  - `c` kann ein Modul oder ein Package sein
#
#  `from a.b.c import d`
#  - `a` und `b` müssen Packages sein
#  - `c` kann ein Modul oder ein Package sein
#  - `d` kann ein Modul, ein Package oder ein Name (d.h. eine Variable, eine Funktion,
#    eine Klasse, usw.) sein

# %% [markdown]
#
#  ### Referenzen innerhalb eines Packages
#
#  - `from . import a` importiert `a` aus dem aktuellen Package
#  - `from .. import a` importiert `a` aus dem übergeordneten Package
#  - `from .foo import a` importiert `a` aus dem "Geschwistermodul" `foo`

# %%
# %pycat greetings/generic.py

# %%
# %pycat greetings/intl/generic.py

# %% [markdown]
#
# ## Workshop: Persönlicher Finanz-Tracker
#
# ### Übersicht
#
# In diesem Workshop werden Sie einen einfachen persönlichen Finanz-Tracker
# entwickeln. Dieses Programm hilft den Benutzern, ihre persönlichen Finanzen,
# einschließlich Ausgaben und Einkommen, zu verfolgen und zu analysieren. Ihre Aufgabe
# wird es sein, diese Anwendung in Pakete und Module zu strukturieren, um eine
# ordnungsgemäße Funktionalität zu gewährleisten und Ihr Verständnis von
# Python-Paketverwaltung und Modulreferenzen zu demonstrieren.


# %% [markdown]
#
# ### Problem- und Funktionsdomäne
#
# Der persönliche Finanz-Tracker besteht aus zwei Hauptkomponenten: Ausgabenverfolgung
# und Einkommensverfolgung. Zusätzlich wird er Funktionen für das Generieren von
# Finanzberichten und das Erstellen von Budgets haben.
#
# **Schlüsselfunktionalitäten:**
#
# 1. **Ausgaben verfolgen:** Einzelne Ausgaben aufzeichnen und kategorisieren.
# 2. **Einkommen verfolgen:** Verschiedene Einkommensquellen aufzeichnen und
#    kategorisieren.
# 3. **Berichte generieren:** Zusammenfassungen von Finanzaktivitäten erstellen.
# 4. **Budgetanalyse:** Ausgaben und Einkommen vergleichen, um Budgets zu setzen und
#    zu analysieren.

# %% [markdown]
#
# ### Paket- und Modulstruktur
#
# Ihr Programm wird in zwei Hauptpakete unterteilt: `finance` und `analytics`. Jedes
# Paket enthält spezifische Module, die mit ihren Funktionalitäten verbunden sind.
#
# 1. **Paket: `finance`**
#    - **Modul: `expenses.py`**
#      - Funktionen zum Hinzufügen, Kategorisieren und Zusammenfassen von Ausgaben.
#    - **Modul: `income.py`**
#      - Funktionen zum Aufzeichnen und Kategorisieren von Einkommensquellen.
#
# 2. **Paket: `analytics`** (ein Unter-Paket innerhalb von `finance`)
#    - **Modul: `reports.py`**
#      - Funktionen zum Erstellen von Finanzberichten basierend auf Einkommen und
#        Ausgaben.
#    - **Modul: `budget.py`**
#      - Funktionen zum Erstellen und Analysieren von Budgets.

# %% [markdown]
#
# ### Spezifikationen von Funktionen und Klassen
#
# - `expenses.py`:
#   - `add_expense()`
#   - `categorize_expense()`
#   - `summarize_expenses()`
#
# - `income.py`:
#   - `record_income()`
#   - `categorize_income()`
#
# - `reports.py`:
#   - `generate_financial_report()`
#
# - `budget.py`:
#   - `create_budget()`
#   - `compare_budget_to_actual()`

# %% [markdown]
#
# ### Paketreferenzen und Abhängigkeiten
#
# Realisieren Sie die folgenden Abhängigkeiten zwischen den Paketen und Modulen:
#
# - `budget.py` sollte sowohl auf `expenses.py` als auch auf `income.py` zugreifen
#   können, um alle Daten für die Budgetanalyse zu erhalten.
# - `reports.py` sollte auf `budget.py` zugreifen können, um Budgetanalysen in
#   Finanzberichte aufzunehmen.
# - `reports.py` sollte auf die Funktion `summarize_expenses()` in `expenses.py`
#   zugreifen können, um Ausgaben in Finanzberichten zu berücksichtigen.
#
# *Hinweis:* Die Abhängigkeiten zwischen den Modulen dienen dazu, die verschiedenen
# Import-Möglichkeiten zu demonstrieren. Sie sind nicht unbedingt das beste Beispiel för
# die Organisation von Funktionalität


# %% [markdown]
#
# ### Programm
#
# Legen Sie eine Datei `main.py` an, die folgendes Budget erzeugt:
#
# ```python
# incomes = [
#     record_income(5000, "Salary"),
#     record_income(200, "Interest"),
# ]
# expenses = [
#     add_expense(100, "Groceries"),
#     add_expense(150, "Utilities"),
#     add_expense(200, "Rent"),
# ]
# ```
#
# Verwenden Sie die Funktionen `generate_financial_report()` und
# `compare_budget_to_actual()` um einen Finanzbericht zu erstellen und das Budget zu
# analysieren.
#
# Stellen Sie sicher, dass die Funktionalität nur ausgeführt wird, wenn `main.py` direkt
# ausgeführt wird (d.h. nicht, wenn das Modul `main` importiert wird).

# %%
# !python -m finance.main

# %%
# import finance.main

# %% [markdown]
#
# ### Workshop-Ziel
#
# Ihre Aufgabe ist es, diese Module und Funktionen zu implementieren und dabei die
# angegebene Struktur einzuhalten. Dabei sollten Sie sicherstellen, dass:
#
# - Jedes Modul die angegebenen Funktionen oder Klassen enthält.
# - Richtige Verweise zwischen den Modulen verwendet werden, um auf notwendige
#   Funktionen anderer Module zuzugreifen.
# - Zyklische Abhängigkeiten vermieden werden, um eine klare und effiziente
#   Code-Struktur zu erhalten.
#
# **Hinweis:** Da der Fokus dieses Workshops auf der Strukturierung von Paketen und
# Modulen liegt, müssen Sie die Funktionen nicht vollständig implementieren. Sie
# können stattdessen Platzhalter verwenden, um die Funktionalität zu simulieren.

# %% [markdown]
#
# ### Erwartetes Ergebnis
#
# Am Ende dieses Workshops werden Sie einen grundlegenden, aber funktionalen
# Persönlichen Finanz-Tracker haben. Dieses Projekt wird Ihre Fähigkeit demonstrieren,
# eine Python-Anwendung in logische Pakete und Module zu strukturieren,
# Inter-Modul-Abhängigkeiten zu verwalten und Kernfunktionalitäten zu implementieren.
