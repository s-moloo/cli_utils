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




