#!/usr/bin/env python
""""
Prototype program to communicate with SplashDrone 4

"""
import socket 

__author__ = "Daniel Philbey"
__copyright__ = "Copyright 2022, Daniel Philbey"
__credits__ = []

__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Daniel Philbey"
__email__ = "daniel.philbey@gmail.com"
__status__ = "Prototype"

HOST = "192.168.2.1"  # The server's hostname or IP address
PORT = 2022  # The port used by the server

# Custom devices can be set in range 0xc8-0xfe
devices = {0x01:'Flight Control', 0x02:'Remote Controller', 0x03:'Gimbal', 0x04:'App', 0xff:'Report', 0x00:'Share', 0xdd:'Dans Device'}

msgIDs = {
    0x1d:'Flight Status Report',
    0x34:'Flight Mission Control',
    0x34:'Acknowledged'
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(64)


print(f"Received {data!r}")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        if s.recv(1) == 0xa6:                       # wait for start flag
            print(' Start Message '.center(64, '='))
            packLen, msgID, src, dst = s.recv(4)    # get info
            print(f'Msg: {msgIDs[msgID]}')
            print(f'Src: {devices[src]}')
            print(f'Dst: {devices[dst]}')
            buff = s.recv(packLen - 5)              # get remaining data
            payload = buff[:-1]
            chksum = buff[-1]
            print(f'Checksum: {chksum}')
            print(' Payload '.center(64, '='))
            print(payload.decode())
            print(' End Message '.center(64, '='))
            print()



        



def decode(data):
    list=data.split(0xa6)
    processed=[]

    for item in list:
        processed.append({'length':item[0], 'msgID':item[1], 'src':item[2], 'dst':item[3], 'payload':item[4:-2], 'checksum':item[-1]})
    print(processed)







class msg:
    start=0xa6

    __slots__='start', 'msgID', 'src', 'dst', 'payload'
    def __init__(self, payload, msgID, src=0xc9, dst=0x01):
        packLength=len(payload.encode()+7)

    def __get__(self):
        return self.msg.encode()






