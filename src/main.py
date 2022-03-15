import data.input as input
import data.processing as processing
import logger.logger as logger
import time
#import plot as visualizer
import variable.const as constant
import AppKit


starttime = time.time()

print('\a')
x=1
while(x==1):
    rawdata = input.getdata()
    data = processing.normalize(rawdata)
    magnitudevalue = float(processing.getmagnitude(data))
    data.append(magnitudevalue)
    timestamp = time.time() - starttime
    data.append(timestamp)
    print(data)
    logger.log(data, constant.datafile)
    if(magnitudevalue>60):
        x=0
        print("Impact Detected")
        AppKit.NSBeep()
    #visualizer.animate()
    

