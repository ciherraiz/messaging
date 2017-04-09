import socket
from application.channel import (Channel, BaseChannel, SenderChannel,
                                 ReceiverChannel)
from application.message import Message


class BaseSChannel(BaseChannel):
        def __init__(self,
                     endpoint: str=None,
                     url: str=None):

                    super(BaseSChannel, self).__init__(endpoint, url)

                    if self.scheme != 'tcp':
                        raise ValueError('Wrong scheme definition')


class SSenderChannel(BaseSChannel, SenderChannel):

    def __init__(self,
                 endpoint: str=None,
                 url: str=None):

                super(SSenderChannel, self).__init__(endpoint, url)

                # create a socket
                self._connector = socket.socket(socket.AF_INET,
                                                socket.SOCK_STREAM)
                # connect
                self._connector.connect((self._hostname, self._port))

    def send(self, message: Message):
        self._connector.send(message.body.encode())

    def close(self):
        self._connector.close()


class SReceiverChannel(BaseSChannel, ReceiverChannel):

    MAX_CONNECTIONS = 10
    BUFFER_SIZE = 1024

    def __init__(self,
                 endpoint: str=None,
                 url: str=None):

                super(SReceiverChannel, self).__init__(endpoint, url)

                # create a socket
                self._connector = socket.socket(socket.AF_INET,
                                                socket.SOCK_STREAM)
                # bind socket
                self._connector.bind((self._hostname, self._port))
                print('bind: {} {}'.format(self._hostname, self._port))
                # start listening
                self._connector.listen(self.MAX_CONNECTIONS)

    def receive(self) -> Message:

        # accept connection
        conn, addr = self._connector.accept()
        print('Connected with {} {}\n'.format(addr[0], str(addr[1])))
        # get message from sender
        data = conn.recv(self.BUFFER_SIZE).decode()
        conn.close()

        if data:
            return Message(data)
        else:
            return None

    def close(self):
        self._connector.close()

class SChannel(Channel):
    @classmethod
    def create(cls, endpoint: str, url: str) -> BaseSChannel:
        if endpoint == cls.SENDER:
            return SSenderChannel(endpoint=endpoint, url=url)
        if endpoint == cls.RECEIVER:
            return SReceiverChannel(endpoint=endpoint, url=url)
