from enum import Enum

class PacketType(Enum):
    REQ = 1 # Req from Robot to Base (LLM Input)
    REP = 2 # Rep from LLM to go from Base to Robot
    FDBK = 3  # Continous messages to indicate current status of Robot

class PacketFooter:
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


        # Total Packet Size
        self.packet_footer_size = ( self.hash_size + 
                                    self.timestamp_size + 
                                    self.num_total_packet_size +
                                    self.packet_sequence_size +
                                    self.packet_type_size )

        self.packet_sizes = {
            "hash_size": self.hash_size,
            "timestamp_size": self.timestamp_size,
            "num_total_packet_size": self.num_total_packet_size,
            "packet_sequence_size": self.packet_sequence_size,
            "packet_type_size": self.packet_type_size,
            "packet_footer_size": self.packet_footer_size
        }
    
    def SetHash(self, hash):
        # Gets set within CreatePacket
        self.hash = hash 

    def SetTimestamp(self, time_stamp):
        # Gets set at time of sending the msg
        self.time_stamp = time_stamp

    def SetNumTotalPackets(self, num_total_packets):
        # Gets set within CreatePacket
        self.num_total_packets = num_total_packets

    def SetPacketSequence(self, packet_sequence):
        # Gets set within CreatePacket
        self.packet_sequence = packet_sequence

    def SetPacketType(self, packet_type):
        # Gets set within CreatePacket
        self.packet_type = packet_type

if __name__ == '__main__':
    packet_footer = PacketFooter()
    print(packet_footer.packet_sizes["packet_footer_size"])
