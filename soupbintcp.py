'''
Created on Jul 14, 2012

@author: jon
'''

from struct import unpack


def parse(data):
    while 1:
        # Parse packet length
        length_bytes = data.read(2)
        if not length_bytes:
            break
        packet_length = unpack('>H', length_bytes)[0]

        # Parse packet type (first byte of packet)
        packet_type = data.read(1)
        if not packet_type:
            break

        # Parse packet payload (rest of packet)
        packet_payload = data.read(packet_length)
        if not packet_payload:
            break

        yield Packet(packet_length, packet_type, packet_payload)


class Packet:

    def __init__(self, length, packet_type, payload):
        self.length = length
        self.packet_type = packet_type
        self.payload = payload

    def __repr__(self):
        return 'Packet: length=' + str(self.length) + \
            ' type=' + self.packet_type
            # Can't print payload as we know its binary
            # + \
            #' payload=' + self.payload
