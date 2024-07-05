import socket

HOST = "192.168.1.27" #This is the ip address of the server
PORT = 66666

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #This is the client socket
socket.connect((HOST,PORT)) #This will connect to the server, we use connect not bind because we are the client

socket.send("Hello server".encode("utf-8")) #This will send the message to the server
print(socket.recv(1024).decode("utf-8")) #This will receive the message from the server

