import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-..... ",
    "7": "--.... ",
    "8": "---... ",
    "9": "----. ",
}


def is_valid_text(text: str) -> bool:
    """Return True when all characters can be encoded in Morse."""
    return all(char in NESTED_MORSE for char in text)


def encode_to_morse(text: str) -> str:
    """Encode a validated uppercase text string into Morse code."""
    return "".join(NESTED_MORSE[char] for char in text).rstrip()


def main():
    """Parse input and print Morse code or the required assertion message."""
    try:
        if len(sys.argv) != 2:
            print("AssertionError: the arguments are bad")
            return

        text = sys.argv[1].upper()
        if not is_valid_text(text):
            print("AssertionError: the arguments are bad")
            return

        print(encode_to_morse(text))
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()