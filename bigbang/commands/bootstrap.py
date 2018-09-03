from bigbang.utils.console import Console
from bigbang.utils import Properties
from bigbang.utils.classes import CommandClass
import json
import os
import sys
import urllib2


class Bootstrap(CommandClass):

    def __init__(self, *args, **kwargs):
        Console.show_description('*** Read bigbang json file...  ***')
        super(Bootstrap, self).__init__(*args, **kwargs)
        Console.show_ok('OK')

    def construct(self, parse_elements, *args, **kwargs):
        action = getattr(
            self,
            'build_{0}'.format(parse_elements['json_init']['tecnology'])
        )
        action(parse_elements, *args, **kwargs)

    def verify_args_command(*args, **kwargs):
        current_path = os.getcwd()
        path_abs = '{0}/{1}'.format(
            current_path,
            Properties.get_file_json_init()
        )

        if not os.path.exists(path_abs):
            return False, None, 'file bigbang.json doesn\'t exists'

        with open(path_abs, 'r') as f:
            try:
                json_init = json.loads(f.read())
                if 'tecnology' not in json_init:
                    return (
                        False,
                        None,
                        'field tecnology is not in bigbang.json'
                    )

                return (
                    True,
                    {
                        'json_init': json_init,
                        'project_path': current_path
                    },
                    None
                )

            except ValueError:
                return False, None, 'bigbang.json format is not correct'

    def build_odoo(self, parse_elements, *args, **kwargs):
        config_path = '{0}/config'.format(parse_elements['project_path'])
        custom_addons_path = '{0}/custom_addons'.format(
            parse_elements['project_path']
        )
        data = urllib2.urlopen('https://gist.githubusercontent.com/Fabfm4/ced07b21d7461d88551d4926159d45d8/raw/afbdcbcd458072ae6fbca4456aa39b8e70e60ab7/.odoorc.bk').read()
        data = data.split('\n')
        content_odoorc_file = []
        for line in data:
            content_odoorc_file.append(line)

        if not os.path.isdir(config_path):
            Console.show_description('Create config folder.......')
            os.makedirs(config_path)
            with open('{0}/.odoorc'.format(config_path), 'w+') as f:
                for item in content_odoorc_file:
                    print >> f, item

            Console.show_ok('OK')

        if not os.path.isdir(custom_addons_path):
            Console.show_description('Create custom_addons folder.......')
            os.makedirs(custom_addons_path)
            Console.show_ok('OK')
