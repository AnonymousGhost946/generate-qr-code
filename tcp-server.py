import socket

# Server setup
server_ip = 'yout ip address'  

server_port = 9999  # Choose any available port

# Create socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to the IP and port
server.bind((server_ip, server_port))

# Start listening with a maximum queue of 5 connections
server.listen(5)
print(f"[*] Listening on {server_ip}:{server_port}")

while True:
    # Accept incoming connection
    client_socket, addr = server.accept()
    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
    
    # Receive data from the client
    data = client_socket.recv(1024)
    print(f"[*] Received: {data.decode('utf-8')}")
    
    # Send a response back to the client
    client_socket.send(b"Message received")
    
    # Close the connection
    client_socket.close()
