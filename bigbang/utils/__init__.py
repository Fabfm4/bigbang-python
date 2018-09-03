class Properties(object):

    @staticmethod
    def get_list_tecnologies():
        return ('odoo', 'django', 'flask')

    @staticmethod
    def get_json_init(tecnology='<name_tecnology>'):
        return {
            'tecnology': tecnology
        }

    @staticmethod
    def get_file_json_init():
        return 'bigbang.json'
