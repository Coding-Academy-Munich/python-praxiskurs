# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Domänenmodelle</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Was ist ein Domänenmodell?
#
# - Eine **konzeptionelle Repräsentation** einer bestimmten Domäne.
# - **Zweck**: Verständnis und Dokumentation, wie Daten-Elemente innerhalb einer
#   Domäne interagieren.
# - **Beinhaltet**:
#   - Entitäten
#   - Beziehungen
#   - Attribute
#   - Operationen

# %% [markdown]
#
# ## Domänenmodelle in verschiedenen Branchen

# %% [markdown]
#
# <img src="img/e-commerce.png" width="100%">

# %% [markdown]
#
# ### Wie finden wir Entitäten und Operationen?
#
# - Entitäten sind of Konzepte, die in der Domäne vorkommen
#   - Personen, Orte, Dinge, ...
#   - Abstrakte Konzepte
#   - Im Beschreibungen oft Substantive
# - Operationen sind oft Verben
#   - Oft werden "Dinge, die mit einer Entität gemacht werden" zu Operationen

# %% [markdown]
#
# **Allerdings:** Das ist nicht immer so einfach!
#
# Viele Konzepte können sowohl als Substantiv als auch als Verb ausgedrückt werden:
#
# - Der Kunde **bestellt** ein Produkt.
# - Der Kunde gibt eine **Bestellung** auf.
#
# (Manchmal findet man beides im Domänenmodell wieder.)

# %% [markdown]
#
# ### E-Commerce
#
# - Entitäten: Unternehmen, Produkte, Kunden, Bestellungen, Positionen
# - Beziehungen:
#   - Unternehmen verkaufen Produkte
#   - Unternehmen haben Kunden und offene Bestellungen
#   - Bestellungen werden von Kunden vorgenommen
#   - Bestellungen enthalten Positionen
#   - Positionen referenzieren Produkte
# - Operationen:
#   - Kunden geben Bestellungen auf
#   - Unternehmen versenden Bestellungen

# %% [markdown]
#
# ### UML-Klassendiagramm
#
# - Domänenmodelle werden oft als UML-Klassendiagramme dargestellt
# - UML = Unified Modeling Language
# - Klassendiagramme sind nur eine von vielen UML-Diagrammarten
# - Wie man Domänenmodelle genau darstellt, ist nicht so wichtig
# - Wesentlich ist, dass alle Stakeholder das Modell verstehen

# %% [markdown]
#
# <img src="img/e-commerce-dm.svg" width="85%"
#      style="margin-left: auto; margin-right: auto;">

# %% [markdown]
#
# <img src="img/cars.png" width="100%">

# %% [markdown]
#
# ### Selbstfahrende Autos
#
# - Entitäten: Autos, Sensoren, GPS, Karten, Fahrbahn, Route, Orte
# - Beziehungen:
#   - Autos haben Sensoren und GPS
#   - Autos haben Karten
#   - Autos fahren auf Fahrbahnen
#   - Routen verbinden Orte
# - Operationen:
#   - Autos fahren Routen
#   - Autos erkennen Fahrbahnen

# %% [markdown]
#
# <img src="img/cars-dm.svg" width="70%"
#      style="margin-left: auto; margin-right: auto;">

# %% [markdown]
#
# <img src="img/bank.png" width="100%">

# %% [markdown]
#
# ### Bankenwesen
#
# - Entitäten: Konten, Transaktionen, Kunden
# - Beziehungen:
#   - Kunden besitzen Konten
#   - Konten erfassen Transaktionen
# - Operationen:
#   - Kunden eröffnen Konten
#   - Kunden zahlen Geld auf Konten ein
#   - Kunden überweisen Geld von Konten

# %% [markdown]
#
# <img src="img/bank-dm.svg" width="60%"
#      style="margin-left: auto; margin-right: auto;">


# %% [markdown]
#
# ## Workshop: Domänenmodelle
#
# Im Folgenden sind einige Domänen aufgeführt. Versuchen Sie, für jede Domäne
# ein (einfaches) Domänenmodell zu erstellen.
#
# Zeichnen Sie jeweils ein UML-Klassendiagramm mit den Entitäten und Beziehungen.
#
# Falls Sie an einem Software-Projekt in einer bestimmten Domäne arbeiten,
# versuchen Sie, ein Domänenmodell für Ihr Projekt zu erstellen.

# %% [markdown]
#
# <img src="img/social-network.png" width="100%">

# %% [markdown]
#
# ### Soziale Netzwerke

# %% [markdown]
#
# - Entitäten: Personen, Gruppen, Beiträge, Kommentare
# - Beziehungen:
#   - Personen sind Mitglieder von Gruppen
#   - Beiträge sind in Gruppen veröffentlicht
#   - Kommentare gehören zu Beiträgen
# - Operationen:
#   - Personen veröffentlichen Beiträge
#   - Personen kommentieren Beiträge

# %% [markdown]
#
# <img src="img/social-network-dm.svg" width="50%"
#      style="margin-left: auto; margin-right: auto;">

# %% [markdown]
#
# <img src="img/medicine.png" width="100%">

# %% [markdown]
#
# ### Gesundheitswesen

# %% [markdown]
#
# - Entitäten: Patienten, Ärzte, Termine, Rezepte
# - Beziehungen: Ärzte und Patienten haben Termine
# - Operationen:
#   - Patienten vereinbaren Termine mit Ärzten
#   - Ärzte schreiben Rezepte für Patienten

# %% [markdown]
#
# <img src="img/medicine-dm.svg" width="60%"
#      style="margin-left: auto; margin-right: auto;">

# %% [markdown]
#
# <img src="img/uni.png" width="100%">

# %% [markdown]
#
# ### Bildungswesen
#

# %% [markdown]
#
# - Entitäten: Studierende, Kurse, Dozierende, Hörsäle
# - Beziehungen:
#   - Dozierende halten Kurse (unterrichten Kurse)
#   - Studierende sind in Kurse eingeschrieben
#   - Kurse finden in Hörsälen statt
# - Operationen:
#   - Dozierende unterrichten Kurse
#   - Studierende schreiben sich in Kurse ein

# %% [markdown]
#
# <img src="img/uni-dm.svg" width="35%"
#      style="margin-left: auto; margin-right: auto;">
