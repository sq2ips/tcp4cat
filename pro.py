import socket
import sys
import serial

import logging
log = logging.getLogger(__name__)

class Pro:
    def __init__(self, logger, port, ip, device, baud, name):
        self.port=port
        self.ip=ip
        self.device=device
        self.baud=baud
        self.logger=logger
        self.name=name
    def start(self):
        self.ser = serial.Serial(self.device, self.baud, timeout=0)
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        server_address = (self.ip, self.port)
        if(self.ip != ''):
            self.logger.info('starting up from ip \'{}\' port {}, '.format(*server_address)+"name: {}".format(self.name))
        else:
            self.logger.info('starting up from ip \'{}\' (any) port {}, '.format(*server_address)+"name: {}".format(self.name))
        self.sock.bind(server_address)
        self.sock.listen(1)
        self.logger.info("Succesfully started.")
    def loop(self):
        self.logger.info("Starting main loop for: {}".format(self.name))
        while True:

            self.logger.info('waiting for a connection')
            connection, client_address = self.sock.accept()
            try:
                self.logger.info('connection from ' + str(client_address) + " on connection named " + self.name)
                connection.settimeout(0.1)
                while True:
                    try:
                        data = connection.recv(16)
                        if data == '': break
                        self.ser.write(data)
                    except Exception as e:
                        self.logger.warning(e)
                    received_data = self.ser.read(self.ser.inWaiting())
                    connection.sendall(received_data)
            except Exception as e:
                print(e)

            finally:
                #clean up connection
                connection.close()
