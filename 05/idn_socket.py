import socket

HOST = '192.168.0.221'
PORT = 5025 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'*IDN?\n')
    data = s.recv(1024)

print('Received', data.decode())