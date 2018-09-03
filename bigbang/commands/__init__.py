import sys
from .help import help
from .init import Init
from .bootstrap import Bootstrap

main_options = ('init', 'bootstrap', 'run')


def str_to_class(str):
    return getattr(sys.modules[__name__], str.capitalize())


def main():
    arguments = sys.argv
    if len(arguments) > 0:
        if arguments[1] in main_options:
            _class = str_to_class(arguments[1])
            _class(*arguments)
        else:
            if arguments[0] not in ('-h', '--help'):
                print("error")
            help()
    else:
        print("error")
        help()
