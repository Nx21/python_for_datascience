import os
import sys


def ft_tqdm(lst: range) -> None:
    """Yield items from lst while displaying a tqdm-like progress bar."""
    total = len(lst)

    if total == 0:
        return

    for index, elem in enumerate(lst, start=1):
        try:
            columns = os.get_terminal_size().columns
        except OSError:
            columns = 80

        percent = int(index / total * 100)
        suffix = f"| {index}/{total}"
        prefix = f"{percent:3d}%|["
        available = columns - len(prefix) - len("]") - len(suffix)
        bar_width = max(1, available)

        filled = int(index / total * bar_width)
        if index < total:
            if filled <= 0:
                bar_content = ">" + " " * (bar_width - 1)
            else:
                bar_content = "=" * (filled - 1) + ">"
                bar_content += " " * (bar_width - filled)
        else:
            bar_content = "=" * bar_width

        line = f"\r{percent:3d}%|[{bar_content}]| {index}/{total}"
        sys.stderr.write(line)
        sys.stderr.flush()
        yield elem
