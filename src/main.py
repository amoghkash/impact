import data.input as input
import data.processing as processing
import logger.logger as logger

while(True):
    rawdata = input.getdata()
    data = processing.normalize(rawdata)
    magnitudevalue = float(processing.getmagnitude(data))
    data.append(magnitudevalue)
    print(data)
    logger.log(data, "data.csv")