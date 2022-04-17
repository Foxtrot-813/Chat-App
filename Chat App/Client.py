import socket
import sys
import time

port = 7777
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', port))

connection = True

while connection:
    client.send(input("Send: ").encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg.lower() == 'quit':
        connection = False
        print("Connection terminated")
        time.sleep(3)
        sys.exit()
    else:
        print(f"Received message: {msg}")
