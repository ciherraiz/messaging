import socket
from application.channel import Channel, BaseChannel, SenderChannel
from application.message import Message


class BaseSChannel(BaseChannel):
        def __init__(self,
                     endpoint: str=None,
                     url: str=None):

                    super(BaseSChannel, self).__init__(endpoint, url)

                    if self.scheme != 'tcp':
                        raise ValueError('Wrong scheme definition')
                    else:


class SSenderChannel(BaseSChannel):

    def __init__(self,
                 endpoint: str=None,
                 url: str=None):

                super(SSenderChannel, self).__init__(endpoint, url)

                # create a socket
                self._connector = socket.socket(socket.AF_INET,
                                                socket.SOCK_STREAM)

                self._connector.connect((self._hostname, self._port))

    def send(self, message: Message):
        raise NotImplementedError('Send method is not implemented yet')


class SChannel(Channel):
    @classmethod
    def create(cls, endpoint: str, url: str) -> BaseSChannel:
        if endpoint == cls.SENDER:
            return SSenderChannel(endpoint=endpoint, url=connector)
