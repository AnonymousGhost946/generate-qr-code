import socket
target_host="google.com"
target_port=80

#making client object
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connecting socket
client.connect((target_host,target_port))

#send some data
client.send(b"GET HTTP/nHOST /1.1 \n\r\n\r")

#receive data
receiveData=client.recv(4096)

#print that data
print(receiveData.decode())
client.close()
