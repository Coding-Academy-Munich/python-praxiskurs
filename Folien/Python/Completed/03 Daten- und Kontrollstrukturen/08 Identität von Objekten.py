# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Identität von Objekten</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
#  ## Identität von Objekten

# %%
a = [1, 2, 3]
b = [1, 2, 3]
c = b

# %%
print(f"a = {a}, b = {b}, c = {c}")

# %%
a[0] = 10

# %%
print(f"a = {a}, b = {b}, c = {c}")

# %%
b[0] = 20

# %%
c[1] = 30

# %%
print(f"a = {a}, b = {b}, c = {c}")

# %% [markdown]
#
#  <img src="img/identity.svg" style="display:block;width:70%;margin:auto;"/>

# %% [markdown]
#
#  ## Test der Identität von Objekten

# %%
a = [1, 2, 3]
b = [1, 2, 3]
c = b


# %% [markdown]
#
#  `==` testet Gleichheit der Werte, nicht (notwendigerweise) Objektidentität.

# %%
a == b

# %%
b == c

# %%
a[0] = 10
a == b

# %% [markdown]
#
#  Mit `is` kann man Objektidentität testen:

# %%
a = [1, 2, 3]
b = [1, 2, 3]
c = b


# %%
a is b

# %%
b is c

# %%
b[0] = 10

# %%
print(f"a = {a}, b = {b}, c = {c}")

# %% [markdown]
#
#  Die Funktion `id()` gibt die Adresse eines Objekts zurück:

# %%
id([1, 2, 3])

# %% [markdown]
#
#  Meistens stellt man Adressen in hexadezimaler Form dar:

# %%
hex(id([1, 2, 3]))

# %% [markdown]
#
# ## Mini-Workshop: Identität
#
# Gegeben seien die folgenden Listen:

# %%
a = [1, 2, 3]
b = [1, 2]

# %% [markdown]
#
# - Sind `a` und `b` Listen, die die gleichen Elemente haben?
# - Sind `a` und `b` die gleiche Liste?
# - An welcher Adresse befindet sich `b`?

# %%
a == b

# %%
a is b

# %%
hex(id(b))

# %%
addr_b = hex(id(b))

# %% [markdown]
#
# Werten Sie jetzt die folgende Zelle aus:

# %%
b.append(3)

# %% [markdown]
#
# - Sind `a` und `b` jetzt Listen, die die gleichen Elemente haben?
# - An welcher Adresse befindet sich jetzt `b`?

# %%
a == b

# %%
hex(id(b))

# %%
addr_b == hex(id(b))
