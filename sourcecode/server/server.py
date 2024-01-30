import socket
import sys

HOST = ''  
PORT = 7976

connected_clients = {}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('# Socket created')

server_socket.bind((HOST, PORT))

print('# Socket bind successful')

# Begin listening on the socket
server_socket.listen(10)
print('# Socket now in listening mode on port :', PORT, HOST)

# Awaiting client connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

# Process data from the client
while True:     
    data = client_socket.recv(1024)
    line = data.decode('UTF-8')    # convert to string (Python 3 only)
    line = line.replace("\n","")   # remove newline character
    print( line )

    # Receive the first message to identify the type (username or other)
    message_type = client_socket.recv(1024).decode('utf-8')

    if message_type == 'username':
        # Receive username from the client
        username = client_socket.recv(1024).decode('utf-8')
        print(f"Username received from {client_address}: {username}")

        # Store the connected device information in the dictionary
        connected_clients[client_address[0]] = {'username': username, 'socket': client_socket}
        print(f"Connected devices: {connected_clients}")

    else:

        print("idk yet")
        # Handle other types of messages or ignore them
        
        # just wait normally

server_socket.close()
