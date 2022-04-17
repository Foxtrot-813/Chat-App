import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 7777
server.bind(('localhost', port))
server.listen()
client, address = server.accept()
connection = True
print("Connection established.")

while connection:
    msg = client.recv(1024).decode('utf-8')
    if msg.lower() == 'quit':
        connection = False
    else:
        print(f"Received message: {msg}")
    client.send(input("Send: ").encode('utf-8'))
