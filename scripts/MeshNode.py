import meshtastic 
import meshtastic.serial_interface
import time
from pubsub import pub
from termcolor import colored, cprint


class MeshNode:

    def __init__(self, id):
        self.meshtastic_id = id 

        # Byte Sizes for each component of the Packet Header
        self.packet_header = {}


        self.packet_header_size = ( self.hash_size + 
                                    self.timestamp_size + 
                                    self.num_total_packet_size +
                                    self.packet_sequence_size +
                                    self.packet_type_size )

        print(f"Packet Header Size: {self.packet_header_size} Bytes")
        print(f"    Hash Size: {self.hash_size}")
        print(f"    Time Stamp Size: {self.timestamp_size}")
        print(f"    Total Number of Packet Size: {self.num_total_packet_size}")
        print(f"    Packet Sequence Number Size: {self.packet_sequence_size}")
        print(f"    Packet Type Size: {self.packet_type_size}")
        # Byte Size Limit for String Message

        # pub.subscribe(self.packet_respond, "meshtastic.receive")


    def SeparateString(self, string_input: str) -> [str]:
        pass

    def CreatePacket(self, string_input:str) -> str:
        """Converts a string into the desired packet for Meshtastic experiments
            The max size a string can be 237 bytes - our custom packet header 
            size
            Hash Length - 32 bits : 4 bytes
            Epoch Timestamp of Transmission - 32 bits: 4 bytes
            Number of total Packets: 1 Byte (256 consecutive packets is max for
            one string) 
            Packet Sequence number: 1 Byte
            Packet Type - ACK, REQ, REP, FDBK: 1 byte


        Parameters
        ----------
        string_input
            Test input string

        Returns
        -------
        str
            New, packetized string ready for comms

        """
        if not isinstance(string_input, str):
            raise TypeError(f"Not a Valid input!\nInput: {string_input}")




if __name__ == '__main__':
    mn = MeshNode("a")
    string_input = "hello"
    mn.CreatePacket(string_input)
    
