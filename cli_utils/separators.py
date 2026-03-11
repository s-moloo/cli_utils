def print_separator():
        print("*" * 30)

def print_char_separator(char):
    print(char[0] * 30)

def print_custom_separator(char, length):
    if length <= 0:
        print("")
        return

    print(char[0] * length)

def print_labeled_separator(label, char="*", width=30):
    print(label.center(width, char[0]))

def print_box(message, char="*"):
    width = len(message) + 4
    border = char[0] * width

    print(border)
    print(f"{char[0]} {message} {char[0]}")
    print(border)

def print_dog():
    """
    Prints a colored ASCII dog in the terminal.
    """

    BROWN = "\033[33m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    dog = [
        r"      /^-----^\ ",
        r"      V  o o  V",
        r"       |  Y  |",
        r"        \ Q /",
        r"        / - \ ",
        r"       |    \ ",
        r"       |     \     )",
        r"       || (___\===="
    ]

    for i, line in enumerate(dog):
        if i <= 3:
            color = BROWN   # head
        else:
            color = YELLOW  # body
        print(color + line + RESET)




