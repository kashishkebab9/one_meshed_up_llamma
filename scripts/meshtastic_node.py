import meshtastic 
import meshtastic.serial_interface
import time
from pubsub import pub
from termcolor import colored, cprint


class mesh_node:
    def __init__(self, id):
        self.meshtastic_id = id 
        # pub.subscribe(self.packet_respond, "meshtastic.receive")

    def packetize_string(self, string_input):
        """
        Converts a string desired to send to a proper packet with timestamp and
        sha256 hash

        Args:
            string_input: input string to convert to message

        Returns:
            Packetized string

        Raises:
            KeyError: Raises an exception.
        """
        try:
            string_input = string_input + "a"
            print(string_input)

        except TypeError:
            cprint("ERROR: Input to packetize_string method incorrect!", "red")
            cprint(f"Input: {string_input}", "red")
            cprint(f"Type: {type(string_input)}", "red")
            return 0


if __name__ == '__main__':
    mn = mesh_node("a")
    string_input = "hello"
    mn.packetize_string(string_input)
    
