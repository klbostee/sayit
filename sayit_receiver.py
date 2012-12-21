import sys
import os
import socket
import struct
import StringIO


class Worker(object):

    def __init__(self, multicast_group='224.3.29.71', server_address=('', 44444)):
        self.notificationSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.notificationSock.bind(server_address)

        # Tell the operating system to add the socket to the multicast group
        # on all interfaces.
        group = socket.inet_aton(multicast_group)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        self.notificationSock.setsockopt(socket.IPPROTO_IP,
                                         socket.IP_ADD_MEMBERSHIP,
                                         mreq)

    def run(self):
        while True:
            message, address = self.notificationSock.recvfrom(1024)
            os.system("say {0}".format(message))


Worker().run()
