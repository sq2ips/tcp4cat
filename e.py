import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 12345)  # replace with your server address and port
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    
    print('sending {!r}'.format(message))
    
    sock.sendall(message.encode('utf-8'))

finally:
    print('closing socket')
    sock.close()
