import meshtastic 
import meshtastic.serial_interface
import time
from pubsub import pub
import sys
from termcolor import colored, cprint


import lorem


from PacketHeader import PacketHeader

class MeshNode:

    def __init__(self, id):
        self.meshtastic_id = id 

        print(f"Initializing MeshNode with ID: {id}")
        self.packet_header = PacketHeader()

        # Byte Sizes for each component of the Packet Header
        # TODO: Make this an interation on the dictionary for robust error checking
        print("============================================================")
        print(f"Number of Bytes for the Packet Header: {self.packet_header.packet_sizes['packet_header_size']}")
        print(f"    Number of Bytes for the Hash: {self.packet_header.packet_sizes['hash_size']}")
        print(f"    Number of Bytes for the Time Stamp: {self.packet_header.packet_sizes['timestamp_size']}")
        print(f"    Number of Bytes for the Number of Total Packets: {self.packet_header.packet_sizes['num_total_packet_size']}")
        print(f"    Number of Bytes for the Packet Sequence Number: {self.packet_header.packet_sizes['packet_sequence_size']}")
        print(f"    Number of Bytes for the Packet Type: {self.packet_header.packet_sizes['packet_type_size']}")

        self.max_string_size= 237 - self.packet_header.packet_sizes["packet_header_size"] 
        print("============================================================")
        print(f"Maximum str size for msgs: {self.max_string_size}")

        print("Done Initializing!")
        print(".")
        print(".")
        print(".")

    def CreateMsg(self, string_input: str):
        string_input = string_input.encode("utf-8")
        sizeof_str = len(string_input)
        print(string_input)
        print(f"Size of Input String: {sizeof_str} bytes")

        # Container for either single or list of Strings, depending on following conditional
        output_string = []
        if sizeof_str > self.max_string_size:
            print(colored("String input is greater than max string size! Performing fragmentation...", 'yellow'))
            output_string = self.SeparateString(string_input)
        else:
            output_string.append(string_input)
        
    def SeparateString(self, string_input: str) -> [str]:
        """ Takes a string larger than the self.max_string_size and fragments 
        it out to a list of substrings

        Parameters
        ----------
        string_input
            String encoded as utf-8 greater than self.max_string_size

        Returns
        -------
        [str]
            List of strings, each ready for packetization
        """



    def CreatePacket(self, string_input:str) -> str:
        """ Converts a string into the desired packet for Meshtastic experiments
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
    string_input = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    mn.CreateMsg(string_input)
    
