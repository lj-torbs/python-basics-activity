def greet(name):
    return f"Hello, {name}!"


def clean(text):
    return text.strip().title()


def shout(text):
    return text.upper() + "!"


def dialogue(speaker, line):
    return f'{speaker} says: "{line}"'


def receipt():
    return "Item\tPrice\nPen\t10"


def initials(full_name):
    return "".join(word[0].upper() for word in full_name.split())


if __name__ == "__main__":
    print(greet("Ana"))
    print(clean("  juan dela cruz "))
    print(shout("hey"))
    print(dialogue("Maria", "Hi"))
    print(receipt())
    print(initials("juan dela cruz"))