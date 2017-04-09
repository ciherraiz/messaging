import pytest
from application.channel import Channel


@pytest.fixture
def sender_channel():
    ulr = 'tcp://192.168.55.112:5556'
    ch = Channel.create(endpoint=Channel.SENDER, url=ulr)
    return ch


def test_scheme(sender_channel):
    assert sender_channel.scheme == 'tcp'


def test_hostname(sender_channel):
    assert sender_channel.hostname == '192.168.55.112'


def test_port(sender_channel):
    assert sender_channel.port == 5556


def test_SENDER_value():
    assert Channel.SENDER == 'sender'


def test_RECEIVER_value():
    assert Channel.RECEIVER == 'receiver'


def test_PUBLISHER_value():
    assert Channel.PUBLISHER == 'publisher'


def test_SUBSCRIBER_value():
    assert Channel.SUBSCRIBER == 'subscriber'


def test_send_a_message(sender_channel):
    message = 'The message'
    with pytest.raises(NotImplementedError):
        sender_channel.send(message)
