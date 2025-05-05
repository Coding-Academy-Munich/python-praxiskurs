# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Pytest</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
#  # Pytest: Testen in Python
#
#  - Python bietet mehrere eingebaute Pakete zum Schreiben von Unit-Tests und
#    Dokumentationstests an (`unittest` und `doctest`).
#  - Viele Projekte verwenden trotzdem das `pytest` Paket, da es viel "Boilerplate"
#    beim Schreiben von Tests vermeidet.
#  - `pytest` kann `unittest` und `doctest`-Tests ausführen.

# %% [markdown]
#
#  ## Installation von Pytest
#
#  Pytest ist in der Anaconda-Installation vorinstalliert.
#
#  Beim Verwenden der Standard Python Distribution kann es mit
#  ```shell
#  pip install pytest
#  ```
#  installiert werden

# %% [markdown]
#
#  ## Schreiben von Tests
#
#  - Pytest kann sehr flexibel konfiguriert werden
#  - Wir verwenden nur die einfachsten Features und verlassen uns auf die automatische
#    Konfiguration
#  - Tests für ein Paket werden in einem Unter-Package `test` geschrieben
#  - Tests für die Datei `foo.py` sind in der Datei `test/foo_test.py`
#  - Jeder Test ist eine Funktion, deren Name mit `test` beginnt
#  - Assertions werden mit der `assert` Anweisung geschrieben

# %% [markdown]
#
#  ## Beispiel: `SimplePytest`
#
#  Siehe `SimplePytestStarterKit`

# %% [markdown]
#
# ## Mini-Workshop: Unit-Tests
#
# Schreiben Sie Unit-Tests für die `negate()` und `my_abs()` Funktionen in
# `examples/SimplePytestStarterKit`. Helfen Ihnen diese Tests Fehler in der
# Implementierung zu finden?
