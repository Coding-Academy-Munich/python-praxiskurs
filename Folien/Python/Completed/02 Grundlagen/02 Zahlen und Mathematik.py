# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Zahlen und Mathematik</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# # Zahlen und Mathematik
#
# - Ganze Zahlen: `1`, `837`, `-12`
# - Gleitkommazahlen: `0.5`, `123.4`, `-0.01`
# - Rechenoperationen:
#     - Addition: `+`
#     - Subtraktion: `-`
#     - Multiplikation: `*`
#     - Division: `/`

# %% [markdown]
# ## Python als Taschenrechner

# %%
17 + 4

# %%
1.5 + 7.4

# %%
1 + 2 * 3

# %% [markdown]
# ## Arten von Zahlen
#
# - Python unterscheidet ganze Zahlen und Gleitkommazahlen:
#     - `1` ist eine ganze Zahl (`int`)
#     - `1.0` ist eine Gleitkommazahl (`float`)
# - Mit `type(...)` kann man den Typ des Arguments erfahren:

# %%
type(1)

# %%
type(1.0)

# %%
type("1")

# %% [markdown]
# Ganze Zahlen in Python haben keine (praktisch relevante) Obergrenze:

# %%
10000000000000000000000000000000000000000000000000 + 500

# %%
type(10000000000000000000000000000000000000000000000000)

# %% [markdown]
# ## Rechenoperationen
#
# | Operator | Operation            |
# |:--------:|:---------------------|
# | +        | Summe                |
# | -        | Differenz            |
# | *        | Multiplikation       |
# | /        | Division             |
# | **       | Potenz               |
# | %        | Modulo, Rest         |
# | //       | ganzzahlige Division |

# %% [markdown]
# ### Division

# %%
4 / 2

# %%
20 / 7

# %%
# // und % können zur Division mit Rest verwendet werden:
20 // 7  # Wie oft geht 7 in 20?

# %%
20 % 7  # Welcher Rest bleibt dabei?

# %%
(20 // 7) * 7 + (20 % 7)

# %% [markdown]
# `/` ist links-assoziativ (genau wie `//`, `%`, `+`, `-`, `*`)

# %%
20 / 5 / 2

# %%
# Besser:
(20 / 5) / 2

# %%
20 / (5 / 2)

# %% [markdown]
# ### Exponentiation (Potenz)

# %%
2**3

# %%
2 * 2 * 2

# %%
2**4

# %%
2 * 2 * 2 * 2

# %% [markdown]
# `**` ist rechts-assoziativ
#
# $2^{(2^3)} = 2^8 = 256 \qquad$
# $(2^2)^3 = 4^3 = 64$

# %%
2**2**3

# %%
2 ** (2**3)

# %%
(2**2) ** 3

# %% [markdown]
# Der `**` Operator kann auch zum Wurzelziehen verwendet werden:
#
# $\sqrt{4} = 4^{1/2} = 2$
# $\sqrt{9} = 9^{1/2} = 3$
# $\sqrt{2} = 2^{1/2} \approx 1.4142$

# %%
4**0.5

# %%
9**0.5

# %%
2**0.5

# %% [markdown]
# ## Mini-Workshop: Zahlen und Mathematik
#

# %% [markdown]
#
# Wie können Sie die Zahl `32` in Python darstellen?

# %%
32

# %% [markdown]
# Wie können Sie den Datentyp von `14` in Python feststellen?

# %%
type(14)

# %% [markdown]
# Wie können Sie den Datentyp von `14.0` in Python feststellen?

# %%
type(14.0)

# %% [markdown]
# Wie können Sie den Datentyp von `"14"` in Python feststellen?

# %%
type("14")

# %% [markdown]
# Was ist der Wert von `1 + 2 * 3`?

# %%
1 + 2 * 3

# %% [markdown]
# Was ist der Datentyp von `1 + 2 * 3` in Python?

# %%
type(1 + 2 * 3)

# %% [markdown]
# Was ist der Wert von `4 / 2` in Python?

# %%
4 / 2

# %% [markdown]
# Was ist der Datentyp von `4 / 2` in Python?

# %%
type(4 / 2)

# %% [markdown]
# Was sind Wert und Datentyp von `1 + 1.0` in Python? Können Sie den Datentyp
# ohne Verwendung von `type` feststellen, indem Sie die Ausgabe ansehen?

# %%
1 + 1.0  # Typ ist float, da Ausgabe Nachkommastellen hat
