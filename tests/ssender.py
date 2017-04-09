from technology.msocket.schannel import SChannel
from application.message import Message

url = "tcp://127.0.0.1:5000"
sender = SChannel.create(endpoint=SChannel.SENDER, url=url)
sender.send(Message('hello my friend'))
sender.close()
