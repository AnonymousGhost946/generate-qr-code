import socket

target_host="123.3.4.1"
target_post=9997

#creat udp object
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#send some data
client.send(b"you will be hacked",(target_host,target_post))

#receive that data
data,addr=client.recvfrom(4096)

#print data
print(data.decode())

client.close()