# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Setter für Properties</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Setter für Properties
#
# Properties können auch modifiziert werden, indem ein *Setter* definiert wird.
# - Der Setter wird mit `@property_name.setter` dekoriert.
# - Er erlaubt es, Logik auszuführen, wenn der Wert einer Property gesetzt wird
#   (z.B. Validierung, Aktualisierung anderer Attribute).

# %%
import math
from math import isclose

# %%
class GeoPointV2:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    @property
    def radius(self):
        return (self.x**2 + self.y**2) ** 0.5

    @radius.setter
    def radius(self, new_radius):
        if new_radius < 0:
            raise ValueError("Radius cannot be negative.")

        old_radius = self.radius

        if old_radius == 0.0:
            raise ValueError("Cannot change radius of point at origin!")
        else:
            # Scale x and y to match the new radius
            scale = new_radius / old_radius
            self.x *= scale
            self.y *= scale

    @property
    def angle(self):
        return math.atan2(self.y, self.x)

    @angle.setter
    def angle(self, new_angle):
        r = self.radius  # Calls the getter
        self.x = r * math.cos(new_angle)
        self.y = r * math.sin(new_angle)

    def __repr__(self):
        # Accessing properties here will call getters
        return (
            f"GeoPointV2({self.x:.1f}, {self.y:.1f}, "
            f"r={self.radius:.2f}, θ={self.angle:.2f})"
        )


# %%
p = GeoPointV2(3.0, 4.0)
print("Original point: ", p)

# %%
# Set radius using the property setter
p.radius = 10.0
print("Set radius to 10:", p)

# %%
assert isclose(p.radius, 10.0)
assert isclose(p.x, 6.0)
assert isclose(p.y, 8.0)

# %%
# Set angle using the property setter
p.angle = math.pi / 2  # 90 degrees
print("Set angle to π/2:", p)

# %%
assert isclose(p.radius, 10.0)  # Radius should remain 10.0
assert p.x <= 1e-12 # Tolerance greater than isclose allows
assert isclose(p.y, 10.0)
assert isclose(p.angle, math.pi / 2)

# %%
# Try setting radius on a point at the origin
p_origin = GeoPointV2(0.0, 0.0)
print("\nOrigin point:", p_origin)

# %%
try:
    p_origin.radius = 5.0
    assert False, "Expected ValueError"
except ValueError as e:
    print(f"Error: {e}")

# %%
assert p_origin.x == 0.0
assert p_origin.y == 0.0
assert p_origin.radius == 0.0

# %% [markdown]
#
# ## Workshop: Temperatur-Konverter
#
# Erstellen Sie eine Klasse `Temperature`, die eine Temperatur intern in Grad
# Celsius speichert (z.B. in `_celsius`).
#
# - Implementieren Sie Properties `celsius`, `fahrenheit` und `kelvin`.
# - Der Konstruktor soll einen Wert und eine Einheit (`'C'`, `'F'` oder `'K'`)
#   akzeptieren und den internen `_celsius`-Wert korrekt initialisieren.
# - Das Setzen einer der Properties (`celsius`, `fahrenheit`, `kelvin`) soll den
#   internen `_celsius`-Wert korrekt aktualisieren.
# - Das Abrufen jeder Property soll den korrekt umgerechneten Wert liefern.
# - Fügen Sie eine `__repr__`-Methode hinzu.
#
# *Formeln:*
# - C = (F - 32) * 5/9
# - F = C * 9/5 + 32
# - C = K - 273.15
# - K = C + 273.15

# %%
class Temperature:
    def __init__(self, value, unit):
        if unit == "C":
            self._celsius = value
        elif unit == "F":
            self._celsius = (value - 32) * 5 / 9
        elif unit == "K":
            self._celsius = value - 273.15
        else:
            raise ValueError("Invalid unit. Use 'C', 'F', or 'K'.")

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9

    @property
    def kelvin(self):
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value):
        self._celsius = value - 273.15

    def __repr__(self):
        return f"Temperature(celsius={self._celsius:.2f})"

# %%
t = Temperature(100, "C")
print(t)

# %%
assert t.celsius == 100.0
assert t.fahrenheit == 212.0
assert t.kelvin == 373.15

# %%
t.fahrenheit = 32.0
print(t)

# %%
assert t.celsius == 0.0
assert t.fahrenheit == 32.0
assert t.kelvin == 273.15

# %%
t.kelvin = 0.0
print(t)

# %%
assert t.celsius == -273.15
assert isclose(t.fahrenheit, -459.67)
assert t.kelvin == 0.0

# %%
t = Temperature(0, "K")
print(t)

# %%
assert t.celsius == -273.15
assert isclose(t.fahrenheit, -459.67)
assert t.kelvin == 0.0

# %%
t = Temperature(32, "F")
print(t)

# %%
assert t.celsius == 0.0
assert t.fahrenheit == 32.0
assert t.kelvin == 273.15


