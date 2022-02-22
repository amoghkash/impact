from csv import writer
from email.mime import base
import os
import logger

basedir = os.path.expanduser('~') + "/impact"

def log(data, file):
    file = basedir + "/data/collection/" + file
    
    with open(file, 'a', newline='') as csvwriter:
        csv = writer(csvwriter)
        csv.writerow(data)
        csvwriter.close

