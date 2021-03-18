import socket

#Class responsible for connecting to the server
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Has to be the same IP as in the server class
        self.server = "192.168.0.42"
        #Same port as in the server class
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id =self.connect()
        print(self.id)

    def connect(self):
        try:
            print("")
            self.client.connect(self.addr)
            #Sends validation of the client connected - Ties into  conn.send(str.encode("Connected")) from the server class (Line 27)
            return self.client.recv(2048).decode()
        except:
            pass

    #Sends a string "data"
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

n = Network()
print(n.send("Hello"))
print(n.send("Penis"))