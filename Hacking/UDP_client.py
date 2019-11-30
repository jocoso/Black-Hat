import socket

target_host = "127.0.0.1"
target_port = 80

#Create socket object
#SOCK_DGRAM: Describes it will be a UDP client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#NOTE: no need to make a connection
#Send some data
client.sentto("AAABBBCCC", (target_host, target_port))

#receive some data
data, addrs = client.recvfrom(4069)

print data