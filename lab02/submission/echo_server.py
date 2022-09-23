#!/usr/bin/env python3
from ast import arg
import socket
import time
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            
            #recieve data, wait a bit, then send it back
            p = Process(target=handle_echo, args=(conn,))
            p.daemon = True
            p.start()
            conn.close()

def handle_echo(conn):
    time.sleep(10)
    full_data = conn.recv(BUFFER_SIZE)
    conn.sendall(full_data)

if __name__ == "__main__":
    main()
