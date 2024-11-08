from ..generic import say_hello as say_hello_en


_greetings = {
    "de": "Hallo",
    "en": "Hello",
    "es": "Hola",
    "fr": "Bonjour",
    "it": "Ciao",
    "pt": "Olá",
}

_goodbyes = {
    "de": "Tschüss",
    "en": "Bye",
    "es": "Adiós",
    "fr": "Au revoir",
    "it": "Ciao",
    "pt": "Tchau",
}


def say_hello(name="", language="en"):
    """Says hello to a person."""
    if language == "en":
        say_hello_en(name)
        return

    greeting = _greetings[language]
    if name == "":
        print(f"{greeting}!")
    else:
        print(f"{greeting}, {name}!")


def say_goodbye(name="", language="en"):
    """Says goodbye to a person."""
    goodbye = _goodbyes[language]
    if name == "":
        print(f"{goodbye}!")
    else:
        print(f"{goodbye}, {name}!")
