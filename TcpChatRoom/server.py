import threading
import socket

host = "127.0.0.1" # localhost
port = 55555 #dont choose well known ports (ranging frtom 1 - 10k)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen() # listen for incoming connections

clients = []
nicknames = []

def broadcast(message):
    for client in clients: #for every client in the list of clients
        client.send(message) #send the message to the client

def handle(client): #we are trying to get a message from the client, if we get an error, we remove the client from the list of clients and the error is that if the client disconnects
    while True:
        try:
            message = client.recv(1024) #recieve message from client (1024 bytes)
            broadcast(message) #broadcast the message to all clients
        except:
            index = clients.index(client) #get the index of the client
            clients.remove(client) #remove the client from the list of clients     
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii')) #broadcast the message to all clients ,when the server send a message we need to encode it to ascii
            nicknames.remove(nickname)
            break

def receive(): #accept connections from clients this is the main function
    while True:
        client , adress = server.accept() #accept the connection
        print(f"Connected with {str(adress)}") 

        client.send('NICK'.encode('ascii')) #send the message to the client to get the nickname
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname) #append the nickname to the list of nicknames
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f'{nickname} joined the chat!'.encode('ascii') ) #when the server send a message we need to encode it to ascii
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,)) #create a thread for the client
        thread.start()

print("Server is listening...")
receive() 






