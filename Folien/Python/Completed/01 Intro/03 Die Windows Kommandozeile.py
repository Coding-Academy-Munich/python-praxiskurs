# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Die Windows Kommandozeile</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # (Anaconda) Powershell
#
# - Im Startmenü unter `Anaconda3 (64-bit)` zu finden
# - Verwenden Sie die Anaconda-Variante der Powershell
#   - Nur diese Version hat Zugriff auf die von Anaconda installierten Programme


# %% [markdown]
#
# ## Starten von Programmen
#
# - Der Prompt der Powershell sieht folgendermaßen aus:
#   ```powershell
#   (base) PS C:\Users\Test User>
#   ```
# - `(base)` ist das aktuelle Anaconda Environment.
# - Sie können viele Programme starten, indem Sie einfach ihren Namen eingeben.
#   - `notepad` für einen einfachen Text-Editor
#   - `python` für den Python Interpreter

# %% [markdown]
#
# ## Das Aktuelle Verzeichnis
#
# - Das im Prompt angezeigte Verzeichnis nennt sich "aktuelles Verzeichnis"
#   oder "Arbeitsverzeichnis".
# - Sie können auch das Kommando `pwd` eingeben, um das aktuelle Verzeichnis zu sehen.
# - Mit `ls` oder `dir` können Sie die Dateien im aktuellen Verzeichnis anzeigen.

# %% [markdown]
#
# ## Wechseln des Arbeitsverzeichnisses
#
# - Mit dem Kommando `cd` können Sie das aktuelle Verzeichnis wechseln
# - Nach `cd` steht ein Pfad:
#   - Absoluter Pfad: `cd c:\Windows`
#   - Relativer Pfad: `cd System` oder `cd .\System`
# - Sie können die `Tab`-Taste verwenden, um Pfade zu vervollständigen
# - `.` steht für das aktuelle Verzeichnis, `..` für das übergeordnete Verzeichnis
# - Sie können `/` oder `\` verwenden, um Pfadbestandteile zu trennen
# - Pfade mit Leerzeichen müssen in Anführungszeichen eingeschlossen werden:
#   - cd 'C:\Users\Test User\'

# %% [markdown]
#
# ## Tipps zum Arbeiten mit Pfaden
#
# - Vervollständigen Sie Pfade mit der `Tab`-Taste
# - Verwenden Sie `~` um in Ihr Home-Verzeichnis zu wechseln
# - Verwenden Sie `..` um ins übergeordnete Verzeichnis zu wechseln
# - Kopieren Sie Pfade aus dem Explorer oder Finder

# %% [markdown]
#
# ## Das war's schon
#
# - Die Kommandozeile bietet viel mehr Features als wir besprochen haben
# - Aber für das, was wir in diesem Kurs machen wollen, wissen wir genug

