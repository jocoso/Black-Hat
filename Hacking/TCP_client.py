import socket

#XXX: Assumptions made
#        -Our connection will always succeed
#        -The server expect for us to send data first
#        -The server will send us a response in a timely fashion

target_host = "0.0.0.0"
target_port = 9999

#Create a socket object
#AF_INET: We are going to be using standard ipv4 address or hostnames
#SOCK_STREAM: Describes it will be a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Make connection with the client
client.connect((target_host, target_port))

#Send some data 
client.send("GET / HTTP/1.1\NHost: google.com\r\n\r\n")

#Receive some data
response = client.recv(4096)

print(response)

