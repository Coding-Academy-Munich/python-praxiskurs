# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Propagation von Exceptions</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Stack-Unwinding
#
# Wenn eine Exception ausgelöst wird, werden geschachtelte Funktionsaufrufe so lange
# abgebrochen, bis ein passender Handler gefunden wird:

# %% [markdown]
#
# <img src="img/stack-code.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%; margin-top: 3%;"/>
#
# <img src="img/stack-01a.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%;"/>

# %% [markdown]
#
# <img src="img/stack-code.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%; margin-top: 3%;"/>
#
# <img src="img/stack-01b.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%;"/>

# %% [markdown]
#
# <img src="img/stack-code.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%; margin-top: 3%;"/>
#
# <img src="img/stack-01c.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%;"/>

# %% [markdown]
#
# <img src="img/stack-code.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%; margin-top: 3%;"/>
#
# <img src="img/stack-01d.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%;"/>

# %% [markdown]
#
# <img src="img/stack-code.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%; margin-top: 3%;"/>
#
# <img src="img/stack-01e.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%;"/>

# %% [markdown]
#
# <img src="img/stack-code.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%; margin-top: 3%;"/>
#
# <img src="img/stack-02.png" alt="Call Stack"
#      style="float: left; width: 37.3%; margin-left: 10%;"/>

# %% [markdown]
#
# <img src="img/stack-code.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%; margin-top: 3%;"/>
#
# <img src="img/stack-03.png" alt="Call Stack"
#      style="float: left; width: 37.3%; margin-left: 10%;"/>

# %% [markdown]
#
# <img src="img/stack-code.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%; margin-top: 3%;"/>
#
# <img src="img/stack-04.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%;"/>


# %%
from enum import Enum


# %%
class ErrorType(Enum):
    VALUE = "ValueError"
    LOOKUP = "LookupError"
    INDEX = "IndexError"


# %%
IndexError.mro()

# %%
ValueError.mro()


# %%
def outer_caller_v0(error_type: ErrorType = ErrorType.VALUE):
    intermediate_fun_v0(error_type)


# %%
def intermediate_fun_v0(error_type: ErrorType):
    raise_and_handle_error_v0(error_type)


# %%
def raise_and_handle_error_v0(error_type: ErrorType):
    try:
        if error_type == ErrorType.VALUE:
            raise ValueError()
        elif error_type == ErrorType.LOOKUP:
            raise LookupError()
        else:
            raise IndexError()
    except LookupError:
        pass


# %%
def outer_caller_with_try_v0(error_type: ErrorType = ErrorType.VALUE):
    try:
        intermediate_fun(error_type)
    except Exception:
        pass


# %%
outer_caller_with_try_v0(ErrorType.VALUE)

# %%
# outer_caller_v0(ErrorType.VALUE)


# %%
def raise_and_handle_error(error_type: ErrorType):
    print("    raise_and_handle_error(): before try")
    try:
        print("    raise_and_handle_error(): before raise")
        if error_type == ErrorType.VALUE:
            raise ValueError("Raising ValueError")
        elif error_type == ErrorType.LOOKUP:
            raise LookupError("Raising LookupError")
        else:
            raise IndexError("Raising IndexError")
        print("    raise_and_handle_error(): after raise")  # noqa
    except LookupError as error:
        print(f"<<< raise_and_handle_error(): caught LookupError [{error}]")
    print("    raise_and_handle_error(): after except")


# %%
def intermediate_fun(error_type: ErrorType):
    print("  intermediate_fun(): before call")
    raise_and_handle_error(error_type)
    print("  intermediate_fun(): after call")


# %%
def outer_caller(error_type: ErrorType = ErrorType.VALUE):
    print("outer_caller(): before calling")
    intermediate_fun(error_type)
    print("outer_caller(): after calling")


# %%
outer_caller(ErrorType.LOOKUP)

# %%
outer_caller(ErrorType.INDEX)

# %%
# outer_caller(ErrorType.VALUE)


# %%
def outer_caller_with_try(error_type: ErrorType = ErrorType.VALUE):
    print("outer_caller(): before try")
    try:
        print("outer_caller(): before calling")
        intermediate_fun(error_type)
        print("outer_caller(): after calling")
    except Exception as error:
        print(f"<<< outer_caller(): caught Exception: {error}")
    print("outer_caller(): after except")


# %%
outer_caller_with_try(ErrorType.INDEX)


# %%
outer_caller_with_try(ErrorType.VALUE)


# %% [markdown]
#
# ## Workshop: Verschachtelte Ausnahmen
#
# In diesem Workshop wollen wir betrachten, wie sich verschachtelte Ausnahmen
# verhalten.
#
# Gegeben seien die folgenden Funktionen.
#
# Welche Ausgabe erwarten Sie für Aufrufe von `outer_caller_ws()` und
# `outer_caller_with_try_ws()` mit den verschiedenen `ErrorType`-Werten?

# %%
def raise_and_handle_error_ws(exception_type: ErrorType):
    print("    raise_and_handle_error_ws(): before try")
    try:
        print("    raise_and_handle_error_ws(): before raise")
        if exception_type == ErrorType.VALUE:
            raise ValueError("Raising ValueError")
        elif exception_type == ErrorType.LOOKUP:
            raise LookupError("Raising LookupError")
        else:
            raise IndexError("Raising IndexError")
    except LookupError as error:
        print(f"<<< raise_and_handle_error_ws(): caught LookupError [{error}]")
        raise
    except ValueError as error:
        print(f"<<< raise_and_handle_error_ws(): caught ValueError [{error}]")
    print("    raise_and_handle_error_ws(): after except")


# %%
def intermediate_fun_ws(exception_type: ErrorType):
    print("  intermediate_fun_ws(): before call")
    try:
        raise_and_handle_error_ws(exception_type)
    except IndexError as error:
        print(f"<<< intermediate_fun_ws(): caught IndexError [{error}]")
        raise TypeError(f"Raising inner TypeError from [{error}]") from error
    except LookupError as error:
        print(f"<<< intermediate_fun_ws(): caught LookupError [{error}]")
        raise TypeError("Raising inner TypeError")
    except Exception as error:
        print(f"<<< intermediate_fun_ws(): caught Exception [{error}]")
        print("  intermediate_fun_ws(): re-raising exception")
        raise
        print("  intermediate_fun_ws(): re-raised exception")  # noqa
    print("  intermediate_fun_ws() after call")


# %%
def outer_caller_ws(exception_type: ErrorType = ErrorType.VALUE):
    print("outer_caller_ws(): before calling")
    intermediate_fun_ws(exception_type)
    print("outer_caller_ws(): after calling")


# %%
outer_caller_ws(ErrorType.VALUE)

# %%
# outer_caller_ws(ErrorType.LOOKUP)

# %%
# outer_caller_ws(ErrorType.INDEX)


# %%
def outer_caller_with_try_ws(exception_type: ErrorType = ErrorType.VALUE):
    print("outer_caller_ws(): before try")
    try:
        print("outer_caller_ws(): before calling")
        intermediate_fun_ws(exception_type)
        print("outer_caller_ws(): after calling")
    except Exception as error:
        print(f"<<< outer_caller_ws(): caught Exception [{error}]")
    print("outer_caller_ws(): after except")


# %%
outer_caller_with_try_ws(ErrorType.VALUE)

# %%
outer_caller_with_try_ws(ErrorType.LOOKUP)

# %%
outer_caller_with_try_ws(ErrorType.INDEX)

# %%
