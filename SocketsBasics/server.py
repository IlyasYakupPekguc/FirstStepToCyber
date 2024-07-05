import socket

Host = "192.168.1.27"
Port = 66666
# host = socket.gethostbyname(socket.gethostname()) #This will get the ip address of the host automatically
# look out if the user has a virtual box or a vpn, it will get the ip address of the virtual box or vpn
# we need the ip adress of "Ethernet adapter Ethernet" or "Wireless LAN adapter Wi-Fi"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Inet is the address family for IPv4 so internet, and SOCK_STREAM is the socket type for TCP , this is only the connection socket
server.bind((Host,Port)) #This will bind the server to the host and port and with the bind we set up the server
server.listen(5) #This will listen for connections, the number is the number of connections that can be queued before the server starts to reject the next coming connections

while True:
    communication_socket, adress = server.accept() #this is the communication socket, this is the actual connection between the server and the client 
    print(f"Connection from {adress} has been established")
    message = communication_socket.recv(1024).decode("utf-8") #This will receive the message from the client
    print(f"Message from client: {message}")
    communication_socket.send("Message received".encode("utf-8")) #we need to encode because we dont send strings, we send bytes
    communication_socket.close() #This will close the connection
    print(f"Connection with {adress} has been closed")



