#we are looking for open ports to check if the server is vulnerable to attacks

import socket
import threading
from queue import Queue

target = "İP Address of the target" 
queue = Queue() #we will use this to store the ports we want to scan and so that the threads don't scan the same port
open_ports = [] #store the open ports


def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Inet is the address family for IPv4 so internet, and SOCK_STREAM is the socket type for TCP
        sock.connect(('target',port)) #connect to the target on the port
        return True #if the port is open and we connected to it
    
    except:
        return False #if the port is closed and we didn't connect to it
    
# for portNumber in range(1,1025): #scan the first 1024 ports
#     result = portscan(portNumber)
#     if(result):
#         print(f"Port {portNumber} is open!")
#     else:
#         print(f"Port {portNumber} is closed!")
#this way is really slow, we can use threading to make it faster (see below)

def fill_queue(port_list): #port list work FIFO
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get() #get the port from the queue
        if portscan(port):
            print(f"Port {port} is open!")
            open_ports.append(port) # add ports to the open_ports list
        #we only want to print the open ports, we don't care about the closed ports cuz there are too many of them 
        #we do not need an else statement

port_list = range(1,1025)
fill_queue(port_list)

thread_list = [] #list of threads is easier to use than manually assigning 10 threads

for t in range(100): #we will use 100 threads
    thread = threading.Thread(target=worker) # we are running the worker function in the thread
    thread_list.append(thread) # add the thread to the list

for thread in thread_list:
    thread.start() #start the thread

for thread in thread_list:
    thread.join() #wait for all threads to finish    

print(open_ports) #print the open ports we only want to print the open ports when all threads are finished 

#NOTE: i do not have open ports so the list will be empty
