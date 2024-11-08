# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Die Linux Shell</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Die Shell auf Linux
#
# - Unter Linux integriert sich Anaconda in die normale Shell
# - Im Gegensatz zu Windows müssen Sie also keine spezielle "Anaconda Shell"
#   starten
# - Falls Ihre Installation sich anders verhält, finden Sie
#   [hier](https://docs.anaconda.com/free/anaconda/install/linux/) weitere
#   Informationen
# - Die meisten Linux Systeme verwenden die Bash Shell


# %% [markdown]
#
# ## Die Bash Shell
#
# - Die Bash Shell ist eine leistungsfähige Shell/Kommandozeile
# - Normalerweise die Default-Shell im Terminal
# - Verwendung: Ausführen von Programmen, Verwalten von Dateien, etc.

# %% [markdown]
#
# ## Der Prompt
#
# - Beispiel für einen Prompt:
#   ```bash
#   (base) [tc@fedora ~]$
#   ```
# - `(base)` ist das aktuelle Anaconda Environment.
# - Information über den Benutzer, Computer und das aktuelle Verzeichnis
# - `$` zeigt an, dass Sie jetzt Kommandos eingeben können
#   - `root`-Benutzer: `#` statt `$`

# %% [markdown]
#
# ## Das Aktuelle Verzeichnis
#
# - Im Prompt angezeigtes Verzeichnis: "aktuelles Verzeichnis" oder
#   "Arbeitsverzeichnis"
# - `pwd` um es in der Shell anzuzeigen
# - `ls`: Anzeigen von Dateien im aktuellen Verzeichnis
# - Optionen in der Form `-l` oder `--help`

# %% [markdown]
#
# ## Wechseln des Arbeitsverzeichnisses
#
# - Mit dem Kommando `cd` können Sie das aktuelle Verzeichnis wechseln
# - Nach `cd` steht ein Pfad:
#   - Absoluter Pfad: `cd /home/some-user/programs`
#   - Relativer Pfad: `cd programs` oder `cd ./programs`
# - Sie können die `Tab`-Taste verwenden, um Pfade zu vervollständigen
# - `.` steht für das aktuelle Verzeichnis, `..` für das übergeordnete Verzeichnis
# - Pfadbestandteile werden mit `/` getrennt
# - Pfade mit Leerzeichen müssen in Anführungszeichen eingeschlossen werden:
# - cd '/home/test user/'


# %% [markdown]
#
# ## Tipps zum Arbeiten mit Pfaden
#
# - Vervollständigen Sie Pfade mit der `Tab`-Taste
# - Verwenden Sie `~` um in Ihr Home-Verzeichnis zu wechseln
# - Verwenden Sie die Kommando-History (Pfeil nach oben, Pfeil nach unten,
#   `Strg-R`) um in Verzeichnisse zu wechseln, die Sie schon einmal besucht
#   haben

# %% [markdown]
#
# ## Das war's schon
#
# - Die Kommandozeile bietet viel mehr Features als wir besprochen haben
# - Aber für das, was wir in diesem Kurs machen wollen, wissen wir genug

