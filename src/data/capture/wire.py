from os import fdopen
import serial
import time
import csv

# Data through serial

csvlist = []
mindatapoints = 2500

# Set Serial and File Constants
port = "/dev/cu.usbserial-0001" #serial port of Arduino
baud = 115200 #board runs at 115200 baud
fileName="data.csv" #name of the CSV file generated

# Connect to Device
ser = serial.Serial(port, baud)
print("Connected to Device:" + port)

file = open(fileName, "a")
print("Created file")


#Ask user for input regarding impact
userinput = input("is this an Impact?: ")

if userinput == "t" or userinput == "y" or userinput == "yes":
    #impact = True
    csvlist.append("True")
else:
    #impact = False
    csvlist.append("False")

# Wait for Start
input("Press Enter to start")

#Countdown
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")


points = 0
t_end = time.time() + 2
starttime = time.time()


while time.time() < t_end:
    #display the data to the terminal
    getData=str(ser.readline())
    data=getData[2:6]
    rawcount = time.time() - starttime

    ts = round(rawcount, 5)

    print(str(ts) + ", " + data)
    csvlist.append(data)
    points = points +1



if points > mindatapoints:
    difference =  points - mindatapoints
    
    print("Removing {} extra data points from beginning".format(str(difference)))
    for i in range(difference):
        csvlist.pop(1)

    with open('data.csv', 'a', newline='') as csvobject:
        writer_object = csv.writer(csvobject)
        writer_object.writerow(csvlist)
        csvobject.close()


elif points < mindatapoints:
    print("Only {} points collected. Trashing data...".format(str(points)))
    
    with open('wastedata.csv', 'a', newline='') as csvobject:
        writer_object = csv.writer(csvobject)
        writer_object.writerow(csvlist)
        csvobject.close()
    
    print("Done.")










    

'''
    #add the data to the file
    file = open(fileName, "a") #append the data to the file
    file.write(data + "\\n") #write data with a newline
    
    #close out the file
    file.close()
'''

