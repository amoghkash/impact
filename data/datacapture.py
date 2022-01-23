from curses import raw
from os import fdopen
import serial
import time
import csv


csvlist = []

port = "/dev/cu.usbserial-0001" #serial port of Arduino
baud = 115200 #board runs at 115200 baud
fileName="data.csv" #name of the CSV file generated

ser = serial.Serial(port, baud)
print("Connected to Arduino port:" + port)

file = open(fileName, "a")
print("Created file")


#Ask user for input regarding impact
userinput = input("is this an Impact?: ")

if userinput == "t":
    #impact = True
    csvlist.append("Yes")
else:
    #impact = False
    csvlist.append("Yes")

# Wait for Start
input("Press Enter to start")

#Countdown
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")

for i in range(20):
        print(str(ser.readline()))

t_end = time.time() + 2
starttime = time.time()

while time.time() < t_end:
    #display the data to the terminal
    
    
    getData=str(ser.readline())
    data=getData[2:6]
    rawcount = time.time() - starttime

    ts = round(rawcount, 5)


    print(str(ts) + ", " + data)
    locallist = [ts, data]
    csvlist.append(locallist)

print(csvlist)

with open('data.csv', 'a', newline='') as csvobject:
    writer_object = csv.writer(csvobject)
    writer_object.writerow(csvlist)
    csvobject.close()
    

'''
    #add the data to the file
    file = open(fileName, "a") #append the data to the file
    file.write(data + "\\n") #write data with a newline
    
    #close out the file
    file.close()
'''

