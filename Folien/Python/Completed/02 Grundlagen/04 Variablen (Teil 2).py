# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Variablen (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ## Variablennamen in Python
#
# - Fangen mit einem Buchstaben oder Unterstrich `_` an
#     - Umlaute gelten auch als Buchstaben
# - Können Ziffern, Buchstaben und Unterstriche `_` enthalten
# - Können viele andere Unicode-Zeichen enthalten
#     - Es ist aber meist besser, das zu vermeiden...
# - Groß- und Kleinschreibung wird unterschieden
#     - `A` ist eine andere Variable als `a`
#

# %%
# 2fast4u = 2

# %%
ähnlichkeitsmaß = 0.1

# %%
_größenmaßstäbe_der_fußgängerübergänge = 0.3
_größenmaßstäbe_der_fußgängerübergänge

# %%
# me@foo = 1

# %%
α = 0.2
β = 0.7
γ = α**2 + 3 * β**2
print(γ)
αβγ = α * β * γ
print(αβγ)
Σ = 1 + 2 + 3
print(Σ)
# ∑ = 1 + 2 + 3 # Unzulässig!


# %%
variable_1 = 123
VARIABLE_1 = 234
Variable_1 = 345
variablE_1 = 456

# %%
print(variable_1)
print(VARIABLE_1)
print(Variable_1)
print(variablE_1)

# %% [markdown]
# ### Stil
#
# - Variablennamen werden klein geschrieben
#     - Außer konstanten Variablen: `CONSTANT_VAR`
# - Bestandteile werden durch Unterstriche `_` getrennt
#     - Dieser Stil nennt sich Snake-Case
# - Variablen, die mit zwei Unterstrichen anfangen und aufhören haben
#   typischerweise eine spezielle Bedeutung (*Dunders*):
#     - `__class__`, `__name__`
#     - Normale benutzerdefinierte Variablen sollten nicht als Dunders benannt
#       werden

# %%
print(__name__)
print(type(__name__))

# %% [markdown]
#
# **Bitte nicht nachmachen, obwohl es möglich ist:**

# %%
__my_var__ = 123

# %%
__my_var__

# %% [markdown]
# - Manchmal werden "private" Variablen mit einem führenden Unterstrich
#   geschrieben: `_my_var`
#   - Das ist (für globale Variablen) besonders relativ verbreitet
#   - In Klassen gibt es weitere Konventionen
# - Die meisten Python-Projekte folgen den Konventionen in
#   [PEP 8](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

# %%
_my_var = 234

# %%
_my_var

# %%
_my_var = 1
print(_my_var)
_my_var = _my_var + 5
print(_my_var)

# %% [markdown]
# ## Zuweisung an mehrere Variablen
#
# In Python können mehrere Variablen gleichzeitig definiert bzw. mit neuen
# Werten versehen werden:

# %%
a, b = 1, 2
print(a)
print(b)

# %% [markdown]
#
# ## Mini-Workshop: Code Cleanup
#
# Der folgende Code enthält Verstöße gegen die in Python verwendete Syntax und die
# üblichen Konventionen. Code mit Syntaxfehlern ist auskommentiert. Korrigieren Sie
# ihn, so dass der Code in Python evaluiert werden kann und den Richtlinien für
# Variablennamen entspricht.

# %%
__anzahl_der_teilnehmer__ = 10
# Preisgeld für den 1. und 2. Platz
# 1terPlatz = 500
# 2terPlatz = 250
GesamtesPreisgeld = 1000
# Summe der Preisgelder für die ersten beiden Plätze
# ΣPreisgelder = 1terPlatz + 2terPlatz

# %%
anzahl_der_teilnehmer = 10
erster_platz = 500
zweiter_platz = 250
gesamtes_preisgeld = 1000
summe_preisgelder = erster_platz + zweiter_platz
