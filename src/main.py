import data.input as input
import data.processing as processing
import logger.logger as logger
import time
import visualizer.plot as visualizer
import variable.const as constant

starttime = time.time()


while(True):
    rawdata = input.getdata()
    data = processing.normalize(rawdata)
    magnitudevalue = float(processing.getmagnitude(data))
    data.append(magnitudevalue)
    timestamp = time.time() - starttime
    data.append(timestamp)
    print(data)
    logger.log(data, constant.datafile)
    #visualizer.animate()
    

