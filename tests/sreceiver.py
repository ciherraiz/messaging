from technology.msocket.schannel import SChannel

url = "tcp://0.0.0.0:5000"
receiver = SChannel.create(endpoint=SChannel.RECEIVER, url=url)
msg = receiver.receive()
print(msg.body)
receiver.close()