# %% [markdown]
#
# ## Workshop: Rechteck-Geometrie
#
# Erstellen Sie eine Klasse `Rectangle`, die `width` (Breite) und `height`
# (Höhe) als *private* Attribute (`_width`, `_height`) speichert.
#
# - Stellen Sie *öffentliche Properties* `width` und `height` bereit, die Lese-
#   und Schreibzugriff auf die privaten Attribute ermöglichen. Fügen Sie
#   Validierung hinzu, um sicherzustellen, dass Breite und Höhe nicht negativ
#   gesetzt werden können.
# - Implementieren Sie *nur lesbare* Properties `area` (Fläche) und `perimeter`
#   (Umfang), die aus `_width` und `_height` berechnet werden.
# - Fügen Sie eine `__repr__`-Methode hinzu, die Breite, Höhe, Fläche und Umfang
#   anzeigt.
#
# *Formeln:*
# - Fläche = Breite * Höhe
# - Umfang = 2 * (Breite + Höhe)

# %%
class Rectangle:
    def __init__(self, width=1.0, height=1.0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width cannot be negative")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height cannot be negative")
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

    def __repr__(self):
        return (
            f"Rectangle(width={self._width:.2f}, height={self._height:.2f}, "
            f"area={self.area:.2f}, perimeter={self.perimeter:.2f})"
        )


# %%
r = Rectangle(3.0, 4.0)
print(r)

# %%
assert r.width == 3.0
assert r.height == 4.0
assert r.area == 12.0
assert r.perimeter == 14.0

# %%
r.width = 5.0
print(r)

# %%
assert r.width == 5.0
assert r.height == 4.0
assert r.area == 20.0
assert r.perimeter == 18.0

# %%
r.height = 2.0
print(r)

# %%
assert r.width == 5.0
assert r.height == 2.0
assert r.area == 10.0
assert r.perimeter == 14.0

# %%
try:
    r.width = -1.0
    assert False, "Expected ValueError"
except ValueError as e:
    print(f"Error: {e}")

# %%
try:
    r.height = -1.0
    assert False, "Expected ValueError"
except ValueError as e:
    print(f"Error: {e}")

# %% [markdown]
#
# ## Workshop: Personenalter
#
# Erstellen Sie eine Klasse `Person`, die `_first_name`, `_last_name` (private
# Attribute) und `birth_date` (Geburtsdatum, öffentliches Attribut) speichert.
# Verwenden Sie `datetime.date` für das Geburtsdatum.
#
# - Implementieren Sie Properties `first_name` und `last_name` für den
#   Lese-/Schreibzugriff auf die privaten Attribute.
# - Implementieren Sie eine *nur lesbare* Property `age`, die das aktuelle Alter
#   der Person in Jahren berechnet.
# - Implementieren Sie eine Property `full_name`, die den Vor- und Nachnamen
#   kombiniert zurückgibt. Das Setzen von `full_name` sollte `_first_name` und
#   `_last_name` aktualisieren (gehen Sie davon aus, dass der Name aus zwei
#   Teilen besteht, die durch ein Leerzeichen getrennt sind).
# - Fügen Sie eine `__repr__`-Methode hinzu.
#
# *Hinweis:* Sie benötigen `import datetime`.
#
# - Ein beliebiges Datum erhalten Sie mit `datetime.date(year, month, day)`.
# - Das heutige Datum erhalten Sie mit `datetime.date.today()`.
# - Die Differenz zwischen zwei Daten ergibt ein `timedelta`-Objekt, dessen
#   `days`-Attribut Sie verwenden können.

# %%
import datetime

# %%
march_1_2023 = datetime.date(2023, 3, 1)
today = datetime.date.today()

# %%
date_diff = today - march_1_2023
date_diff.days


# %%
class Person:
    def __init__(self, first_name, last_name, birth_date):
        self._first_name = first_name
        self._last_name = last_name
        self.birth_date = birth_date

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def age(self):
        today = datetime.date.today()
        age = today - self.birth_date
        return age.days // 365

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @full_name.setter
    def full_name(self, value):
        first_name, last_name = value.split(" ", 1)
        self._first_name = first_name
        self._last_name = last_name

    def __repr__(self):
        return (
            f"Person(first_name={self._first_name}, last_name={self._last_name}, "
            f"birth_date={self.birth_date}, age={self.age})"
        )


# %%
p = Person("John", "Doe", datetime.date(1990, 1, 1))
print(p)

# %%
assert p.first_name == "John"
assert p.last_name == "Doe"
assert p.birth_date == datetime.date(1990, 1, 1)
assert p.age >= 33  # Adjust based on the current date
assert p.full_name == "John Doe"

# %%
p.full_name = "Jane Smith"
print(p)

# %%
assert p.first_name == "Jane"
assert p.last_name == "Smith"
assert p.full_name == "Jane Smith"
