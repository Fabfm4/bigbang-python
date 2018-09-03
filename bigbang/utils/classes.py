from .console import Console


class CommandClass(object):

    def __init__(self, *args, **kwargs):
        valid, elements, _ = self.verify_args_command(*args, **kwargs)
        if valid:
            self.construct(elements, *args, **kwargs)

        else:
            Console.show_fail('ERROR:')
            Console.show_fail(_)

    def construct(self, parse_elements, *args, **kwargs):
        raise NotImplementedError('Method is not implement')

    def verify_args_command(self, *args, **kwargs):
        raise NotImplementedError('Method is not implement')
