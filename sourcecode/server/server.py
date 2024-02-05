import socket, pickle, sys, threading

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
#client_socket, client_address = server_socket.accept()
#print(f"Connection from {client_address}")

#connected_clients[0, 10] = client_address

#print(connected_clients)

# For storing
# type(b) gives <class 'bytes'>;
b = pickle.dumps(connected_clients)
 
# For loading
myEntry = pickle.loads(b)
#print(myEntry)

#server_socket.setblocking(False)

# Process data from the client

def handle_client(client_socket):
    while True:
        # Send data to the client
        message = "Hello from the server!"
        client_socket.send(message.encode())

quit = input()

while True:
    if quit.upper() == 'QUIT':
        sys.exit()

    try:
             # try to accept, if there is not, then nobody tries to connect
            client, client_address = server_socket.accept()
            #client.setblocking(False)

            connected_clients[client] = client_address
            client_ip, client_port = client_address

            print(f'"{client_ip}:{client_port}" has connected!')
            data = client.recv(1024)
            line = data.decode('UTF-8')    # convert to string (Python 3 only)
            line = line.replace("\n","")   # remove newline character
            print( line )
    except:
            for client in list(connected_clients.keys()):
                try:
                    data = client.recv(1024) # if it fails, the client doesn't send data
                    print(data)
                except:
                    continue

                client_address = connected_clients[client]
                client_ip, client_port = client_address

                if not data:
                    print(f'"{client_ip}:{client_port}" left the match!') # if the data contains nothing, the client sent the "QUIT" command
                    connected_clients.pop(client)
                    continue
    finally: # Simple timeout, stops the server after 30 seconds of inactivity
                if len(connected_clients) == 1:
                    client_thread = threading.Thread(target=handle_client, args=(client,)).start()
       
                


    # Receive the first message to identify the type (username or other)


    #else:

        #print("idk yet")
        # Handle other types of messages or ignore them
        
        # just wait normally

server_socket.close()