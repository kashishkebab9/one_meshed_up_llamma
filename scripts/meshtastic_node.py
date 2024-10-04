import meshtastic 
import meshtastic.serial_interface
import time
from pubsub import pub
from termcolor import colored, cprint


class mesh_node:
    def __init__(self, id):
        self.meshtastic_id = id 
        # pub.subscribe(self.packet_respond, "meshtastic.receive")

    def packetize_string(self, string_input:str) -> str:
         """Converts a string into the desired packet for Meshtastic experiments
            The max size a string can be 237 bytes - our custom packet header size
            Hash Length - 32 bits : 4 bytes
            Epoch Timestamp - 32 bits: 4 bytes
            Number of total Packets: 1 Byte (256 consecutive packets is max for one string) 
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

        try:
            string_input = string_input + "a"
            print(string_input)

        except TypeError:
            cprint("ERROR: Input to packetize_string method incorrect!", "red")
            cprint(f"Input: {string_input}", "red")
            cprint(f"Type: {type(string_input)}", "red")
            return 0

        # TODO: Check for size of string






if __name__ == '__main__':
    mn = mesh_node("a")
    string_input = "hello"
    mn.packetize_string(string_input)
    
