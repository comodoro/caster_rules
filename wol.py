import socket
import struct
import sys

def wake(addr, mac, port=7):
    mac_bytes = ''.join(mac.split(':')) if ':' in mac else mac
    if len(mac_bytes) != 6*2:
        raise ValueError('Invalid MAC')
    hwa = bytearray.fromhex(mac_bytes)
    msg = '\xff' * 6 + hwa * 16
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(msg, (addr, port))
    s.close()

if __name__ == '__main__':
    wake(sys.argv[1], sys.argv[2])