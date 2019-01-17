#!/usr/bin/env python3

import socket

# it means listening to local host
HOST = ""
PORT = 8001
Buffer_SIZE = 1024

def main():
    #create socket
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        #allows to reuse same bind port
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind((HOST,PORT))
        s.listen(1) # make socket listen


        #listen forever for connections
        while True:
            conn,addr = s.accept() # accept any incoming connections and store the addr connects with me
            print(addr) #Q4
            full_data = b""

            while True:
                data = conn.recv(Buffer_SIZE)
                if not data:
                    break
                full_data += data
                #print(full_data)
                #send data back as response
                conn.sendall(full_data)
if __name__ == "__main__":
    main()