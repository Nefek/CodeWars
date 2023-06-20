def validate_hello(greetings):
    a = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    for i in a:
        if i in greetings.lower(): return True
    return False
