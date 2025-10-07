# Course name: Intro to Security 2025
# Student name and id: Bror Hansen, broh
# Date: 06/10/26
# Part 3 - server

import socket
import ssl

HOST = '0.0.0.0'
PORT = 7007
CERTFILE = 'server_cert.pem'
KEYFILE = 'server_key.pem'

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)

print('Starting TLS server on port', PORT)

with socket.socket() as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(1)
    while True:
        conn, addr = sock.accept()
        with context.wrap_socket(conn, server_side=True) as ssock:
            print('Connection from', addr, 'TLS:', ssock.version())
            print('Cipher:', ssock.cipher())
            data = ssock.recv(4096)
            msg = data.decode('utf-8')
            print('Received:', msg)
            ssock.sendall(b'ACK')
            