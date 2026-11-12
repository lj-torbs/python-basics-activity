"""Task 2: Strings, escape sequences, f-strings, string methods  (lessons 1.3 to 1.6)

Complete each function. Keep the function names and parameters.
Run the checks with:  python -m unittest tests.test_tasks.Task2Strings -v
"""


def greet(name):
    """Return 'Hello, <name>!' using an f-string."""
    return f"Hello, {name}!"


def clean(text):
    """Remove spaces at both ends and make it Title Case."""
    return text.strip().title()


def shout(text):
    """Return the text in UPPER CASE followed by '!'."""
    return text.upper() + "!"


def dialogue(speaker, line):
    """Return: <speaker> says: "<line>"."""
    return f'{speaker} says: "{line}"'


def receipt():
    """Return a two line string using escape sequences."""
    return "Item\tPrice\nPen\t10"


def initials(full_name):
    """Return the capital first letters of each word."""
    return "".join(word[0].upper() for word in full_name.split())


if __name__ == "__main__":
    print(greet("Ana"))
    print(clean("  juan dela cruz "))
    print(shout("hey"))
    print(dialogue("Maria", "Hi"))
    print(receipt())
    print(initials("juan dela cruz"))