#!/usr/bin/python

import socket
import sys
import serial

#open serial port
ser = serial.Serial('/dev/ttytest0', 115200, timeout=0)
#create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

#bond to the port. Don't use localhost to accept external connections
server_address = ('', 8888)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

#listen
sock.listen(1)

#loop
while True:
    #waits for a new connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        #continously send from serial port to tcp and viceversa
        connection.settimeout(0.1)
        while True:
            try:
                data = connection.recv(16)
                if data == '': break
                ser.write(data)
            except KeyboardInterrupt:
                connection.close()
                sys.exit()
            except Exception as e:
                pass
            received_data = ser.read(ser.inWaiting())
            connection.sendall(received_data)
    except Exception as e:
        print(e)

    finally:
        #clean up connection
        connection.close()
