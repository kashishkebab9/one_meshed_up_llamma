import meshtastic
import meshtastic.serial_interface
import time
from pubsub import pub
import lorem

can_continue = False
# TODO:
# keep track of the last id msg sent and check the ack on it
# the ACK msg has the id of the message it is acking in its
# requestid field

def OnReceive(packet):
    print(packet)

    global can_continue

    print("Received ACK!")
    can_continue = True

interface = meshtastic.serial_interface.SerialInterface()

pub.subscribe(OnReceive, "meshtastic.receive")

for i in range(3):
    print("Sending Text...")

    # large payload
    #interface.sendText(f"Packet {i}: {lorem.paragraph()[:223 ]}", destinationId="!01475a49")

    # small payload
    interface.sendText(f"Packet {i}", destinationId="!b47f5555", wantAck=True)
    while not can_continue:
        pass
    time.sleep(1)
    can_continue = False


# ensuring message doesnt get lost
for i in range(5):
    interface.sendText(f"DONE", destinationId="!01475a49")
