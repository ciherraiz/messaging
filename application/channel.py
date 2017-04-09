from urllib.parse import urlparse
from application.message import Message


class BaseChannel:
        def __init__(self,
                     endpoint: str=None,
                     url: str=None):

                    self._endpoint = endpoint
                    try:
                        parsed_url = urlparse(url)
                        self._url = url
                        self._scheme = parsed_url.scheme
                        self._hostname = parsed_url.hostname
                        self._port = parsed_url.port
                    except:
                        raise ValueError('Invalid URL connector')

        @property
        def scheme(self) -> str:
            return self._scheme

        @property
        def hostname(self) -> str:
            return self._hostname

        @property
        def port(self) -> int:
            return self._port


class SenderChannel(BaseChannel):

    def send(self, message: Message):
        raise NotImplementedError('Send method is not implemented yet')


class Channel:
    SENDER = 'sender'
    RECEIVER = 'receiver'
    PUBLISHER = 'publisher'
    SUBSCRIBER = 'subscriber'

    @classmethod
    def create(cls, endpoint: str, url: str) -> BaseChannel:
        if endpoint == cls.SENDER:
            return SenderChannel(endpoint=endpoint, url=url)
