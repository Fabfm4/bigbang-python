from bigbang.utils.console import Console
from bigbang.utils import Properties
from bigbang.utils.classes import CommandClass
import json
import os


class Init(CommandClass):

    def __init__(self, *args, **kwargs):
        Console.show_description('*** Creating json init file...  ***')
        super(Init, self).__init__(*args, **kwargs)
        Console.show_ok('OK')

    def construct(self, parse_elements, *args, **kwargs):
        with open(parse_elements['path_file'], 'w+') as f:
            f.write(json.dumps(
                Properties.get_json_init(parse_elements['tecnology']),
                indent=4,
                sort_keys=True
            ))

    def verify_args_command(self, *args, **kwargs):
        tecnology = '<name_tecnology>'
        if len(args) == 3:
            if args[2] in Properties.get_list_tecnologies():
                tecnology = args[2]
            else:
                return False, None, '{0}: that option doesn\'t exists'.format(
                    args[2]
                )

        if len(args) > 3:
            return False, None, '{0}: that option isn\'t valid'.format(
                args[3]
            )

        current_path = os.getcwd()
        path_abs = '{0}/{1}'.format(
            current_path,
            Properties.get_file_json_init()
        )
        if os.path.isfile(path_abs):
            return False, None, 'file bigbang.json already exists'

        parse_elements = {
            'tecnology': tecnology,
            'path_file': path_abs
        }
        return True, parse_elements, None
