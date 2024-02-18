#!/usr/bin/env python3
###################################################################################
# This server represents the main socket driven Composability Manager main        #
#  "Copyright 2023 OpenFabrics Alliance. All rights reserved."                    #
###################################################################################

import sys
import socket
import json
import logging
import threading

def logging():
    pass

def ERROR(error_string):
    print({error_string})
    log_send ("Closing: {socket.gethostname()} Composability Manager on: {SERVERADDRESS}) due to error")
            
    return 1

n = len(sys.argv)

if n >= 2:
    PORT=int(sys.argv[1])
else:
    ERROR("Usage python3 composability_manager.py <Port Number>")

SERVERIP=socket.gethostbyname(socket.gethostname())
SERVERADDRESS=(SERVERIP,PORT)

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(SERVERADDRESS)


def client_connection(conn,addr):
    
    conn.close()

def main():
    print ("[Starting] ",{socket.gethostname()}," Composability Manager on: ",{SERVERADDRESS})
    server.listen()
    while True:
            conn, addr=server.accept()
            thread=threading.Thread(target=command_parser,args=(conn,addr))
            thread.start()


main()

