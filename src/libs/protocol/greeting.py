'''
Handle the basic protocol greeting (connecting to the update server,
asking for updates and a validity check, and getting the list of any
new sub-servers/fallback which should be used.
'''
import socket
import struct
import libs.socks


class Greeter():
    def __init__(self, address):
        # TODO: switch to socks socket
        # self.sock = libs.socks.socksocket()
        self.sock = socket.socket()
        self.sock.connect((address, 31337))

        # Say hello to the server :>
        self.sock.send(b'\x00')

        # Parse the list of servers
        data = self.sock.recv(8184)
        servers = struct.unpack('16s16s16s16s', data)

        print('Alternate servers:\n %s\n %s\n %s' % servers[0:3])
        print('Web server:\n %s' % servers[3])

        # Ask for/get news
        self.sock.send(b'\x01')
        data = self.sock.recv(16384)
        news = data.decode()

        print('\n--- news ---')
        print(news)
