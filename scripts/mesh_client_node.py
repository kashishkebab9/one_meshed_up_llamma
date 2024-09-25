import meshtastic
from meshtastic.serial_interface import SerialInterface;
from pubsub import pub
import time
import datetime

import numpy as np

# local.sendText(text="hello", onResponse=callback, destinationId="!b47f5555");
local = SerialInterface();
time_stamps = []
def calculate_freq_stat(timestamp_list):
    intervals = np.diff(timestamp_list)
    avg_interval = np.mean(intervals)
    if avg_interval > 0:
        avg_frequency = 1.0/avg_interval
        print(f"Average Frequency: {avg_frequency}")

def onReceive(packet, interface): # pylint: disable=unused-argument
    """called when a packet arrives"""
    global time_stamps
    try:
        if "Packet" in packet["decoded"]["payload"].decode("utf-8"):
            print(f"Received: {packet["decoded"]["payload"]}")
            print(f"Timestamp Received: {packet["rxTime"]}")
            local.sendText("ACK")
            print("Sent Text!")
            time_stamps.append(packet["rxTime"])
            
        elif "DONE" in packet["decoded"]["payload"].decode("utf-8"):

            print("------------------------------")
            print("Final Stats:")
            print(f"Received Packets: {len(time_stamps)} / 100")
            calculate_freq_stat(time_stamps)
            local.close()
            

    except UnicodeDecodeError:
        pass

pub.subscribe(onReceive, "meshtastic.receive")

def callback(packet):
    # You will need to adapt this code
    print(repr(packet));
    if (packet.decoded.portnum == 1): # Filter for text messaging app only.
        print(f'received txt message - {packet.decoded.payload.decode("utf-8")}');

while True:
    pass

local.close()
