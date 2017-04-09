import pytest
from technology.msocket.schannel import SChannel


@pytest.fixture
def sender_schannel():
    url = "tcp://127.0.0.1:5000"
    ch = SChannel.create(endpoint=SChannel.SENDER, url=url)
    return ch


@pytest.fixture
def receiver_schannel():
    url = "tcp://127.0.0.1:5000"
    ch = SChannel.create(endpoint=SChannel.RECEIVER, url=url)
    return ch


def test_tcp_scheme():
    url = "tkp://127.0.0.1:5000"
    with pytest.raises(ValueError):
        SChannel.create(endpoint=SChannel.SENDER, url=url)


# def test_schannel_send_a_message(sender_schannel, receiver_schannel):
#    message = 'The message'
#    sender_schannel.send(message)
