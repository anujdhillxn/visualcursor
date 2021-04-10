import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

df = pd.read_csv("training_data.csv")
data = df.iloc[:,0:-1].values
mouselocs = df.iloc[:,-1:].values
labelx = mouselocs//2003
labely = mouselocs%2003
modelx = Sequential()
modelx.add(Dense(30,input_dim = 1080, activation = 'relu'))
modelx.add(Dense(30,input_dim = 30, activation = 'relu'))
modelx.add(Dense(1, activation = 'linear'))
modelx.compile(Adam(lr=0.01), 'mean_squared_error')
historyx = modelx.fit(data,labelx,epochs = 200,validation_split = 0.0,verbose = 0)
modelx.save("modelx")
modely = Sequential()
modely.add(Dense(30,input_dim = 1080, activation = 'relu'))
modely.add(Dense(30,input_dim = 30, activation = 'relu'))
modely.add(Dense(1, activation = 'linear'))
modely.compile(Adam(lr=0.01), 'mean_squared_error')
historyy = modely.fit(data,labely,epochs = 200,validation_split = 0.0,verbose = 0)
modely.save("modely")




