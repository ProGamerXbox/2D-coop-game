import socket, pickle, sys, threading, time

HOST = ''  
PORT = 7976

connected_clients = {}
client_id = {}


playerList = []

class player:
    def __init__(self, client, client_id):
         self.client = client
         self.id = client_id

    def pos(self, x, y):
        self.x = x
        self.y = y
    
    def isYou(self, client):
        if self.client == client:
             return True
        else:
             return False
    def send(self, message):
        self.client.send(message.encode('utf-8'))
         

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('# Socket created')

server_socket.bind((HOST, PORT))

print('# Socket bind successful')

# Begin listening on the socket
server_socket.listen(10)
print('# Socket now in listening mode on port :', PORT, HOST)

server_socket.setblocking(0)

# Awaiting client connection
#client_socket, client_address = server_socket.accept()
#print(f"Connection from {client_address}")

#connected_clients[0, 10] = client_address

#print(connected_clients)

# For storing
# type(b) gives <class 'bytes'>;

#print(myEntry)

#server_socket.setblocking(False)

# Process data from the client

#def handle_client(client_socket):
#    while True:
#        # Send data to the client
#        message = "Hello from the server!"
#        client_socket.send(message.encode())

def sendToPlayer(idOrigin, message):

    for truc in playerList:
        print(sys.getsizeof(message))
        if truc.id != idOrigin:
            print(f'sending {message}')
            truc.sendall(message)
        else:
            truc.sendall("0".encode)

while True:

#    if quit.upper() == 'QUIT':
#        sys.exit()

    
    try:    
            # try to accept, if there is not, then nobody tries to connect
            client, client_address = server_socket.accept()
            client.setblocking(0)
    except:
        pass
    else:
        try:
            #client.setblocking(False)
            playerList.append(player(client, len(client_id)))
            connected_clients[client] = client_address
            client_ip, client_port = client_address
            client_id[client] = len(client_id)
            print(f'"{client_ip}:{client_port}" has connected!')
            data = client.recv(24)
        except:
            raise Exception("erro")
        line = data.decode('UTF-8')    # convert to string (Python 3 only)
        line = line.replace("\n","")   # remove newline character
        print( line )
        try:
            dataToSend = f'{client_id[client]}'.encode("UTF-8")
            client.send(dataToSend)
        except:
            raise Exception("failed to send id to client")
    finally:
            for client in list(connected_clients.keys()):
                try:
                    data = client.recv(1024) # if it fails, the client doesn't send data
                    id = client_id[client]
                    sendToPlayer(id, data)
                except:
                    continue

                client_address = connected_clients[client]
                client_ip, client_port = client_address

                if not data:
                    print(f'"{client_ip}:{client_port}" left the match!') # if the data contains nothing, the client sent the "QUIT" command
                    connected_clients.pop(client)
                    continue


    # Receive the first message to identify the type (username or other)


    #else:

        #print("idk yet")
        # Handle other types of messages or ignore them
        
        # just wait normally

server_socket.close()
