import socket

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect(('B1:21:81:2B:A0:1C', 2))

s.send(bytearray([0x01, 0x04, 0x00, 0x45, 0x00, 0x49, 0x00, 0x02]))

c = s.recv(1)
while(c):
    print(c)
    c = s.recv(1)

s.close()
