import socket

SRV_ADDR = input("Enter the Server Address: ")
SRV_PORT = int(input("Enter the Server Port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((SRV_ADDR, SRV_PORT))

print("Connection Established")

message = input("Enter a message to send: ")

s.sendall(message.encode())
s.close()