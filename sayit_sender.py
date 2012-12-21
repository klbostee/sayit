import socket
import struct
import sys


multicast_group = ('224.3.29.71', 44444)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
sent = sock.sendto(" ".join(sys.argv[1:]), multicast_group)
sock.close()
