import socket

# Target is the localhost IP and port where the server is running
target_host = "your ip address"  
target_port = 9999  # Same port as the server

# Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect((target_host, target_port))

# Send a message
message = "Haaa you are hacked"
client.send(message.encode('utf-8'))

# Receive the response from the server
response = client.recv(4096)

# Print the response
print(f"[*] Server response: {response.decode('utf-8')}")

# Close the connection
client.close()
