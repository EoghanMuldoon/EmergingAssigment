import csv
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from scipy import stats


Power=[]
Speed=[]
Data=[]
tempList=[]

with open('DATA.txt') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        temp=(', '.join(row))
        x=temp.split(",")
        Speed.append(float(x[0]))
        Power.append(float(x[1]))
    
    length=len(Speed)


# Build a simple model

x=Speed
y=Power



mymodel = np.poly1d(np.polyfit(x, y, 3))

myline = np.linspace(1, 22, 100)

#plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
print(np.random.normal())





