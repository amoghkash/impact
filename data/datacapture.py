from os import fdopen
import serial
import time

port = "/dev/cu.usbserial-0001" #serial port of Arduino
baud = 115200 #board runs at 115200 baud
fileName="data.csv" #name of the CSV file generated

ser = serial.Serial(port, baud)
print("Connected to Arduino port:" + port)

file = open(fileName, "a")
print("Created file")

t_end = time.time() + 2
starttime = time.time()


while time.time() < t_end:
    #display the data to the terminal
    getData=str(ser.readline())
    data=getData[2:6]
    rawcount = time.time() - starttime

    print(str(ts) + ", " + data)
    

    #add the data to the file
    #file = open(fileName, "a") #append the data to the file
    #file.write(data + "\\n") #write data with a newline
    
    #close out the file
    #file.close()

