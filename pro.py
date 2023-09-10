import socket
import sys
import serial

import logging
log = logging.getLogger(__name__)

class Pro:
    def __init__(self, log, port, ip, device, baud, name):
        self.port=port
        self.ip=ip
        self.device=device
        self.baud=baud
        self.log=log
        self.name=name
    def start(self):
        self.ser = serial.Serial(self.device, self.baud, timeout=0)
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        server_address = (self.ip, self.port)
        self.log.info('starting up on ip \'{}\' port {}, '.format(*server_address)+"name: {}".format(self.name))
        self.sock.bind(server_address)
        self.sock.listen(1)
        self.log.info("Succesfully started.")
    def loop(self):
        self.log.info("Starting main loop for: {}".format(self.name))
        while True:

            self.log.info('waiting for a connection')
            connection, client_address = self.sock.accept()
            try:
                self.log.info('connection from' + str(client_address) + " on connection named " + self.name)
                connection.settimeout(0.1)
                while True:
                    try:
                        data = connection.recv(16)
                        if data == '': break
                        self.ser.write(data)
                    except KeyboardInterrupt:
                        connection.close()
                        sys.exit()
                    except Exception as e:
                        pass
                    received_data = self.ser.read(self.ser.inWaiting())
                    connection.sendall(received_data)
            except Exception as e:
                print(e)

            finally:
                #clean up connection
                connection.close()
