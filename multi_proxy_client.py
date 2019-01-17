#!/usr/bin/env python3
import socket
from multiprocessing import Pool

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = """GET / HTTP/1.0
HOST:www.google.com

"""

def connect_socket(addr):
    (family,socktype,proto,cannoname,sockaddr) = addr
    try:
        s = socket.socket(family,socktype,proto)
        # sockaddr is the server addr
        s.connect(sockaddr)
        # change strings to byte
        s.sendall(payload.encode())

        s.shutdown(socket.SHUT_WR)
        # a byte string
        full_data = b""
        while True:
            data = s.recv(BUFFER_SIZE)
            # if data is all received
            if not data:
                break
            full_data += data
        print(full_data)
    except Exception as e:
        print(e)
        print("DID not connect")
    finally:
        s.close()
        

def main():
    addr_info = socket.getaddrinfo(HOST,PORT,proto=socket.SOL_TCP)
    addr = addr_info[1]
    #print(addr_info)
    #connect_socket(addr)
    with Pool() as p:
        p.map(connect_socket,[addr for _ in range(1,50)])

if __name__=="__main__":
    main()

