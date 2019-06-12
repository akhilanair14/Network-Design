import socket
import time
import os

class client:
    def __init__(self):
        self.s = socket(AF_INET, SOCK_DGRAM)
        self.r = socket(AF_INET, SOCK_DGRAM)
        self.d = ('localhost',15000)
        self.r.bind(self.d)
        self.r.settimeout(0.5)
        self.corrupt = False
        a = os.path.abspath(file)
        n = os.path.dirname(a)
        os.chdir(n)
        self.sequence = 0
    def send_data(self):
        fileRead=open('123.jpg','rb')
        message = fileRead.read(1024)

        while message != b"":
            packet = message
            s.sendto(packet, server_addr)
            message = fileRead.read(1024)
            fileRead.close()
            for refer, segment in enumerate(segments):
                self.send_segment(segment,refer)
                self.sequence = 1 - self.sequence
            print('segment successfully')
            self.close()
            break
    def send_segment(self):
        self.send_data('start')
        for segment in self.segment:
            self.send_data(segment)
        self.send_data('end')

