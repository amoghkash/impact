from csv import writer
import variable.const as constant


def log(data, file):
    file = constant.basedir + "/data/collection/" + file
    
    with open(file, 'a', newline='') as csvwriter:
        csv = writer(csvwriter)
        csv.writerow(data)
        csvwriter.close

