import socket
from _thread import *
import sys

#LocalIP of the computer running the server
server = "192.168.0.42"
#We know that port 5555 is an unused port, so we can safely use it for our program
port = 5555

#Note til self - Find ud af hvad argumenterne i socket.socket() gør
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#For safety and errorhandling, we try if the port is unused and can bind to the socket, together with the server
try:
    sock.bind((server, port))
except socket.error as e:
    str(e)

#sock.listen() "opens" up the port so that we can start connecting to it. The argument is the max number of connections
sock.listen(20)

print("Waiting for connection, Server started")

#Everything before this is esentially the server, without functionality

def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""

    while True:
        try:
            #Data recieved from whoever is connectet, in bits - 2048 bits (Ved ikke en skid om bits). If we get an error with this, we can just multiply the bits by x
            #Larger amount of bits = longer recieve time (2048 is almost instant)
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            #Breaks the connection if we dont get any information from the client
            if not data:
                print("Disconnectet")
                break
            else:
                print("Recieved: ", reply)
                print("Sending: ", reply)
            #Encodes string reply, into a byte object
            conn.sendall(str.encode(reply))
        #Breaks in case of anything unexpectet happening
        except:
            break
    print("Lost connection")
    conn.close()


while True:
    #Accepts incomming connections to the server, and stores the connection (conn - what is connectet) and the address (IP address)
    conn, addr = sock.accept()
    print ("Connected to: " , addr)
    
    #Start a new thread for each connection - Explenation: This while loop always runs, while it makes threads on the threaded_client method
    start_new_thread(threaded_client, (conn, ))