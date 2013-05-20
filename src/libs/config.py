'''
Load and parse configuration files automatically
'''
import configparser
import os

CONFIG_DIR = os.path.join(os.getenv('HOME'), '.binaryslave')


class MainConfig():
    def __init__(self):
        self.path = os.path.join(CONFIG_DIR, 'main.ini')
        self.config = configparser.ConfigParser()
        self.config.read(self.path)

        if not self.config.has_section('main'):
            self.config.add_section('main')
            self.config.set('main', 'server', 'localhost')  # TODO: real addr
            self.config.add_section('proxy')
            self.config.set('proxy', 'toraddress', 'localhost')
            self.config.set('proxy', 'torport', 9050)
            self.save()

    def save(self):
        '''
        Save any changes to the configuration file.
        '''
        if os.path.exists(CONFIG_DIR):
            with open(self.path, 'w') as configfp:
                self.config.write(configfp)
        else:
            os.mkdir(CONFIG_DIR, 0o750)
            with open(self.path, 'w') as configfp:
                self.config.write(configfp)

    def get(self, section, option):
        return self.config.get(section, option)

    def get_int(self, section, option):
        self.config.getint(section, option)
