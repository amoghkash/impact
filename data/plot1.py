import matplotlib.pyplot as plt
import csv

xx = []
xy = []
xz = []
mag = []
y=[]

with open('data.csv') as file:
    next(file)
    x =0
    lines = csv.reader(file, delimiter=',')
    for row in lines:
       #if x==10:
        xx.append(float(row[0]))
        xy.append(float(row[1]))
        xz.append(float(row[2]))
        mag.append(float(row[3]))
        time = float(row[4])
        time = round(time, 2)
        y.append(x)
        #x=0
        x = x +1


#plt.plot(y, xx, label = "Acc X")
#plt.plot(y, xy, label = "Acc Y")
#plt.plot(y, xz, label = "Acc Z")
plt.plot(y, mag, label = "Magnitude")

plt.legend()
plt.show()