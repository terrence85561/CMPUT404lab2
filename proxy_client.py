#!/usr/bin/env python3
import socket

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
        #print(full_data)
    except:
        print("DID not connect")
    finally:
        s.close()
        

def main():
    addr_info = socket.getaddrinfo(HOST,PORT,proto=socket.SOL_TCP)
    print(addr_info)
    addr = addr_info[1]
    connect_socket(addr)

if __name__=="__main__":
    main()

