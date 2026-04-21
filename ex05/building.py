import string
import sys


def count_text(text: str) -> tuple[int, int, int, int, int, int]:
    """Count character categories in the given text."""
    total = len(text)
    upper = len(list(filter(str.isupper, text)))
    lower = len(list(filter(str.islower, text)))
    punctuation = len(list(filter(lambda c: c in string.punctuation, text)))
    spaces = len(list(filter(str.isspace, text)))
    digits = len(list(filter(str.isdigit, text)))


    return total, upper, lower, punctuation, spaces, digits


def main():
    """Parse input text and print text statistics."""
    try:
        argc = len(sys.argv) - 1

        if argc > 1:
            print("AssertionError: more than one argument is provided")
            return

        if argc == 0 or (argc == 1 and sys.argv[1] == ""):
            text = input("What is the text to count?\n")
            text += "\n"
        else:
            text = sys.argv[1]
        total, upper, lower, punctuation, spaces, digits = count_text(text)
        print(f"The text contains {total} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punctuation} punctuation marks")
        print(f"{spaces} spaces")
        print(f"{digits} digits")
    except Exception:
        print("AssertionError: the arguments are bad")
        return


if __name__ == "__main__":
    main()