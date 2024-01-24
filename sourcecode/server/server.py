import socket
import sys

HOST = ''  
PORT = 7976

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('# Socket created')

# Establish socket on the desired port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('# Bind failed. ')
    sys.exit()

print('# Socket bind successful')

# Begin listening on the socket
s.listen(10)
print('# Socket now in listening mode on port :', PORT)

# Awaiting client connection
conn, addr = s.accept()
print('# Established connection with ' + addr[0] + ':' + str(addr[1]))

# Process data from the client
while True:     
    data = conn.recv(1024)
    line = data.decode('UTF-8')    # convert to string (Python 3 only)
    line = line.replace("\n","")   # remove newline character
    print( line )     

s.close()