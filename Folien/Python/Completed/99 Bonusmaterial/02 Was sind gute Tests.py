# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Was sind gute Tests?</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# <img src="img/velocity-tests-03.png"
#      alt="Velocity vs. Tests 3"
#      style="width: 75%; margin-left: auto; margin-right: auto;"/>

# %% [markdown]
#
# ## Welche Eigenschaften sollte ein Test haben?
#
# <ul>
# <li class="fragment">Zeigt viele Fehler/Regressionen im Code auf</li>
# <li class="fragment">Gibt schnelle Rückmeldung</li>
# <li class="fragment">Ist deterministisch</li>
# <li class="fragment">Ist leicht zu warten und verstehen</li>
# <li class="fragment"><b>Unempfindlich gegenüber Refactorings</b></li>
# </ul>
#
# <p class="fragment">
#   Leider stehen diese Eigenschaften oft im Konflikt zueinander!
# </p>

# %% [markdown]
#
# ## Aufzeigen von Fehlern/Regressionen
#
# ### Einflüsse
#
# <ul>
#   <li class="fragment">Menge des abgedeckten Codes</li>
#   <li class="fragment">Komplexität des abgedeckten Codes</li>
#   <li class="fragment">Interaktion mit externen Systemen</li>
#   <li class="fragment">Signifikanz des abgedeckten Codes für die Domäne/das
#   System</li>
# </ul>

# %%
class Item:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.set_price(price)

    def __repr__(self) -> str:
        return f"Item({self.name}, {self.price})"

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def set_price(self, value: float) -> None:
        self.price = abs(value)

# %%
class Order:
    def __init__(self, *items: Item) -> None:
        self.items = list(items)

    def __repr__(self) -> str:
        return f"Order({', '.join(map(str, self.items))}), total = {self.get_total()}"

    def get_items(self) -> list[Item]:
        return self.items

    def get_total(self) -> float:
        return sum(item.get_price() for item in self.items)

# %%
def test_item_name():
    unit = Item("Apple", 1.0)

    assert unit.get_name() == "Apple"
    print("Success.")


# %%
test_item_name()

# %%
def test_order_total():
    unit = Order(
        Item("Apple", 1.0),
        Item("Banana", -2.0),
    )

    assert unit.get_total() == 3.0
    print("Success.")


# %%
test_order_total()

# %%
def test_order_output():
    unit = Order(
        Item("Apple", 1.0),
        Item("Banana", -2.0),
    )

    print(unit)
    assert str(unit) == "Order(Item(Apple, 1.0), Item(Banana, 2.0)), total = 3.0"
    print("Success.")

# %%
test_order_output()

# %% [markdown]
#
# ## Schnelle Rückmeldung
#
# ### Einflüsse
#
# - Menge des abgedeckten Codes
# - Komplexität/Anzahl Iterationen des abgedeckten Codes
# - Interaktion mit externen Systemen

# %% [markdown]
#
# ## Deterministisch
#
# <ul>
#   <li class="fragment">Gleicher Code führt immer zum gleichen Ergebnis</li>
#   <li class="fragment">Gründe für Nichtdeterminismus
#     <ul>
#       <li class="fragment">Zufallszahlen</li>
#       <li class="fragment">Zeit/Datum</li>
#       <li class="fragment">Interaktion mit externen Systemen</li>
#       <li class="fragment">Nicht initialisierte Variablen</li>
#       <li class="fragment">Kommunikation zwischen Tests</li>
#     </ul>
#   </li>
#   <li class="fragment">
#      Tests, die falsche Warnungen erzeugen sind nicht
#      hilfreich sondern schädlich!
#   </li>
# <ul>

# %%
import random

# %%
def test_random_bad():
    roll = random.randint(1, 2)

    assert roll == 1
    print("Success!")


# %%
# test_random_bad()

# %%
def test_random_better():
    random.seed(42)
    roll = random.randint(1, 2)

    assert roll == 1
    print("Success!")

# %%
# test_random_better()

# %%
import time

# %%
def test_date_bad():
    now = time.time()
    unit = time.localtime(now)

    assert unit.tm_year == 2024
    assert unit.tm_sec % 2 == 0
    print("Success!")

# %%
# test_date_bad()

# %%
import datetime

# %%
def test_date_better():
    unit = datetime.datetime(2024, 1, 1, 0, 0, 0).timetuple()

    print(unit)
    assert unit.tm_year == 2024
    assert unit.tm_sec % 2 == 0
    print("Success!")


# %%
# test_date_better()

# %% [markdown]
#
# ## Leicht zu warten
#
# <ul>
#   <li>Einfache, standardisierte Struktur<br>
#     <table style="display:inline;margin:20px 20px;">
#     <tr><td style="text-align:left;width:60px;padding-left:15px;">Arrange</td>
#         <td style="text-align:left;width:60px;padding-left:15px;border-left:1px solid black;">Given</td>
#         <td style="text-align:left;width:300px;padding-left:15px;border-left:1px solid black;">
#           Bereite das Test-Environment vor</td></tr>
#     <tr><td style="text-align:left;padding-left:15px;">Act</td>
#         <td style="text-align:left;width:60px;padding-left:15px;border-left:1px solid black;">
#            When</td>
#         <td style="text-align:left;width:300px;padding-left:15px;border-left:1px solid black;">
#            Führe die getestete Aktion aus (falls vorhanden)</td></tr>
#     <tr><td style="text-align:left;padding-left:15px;">Assert</td>
#         <td style="text-align:left;width:60px;padding-left:15px;border-left:1px solid black;">
#            Then</td>
#         <td style="text-align:left;width:300px;padding-left:15px;border-left:1px solid black;">
#            Überprüfe die Ergebnisse</td></tr>
#     </table>
#   </li>
#   <li>Wenig Code
#     <ul>
#       <li>Wenig Boilerplate</li>
#       <li>Factories, etc. für Tests</li>
#     </ul>
#   </li>
# </ul>

# %% [markdown]
#
# ## Unempfindlich gegenüber Refactorings
#
# - Möglichst wenige falsche Positive!
# - Typischerweise vorhanden oder nicht, wenig Zwischenstufen
#
# ### Einflüsse
#
# - Bezug zu Domäne/System
# - Zugriff auf interne Strukturen

# %%
class VeryPrivate:
    def __init__(self) -> None:
        self.__secret = 42

    def divides_secret(self, value: int) -> bool:
        return value // self.__secret == 0

# %%
def test_very_private():
    unit = VeryPrivate()

    assert unit._VeryPrivate__secret == 42 # type: ignore
    print("Success!")


# %%
test_very_private()

# %% [markdown]
#
# Die folgenden Einflüsse stehen im Konflikt zueinander:
#
# - Erkennen von Fehlern/Regressionen
# - Schnelle Rückmeldung
# - Unempfindlich gegenüber Refactorings
#
# Die Qualität eines Tests hängt vom *Produkt* dieser Faktoren ab!

# %% [markdown]
#
# ## Wie finden wir den Trade-Off?
#
# - Unempfindlich gegenüber Refactorings kann *nie* geopfert werden
# - Wir müssen also einen Kompromiss finden zwischen
#   - Erkennen von Fehlern/Regressionen
#   - Schnelle Rückmeldung
#
# ### Typischerweise
#
# - Schnelles Feedback für die meisten Tests (Unit-Tests)
# - Gründliche Fehlererkennung für wenige Tests (Integrationstests)
