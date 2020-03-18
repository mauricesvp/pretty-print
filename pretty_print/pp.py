"""Pretty Print."""
import sys

RESET = "\x1b[0m"
BLACK = "\x1b[30m"
RED = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[33m"
BLUE = "\x1b[34m"
MAGENTA = "\x1b[35m"
CYAN = "\x1b[36m"
WHITE = "\x1b[37m"


def print_ok(string: str):
    print_(GREEN, "OK", string)


def print_failed(string: str):
    print_(RED, "FAIL", string)


def print_warning(string: str):
    print_(YELLOW, "WARN", string)


def print_info(string: str):
    print_(CYAN, "INFO", string)


def print_flag(string: str):
    print_(MAGENTA, "FLAG", string)


def print_(color: str, tag: str, string: str):
    sys.stdout.write("[" + color + tag.center(4) + RESET + "] " + string + "\n")
