# Course name: Intro to Security 2025
# Student name and id: Bror Hansen, broh
# Date: 06/10/26
# Part 3 - client

import sys
import socket
import ssl

if len(sys.argv) != 4:
    print('Usage: python client.py "message" host port')
    sys.exit(1)

message = sys.argv[1]
host = sys.argv[2]
port = int(sys.argv[3])
cafile = 'server_cert.pem'

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.check_hostname = False
context.load_verify_locations(cafile=cafile)

with socket.create_connection((host, port)) as sock:
    with context.wrap_socket(sock, server_hostname=None) as ssock:
        print('Connected, TLS:', ssock.version())
        ssock.sendall(message.encode('utf-8'))
        data = ssock.recv(4096)
        if data:
            print('Server reply:', data.decode('utf-8'))
        else:
            print('No reply')
