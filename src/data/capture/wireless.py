from os import fdopen
import time
import csv
import data.input
import data.processing as processing
import logger.logger as logger
import time
import variable.const as constant

# Data through serial

csvlist = []
mindatapoints = 1000

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


while(time.time() < t_end):
    rawdata = data.input.getdata()
    data = processing.normalize(rawdata)
    magnitudevalue = float(processing.getmagnitude(data))

    rawcount = time.time() - starttime

    ts = round(rawcount, 5)

    print(str(ts) + ", " + data)
    csvlist.append(magnitudevalue)
    points = points +1



if points > mindatapoints:
    difference =  points - mindatapoints
    
    print("Removing {} extra data points from beginning".format(str(difference)))
    for i in range(difference):
        csvlist.pop(1)

    with open(constant.trainingfile, 'a', newline='') as csvobject:
        writer_object = csv.writer(csvobject)
        writer_object.writerow(csvlist)
        csvobject.close()


elif points < mindatapoints:
    print("Only {} points collected. Trashing data...".format(str(points)))
    
    with open(constant.trashfile, 'a', newline='') as csvobject:
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

