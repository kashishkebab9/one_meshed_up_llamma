from num import Enum

class PacketHeader(self):
    def __init__(self):
        # All header components are strings
        self.hash = None
        self.time_stamp = None
        self.num_total_packets = None
        self.packet_sequence = None
        self.packet_type = None

        # Byte Sizes, to ensure we don't go above the limit
        self.hash_size = 4
        self.timestamp_size = 4
        self.num_total_packet_size = 1
        self.packet_sequence_size = 1
        self.packet_type_size = 1

        self.packet_component_sizes = {
            "hash_size": self.hash_size,
            "timestamp_size": self.timestamp_size,
            "num_total_packet_size": self.num_total_packet_size,
            "packet_sequence_size": self.packet_sequence_size,
            "packet_type_size": self.packet_type_size
        }
    
    def SetHash(self, hash)
        # TODO Perform Stringification 
        self.hash = hash

    def SetTimestamp(self, time_stamp)
        # TODO Perform Stringification 
        self.hash = hash

    def SetNumTotalPackets(self, num_total_packets)
        # TODO Perform Stringification 
        self.hash = hash

    def SetPacketSequence(self, packet_sequence)
        # TODO Perform Stringification 
        self.hash = hash

    def SetPacketType(self, packet_type)
        # TODO Perform Stringification 
        self.hash = hash
