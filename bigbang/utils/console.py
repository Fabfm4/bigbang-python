from .colors import bcolors


class Console(object):

    @staticmethod
    def show_description(text):
        print(bcolors.BLUE + text + bcolors.ENDC)

    @staticmethod
    def show_ok(text):
        print(bcolors.GREEN + text + bcolors.ENDC)

    @staticmethod
    def show_fail(text):
        print(bcolors.RED + text + bcolors.ENDC)
