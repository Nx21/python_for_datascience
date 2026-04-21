import sys

from ft_filter import ft_filter


def parse_args(argv: list[str]) -> tuple[str, int]:
    """Validate CLI arguments and return text and threshold."""
    if len(argv) != 3:
        raise ValueError

    text = argv[1]
    try:
        int(text)
    except ValueError:
        pass
    else:
        raise ValueError

    n = int(argv[2])
    return text, n


def main():
    """Filter and print words with length strictly greater than N."""
    try:
        text, n = parse_args(sys.argv)
        words = [word for word in text.split()]
        result = ft_filter(lambda w: len(w) > n, words)
        print(result)
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()