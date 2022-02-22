import math
from numpy import square

def normalize(accelerationlist):
    values = list(map(decompress, accelerationlist))
    x = values[0]
    y = values[1]
    z = values[2]
    return(values)


def decompress(n):
    return(int(n)/100)


def getmagnitude(list):
    sum = (square(list[0])) + (square(list[1])) + (square(list[2]))
    magnitude = format(math.sqrt(sum),".2f")
    return(magnitude)
