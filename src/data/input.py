import socket
import time

# Declare Constant Variables
HOST = '0.0.0.0' 
PORT = 3333 
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))


def getdata():
    data = s.recvfrom(BUFFER_SIZE) # getdata
    if data:
        datalist = list(data)
        strdata = str(datalist[0])
        strdata = strdata[6:-1]
        accelerationvalues = strdata.replace("\\x00",",")
        accelerationlist = list(accelerationvalues.split(","))
        return(accelerationlist) # Return


