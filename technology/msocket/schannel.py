from application.channel import Channel, BaseChannel, SenderChannel
from application.message import Message


class BaseSChannel(BaseChannel):
        def __init__(self,
                     endpoint: str=None,
                     connector: str=None):

                    super(BaseSChannel, self).__init__(endpoint, connector)

                    if self.scheme != 'tcp':
                        raise ValueError('Wrong scheme definition')


class SSenderChannel(BaseSChannel):
    def send(self, message: Message):
        raise NotImplementedError('Send method is not implemented yet')


class SChannel(Channel):
    @classmethod
    def create(cls, endpoint: str, connector: str) -> BaseSChannel:
        if endpoint == cls.SENDER:
            return SSenderChannel(endpoint=endpoint, connector=connector)
