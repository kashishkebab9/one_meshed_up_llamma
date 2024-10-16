import meshtastic 
import meshtastic.serial_interface
import time
from pubsub import pub
import sys
from termcolor import colored, cprint
import hashlib
from PacketFooter import PacketFooter, PacketType

class MeshNode:

    def __init__(self, id):
        self.meshtastic_id = id 

        print(f"Initializing MeshNode with ID: {id}")
        self.packet_footer = PacketFooter()

        # Byte Sizes for each component of the Packet Footer
        # TODO: Make this an interation on the dictionary for robust error checking
        print("============================================================")
        print(f"Number of Bytes for the Packet Footer: {self.packet_footer.packet_sizes['packet_footer_size']}")
        print(f"    Number of Bytes for the Hash: {self.packet_footer.packet_sizes['hash_size']}")
        print(f"    Number of Bytes for the Time Stamp: {self.packet_footer.packet_sizes['timestamp_size']}")
        print(f"    Number of Bytes for the Number of Total Packets: {self.packet_footer.packet_sizes['num_total_packet_size']}")
        print(f"    Number of Bytes for the Packet Sequence Number: {self.packet_footer.packet_sizes['packet_sequence_size']}")
        print(f"    Number of Bytes for the Packet Type: {self.packet_footer.packet_sizes['packet_type_size']}")
        print("============================================================")

        self.max_string_size= 237 - self.packet_footer.packet_sizes["packet_footer_size"] 
        print(f"Maximum str size for msgs: {self.max_string_size}")

        # Length of the hash in bits
        # We can expect a collision after approx
        # math.sqrt(2**HASH_LENGTH_BITS)
        # https://preshing.com/20110504/hash-collision-probabilities/

        self.HASH_LENGTH = 5
        self.HASH_LENGTH_BITS = self.HASH_LENGTH * 8

        print("Done Initializing!")
        print(".")
        print(".")
        print(".")

    def CreateMsg(self, string_input: str):
        """ Takes a string and outputs full meshtastic packet with footer, only missing field will be timestamp_size
        since that needs to be appended at time of Send()

        Parameters
        ----------
        string_input
            Desired String to send in Meshtastic Network

        Returns
        -------
        [str]
            List of strings, each packetized
        """
        string_input = string_input.encode("utf-8")
        sizeof_str = len(string_input)
        print(f"String Input: {string_input}")
        print(f"Size of Input String: {sizeof_str} bytes")

        # Container for either single or list of Strings, depending on following conditional
        string_container = []
        if sizeof_str > self.max_string_size:
            print(colored("String input is greater than max string size! Performing fragmentation...", 'yellow'))
            string_container = self.SeparateString(string_input)
        else:
            string_container.append(string_input)

        # TODO: Determine all other PacketFooter Parameters
        for string_msg in string_container:
            self.CreatePacket(string_msg)


        
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
        # TODO: Check if string is ENCODED
        if len(string_input) < self.max_string_size:
            return [string_input]

        last_packet_size = len(string_input) % self.max_string_size
        num_full_packets = (len(string_input) - last_packet_size) / self.max_string_size

        if not num_full_packets.is_integer():
            print(colored("ERROR: Value is not whole, packet calculation has occured", 'red'))
            print(colored(f"Value: {num_full_packets}", 'red'))

        output_string_list = []
        for i in range(int(num_full_packets)):
            string_val = string_input[:self.max_string_size]
            string_input = string_input[self.max_string_size:]
            output_string_list.append(string_val)

        output_string_list.append(string_input)
        return output_string_list

    def CreatePacket(self, string_input:str, num_packets:int, packet_sequence:int, packet_type:PacketType ) -> str:
        """ Converts a string into the desired packet for Meshtastic experiments
            The max size a string can be 237 bytes - our custom packet footer 
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
        # TODO: Check if string is ENCODED
        # if not isinstance(string_input, str):
        #     raise TypeError(f"Not a Valid input!\nInput: {string_input}")
        packet_footer = PacketFooter()

        # Set Hash
        hash = hashlib.sha256(string_input)
        hash_s = str(hash.hexdigest()[:self.HASH_LENGTH])
        packet_footer.SetHash(hash_d)

        # Set the Num Packets
        if num_packets > packet_footer.MAX_NUM_PACKETS:
            raise ValueError("Too Many packets for this transmission!")
        num_packets_s = str(num_packets)
        packet_footer.SetNumTotalPackets(num_packets_s)

        # Set the Packet Sequence
        if packet_sequence > num_packets - 1:
            raise ValueError("Packet Sequence Index greater than this transmission num packets")
        packet_sequence_s = str(packet_sequence)
        packet_footer.SetPacketSequence(packet_sequence_s)




if __name__ == '__main__':
    mn = MeshNode("a")
    string ="AA"
    string = string.encode("utf-8")
    mn.CreatePacket(string, 1, 0, PacketType.REQ)

    # 500 char input
    # Lorem was adding confusion, just want to make the char->byte mapping 
    # explicit with this string
    
