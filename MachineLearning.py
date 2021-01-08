
import csv
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt
import flask as fl

app=fl.Flask(__name__)

#add root route
@app.route("/")
def home():
    return app.send_static_file('index.html')

#add root route
@app.route("/api/machineLearing")
def machineLearing():

    Power=[]
    Speed=[]

    with open('DATA.txt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            temp=(', '.join(row))
            x=temp.split(",")
            speed=float(x[0])
            power=float(x[1])
            if(power!=0.0):
                Speed.append(speed)
                Power.append(power)
                
        
    train = pd.DataFrame()
    train['x']=Speed
    train['y']=Power

    #create test Data
    train = pd.DataFrame()
    train['x']=(24.299,20.145,19.094)
    train['y']=(93.694,99.029,97.148)

    test = pd.DataFrame()
    test['x']=Speed
    test['y']=Power


    #use findCureType.py to see what the data looks like 
    #use this website to see it a Sigmoid curce
    #https://medium.com/linum-labs/intro-to-bonding-curves-and-shapes-bf326bc4e11a

    #neural network 
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(50, input_shape=(1,), activation="sigmoid", kernel_initializer='glorot_uniform', bias_initializer='glorot_uniform'))
    model.add(tf.keras.layers.Dense(1, activation="linear", kernel_initializer='glorot_uniform', bias_initializer='glorot_uniform'))
    ##could be more accuate with different loss
    model.compile(tf.keras.optimizers.Adam(lr=0.01), loss='mean_squared_error')
    model.fit(train['x'], train['y'], epochs=1000 , batch_size=10)

    #test out the oredications
    model.predict([1.0,13.0,25.0])

    #return{"Value":model.predict([5.0])}
    power=model.predict([5.0])
    floatPower=float(power)
    return{"value": floatPower}

        
