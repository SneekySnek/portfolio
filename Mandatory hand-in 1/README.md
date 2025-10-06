# Quick start

Start the server (listens on port 7007):

```powershell
py server.py
```

Send a message with the client:

```powershell
py client.py "test message" localhost 7007
```

Expected client output:

```
Connected, TLS: TLSv1.3
Server reply: ACK
```

Generate a self-signed server certificate/key (PowerShell, requires OpenSSL):

```powershell
openssl req -x509 -newkey rsa:2048 -keyout server_key.pem -out server_cert.pem -days 365 -nodes -subj "/CN=localhost"
```

Place `server_cert.pem` and `server_key.pem` in the project root before starting `server.py`.

That's it.