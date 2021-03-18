import socket

#Class responsible for connecting to the server and sending/recieving data
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Has to be the same IP as in the server class
        self.server = "192.168.0.42"
        #Same port as in the server class
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            print("")
            self.client.connect(self.addr)
            #Sends validation of the client connected - Ties into  conn.send(str.encode("Connected")) from the server class (Line 27)
            return self.client.recv(2048).decode()
        except:
            pass

    #Sends a string "data" to the server
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            #Returns the decoded version of the data its trying to send
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

#n = Network()
