import sys


def main():
    """
        Parse one optional integer argument
        and print whether it is odd or even.
    """
    try:
        argc = len(sys.argv) - 1

        if argc == 0:
            return
        if argc > 1:
            print("AssertionError: more than one argument is provided")
            return

        try:
            value = int(sys.argv[1])
        except Exception:
            print("AssertionError: argument is not an integer")
            return

        if value % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except Exception:
        return


if __name__ == "__main__":
    main()
