#! /usr/bin/env python3
'''
binaryslave: a fully interactive, online hacking game
'''
print('''
[[ Binary Slave ]]

You are a slave to your computer.
  There is only 10 rules to this slavery.

    0) If it is in binary, it is the truth.
    1) There will be no exceptions to rule 0.

''')

import libs.config
import libs.socks
import libs.validity

import libs.protocol.greeting


class Main():
    def __init__(self):
        self.config = libs.config.MainConfig()
        libs.socks.setdefaultproxy(libs.socks.PROXY_TYPE_SOCKS5,
                                   self.config.get('proxy', 'toraddress'),
                                   self.config.get_int('proxy', 'torport'))

        self.server = self.config.get('main', 'server')
        greeter = libs.protocol.greeting.Greeter(self.server)


if __name__ == '__main__':
    main = Main()
