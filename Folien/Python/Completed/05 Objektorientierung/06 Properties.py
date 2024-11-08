# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Properties</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ## Properties
#
# Wie können wir es ermöglichen auf einen Punkt sowohl mittels der `x` und
# `y`-Koordinaten zuzugreifen, als auch mittels Radius und Winkel?

# %%
import math


# %%
class GeoPointV0:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def get_radius(self):
        return math.hypot(self.x, self.y)

    def get_angle(self):
        return math.atan2(self.y, self.x)

    def __repr__(self):
        return (
            f"GeoPointV0({self.x:.1f}, {self.y:.1f}, "
            f"r={self.get_radius():.2f}, θ={self.get_angle():.2f})"
        )


# %%
p = GeoPointV0()
p

# %%
assert p.x == 0.0
assert p.y == 0.0
assert p.get_radius() == 0.0
assert p.get_angle() == 0.0

# %%
p = GeoPointV0(1.0, 0.0)
p

# %%
assert p.x == 1.0
assert p.y == 0.0
assert p.get_radius() == 1.0
assert p.get_angle() == 0.0

# %%
p = GeoPointV0(0.0, 2.0)
p

# %%
from math import isclose, pi

assert p.x == 0.0
assert p.y == 2.0
assert p.get_radius() == 2.0
assert isclose(p.get_angle(), pi / 2)

# %% [markdown]
#
# Es ist unschön, dass bei der Verwendung von `GeoPointV0` die Attribute `x` und `y`
# anders behandelt werden müssen als `radius` und `angle`:

# %%
p = GeoPointV0(1.0, 1.0)
print(p.x, p.y, p.get_radius(), p.get_angle())


# %%
class GeoPointV1:  # noqa
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    @property
    def radius(self):
        return (self.x**2 + self.y**2) ** 0.5

    @property
    def angle(self):
        return math.atan2(self.y, self.x)

    def __repr__(self):
        return (
            f"GeoPointV1({self.x:.1f}, {self.y:.1f}, "
            f"r={self.radius:.2f}, θ={self.angle:.2f})"
        )


# %%
p = GeoPointV1()
p

# %%
assert p.x == 0.0
assert p.y == 0.0
assert p.radius == 0.0
assert p.angle == 0.0

# %%
p = GeoPointV1(1.0, 0.0)
p

# %%
assert p.x == 1.0
assert p.y == 0.0
assert p.radius == 1.0
assert p.angle == 0.0

# %%
p = GeoPointV1(0.0, 2.0)
p

# %%
from math import isclose, pi

assert p.x == 0.0
assert p.y == 2.0
assert p.radius == 2.0
assert isclose(p.angle, pi / 2)

# %%
GeoPointV1(1.0, 0.0)

# %%
GeoPointV1(0.0, 2.0)

# %%
p = GeoPointV1(1.0, 1.0)
print(p.x, p.y, p.radius, p.angle)


# %% [markdown]
#
# ## Setter für Properties:
#
# Properties können auch modifiziert werden:

# %%
class GeoPointV2:  # noqa
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    @property
    def radius(self):
        return (self.x**2 + self.y**2) ** 0.5

    @radius.setter
    def radius(self, new_radius):
        old_radius = self.radius
        if old_radius == 0.0:
            raise ValueError("Cannot change radius of origin!")
        self.x *= new_radius / old_radius
        self.y *= new_radius / old_radius

    @property
    def angle(self):
        return math.atan2(self.y, self.x)

    def __repr__(self):
        return (
            f"GeoPointV2({self.x:.1f}, {self.y:.1f}, "
            f"r={self.radius:.2f}, θ={self.angle:.2f})"
        )


# %%
p = GeoPointV2(3.0, 4.0)
print("Original point:  ", p)
p.radius = 10.0
print("Set radius to 10:", p)

# %%
assert p.radius == 10.0
