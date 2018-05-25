from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ServerEndpoint, TCP4ClientEndpoint
from twisted.internet.error import CannotListenError
from twisted.internet.endpoints import connectProtocol

import p2pClient as p2pClient
from p2pClient import MyFactory, MyProtocol, UDPClientProtocol

ncfactory = MyFactory()
def connect():
<<<<<<< HEAD
    # # host = "52.14.183.26" #адрес сервера
=======
    # # host = "52.14.170.246" #адрес сервера
>>>>>>> 5f0a82f9399bad38be08dd6064249e04f73f07e7
    # host = "localhost"
    # port = 5006 #порт сервера
    #
    # try:
    #     endpoint = TCP4ServerEndpoint(reactor, 5005)
    #     endpoint.listen(ncfactory)
    #     print("LISTEN")
    # except CannotListenError:
    #     print("[!] Address in use")
    #     raise SystemExit

<<<<<<< HEAD
    t = reactor.listenUDP(5005, UDPClientProtocol("52.14.183.26", 5006))
=======
    t = reactor.listenUDP(5006, UDPClientProtocol())
>>>>>>> 5f0a82f9399bad38be08dd6064249e04f73f07e7
    reactor.run()

if __name__ == "__main__":
    connect()
