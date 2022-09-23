#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

#get host information
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip

#send data to server
def send_data(serversocket, payload):
    print("Sending payload")    
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print ('Send failed')
        sys.exit()
    print("Payload sent successfully")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print("Starting proxy server")
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(2)
        
        host = "www.google.com"
        payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
        buffer_size = 4096
        
        #continuously listen for connections
        while True:
            conn, addr = proxy_start.accept()
            print("Connected by", addr)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                
                print("Connecting to Google")
                remote_ip = get_remote_ip(host)
                proxy_end.connect((remote_ip , 80))
                p = Process(target=handle_echo, args=(proxy_end, addr, conn))
                p.daemon = True
                p.start()
                print("Started Process ", p)
            
            conn.close()

def handle_echo(proxy_end, addr, proxy_start):
    time.sleep(10)
    send_full_data = proxy_start.recv(BUFFER_SIZE)
    print(f"SEnding received data {send_full_data}to google")
    proxy_end.sendall(send_full_data)
    proxy_end.shutdown(socket.SHUT_WR)
    data = proxy_end.recv(BUFFER_SIZE)
    print(f"Sending received data {data} to client")
    proxy_start.send(data)

if __name__ == "__main__":
    main()
