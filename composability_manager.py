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
import composability_manager_parser

HEADER=64
FORMAT='utf-8'
PORT=9876
SERVER=socket.gethostbyname(socket.gethostbyname(socket.gethostname()))
ADDR=(SERVER,PORT)
DISCONNECT_MESSAGE="!DISCONNECT"

def ERROR(error_string):
    print({error_string})
    sys.exit() 

paramnum = len(sys.argv)
print (f"the number of parameters passed in is",paramnum)
if paramnum < 2:
    ERROR("Usage python3 composability_manager.py <Port Number>")
PORT=int(sys.argv[1])

#PORT=9499
SERVERIP=socket.gethostbyname(socket.gethostname())
SERVERADDRESS=(SERVERIP,PORT)

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(SERVERADDRESS)


def client_connection(conn,addr):
    

    print(f"[NEW CONNECTION] {addr} connected.")
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            print("message length is: ",(msg_length));
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg==DISCONNECT_MESSAGE:
                connected=False
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()

def main():
    print ("[Starting] ",{socket.gethostname()}," Composability Manager on: ",{SERVERADDRESS})
    server.listen()
    while True:
            conn, addr=server.accept()
            thread=threading.Thread(target=client_connection,args=(conn,addr))
            thread.start()


main()

