from time import sleep
from SX127x.LoRa import *
from SX127x.board_config import BOARD

class LoRaReceiver(LoRa):
    def __init__(self):
        BOARD.setup()
        super(LoRaReceiver, self).__init__(board_config=BOARD)
        self.set_mode(MODE.STDBY)  # Set mode to standby
        self.data_length_rx = 0
        self.destination_rx = 0
        self.localAddress_rx = 0
        self.rssiNode = 0
        
    def on_rx_done(self):
        self.clear_irq_flags(RxDone=1)
        payload = self.read_payload(nocheck=True)
        print(f"Received: {payload}")
        self.localAddress_rx = payload[0]
        self.destination_rx = payload[1]
        self.data_length_rx = payload[2]
        self.rssiNode = self.get_pkt_rssi_value()
        print(" destination  :" ,hex(self.destination_rx))
        print(" localAddress :" ,hex(self.localAddress_rx))
        print(" data         :" ,self.received_data)
        print(" RSSI	 :" ,str(self.rssiNode))

    def receive(self):
        self.set_mode(MODE.RXCONT)  # Set mode to continuous receive
        while True:
            sleep(1)  # Wait for messages

if __name__ == '__main__':
    lora = LoRaReceiver()
    lora.receive()
    lora.set_mode(MODE.STDBY)
    lora.set_pa_config(pa_select=1)
    lora.set_freq(923.0)
