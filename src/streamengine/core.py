import math
import data.input as input
import data.processing as processing
import pandas as pd

stream = []
rawdata = input.getdata()
data = processing.normalize(rawdata)

def getframe(points, data = processing.getmagnitude(data)):
    while True:
        dataframe(stream, points, data)
        return(stream)
        
    


def dataframe(list, maxpoints, data):
    totalpoints = len(list)
    while(totalpoints > maxpoints):
        list.pop[0]
    
    while(totalpoints < maxpoints):
        list.append(data)
        data = input.getdata()



# Take the last x digits or values and save them into a variable for 


