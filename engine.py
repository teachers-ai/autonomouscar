import keras,os
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D , Flatten
import numpy as np
import cv2

class Engine:


    def __init__(self):
        self.model = self.getModel()

    def getModel(self):
        # change this function , inorder to use your model
        model_weight = "./models/hanuman1.h5"
        
        model = Sequential()
        model.add(Conv2D(input_shape=(50, 200, 3),filters=32,kernel_size=(3,3),padding="same", activation="relu"))
        model.add(Conv2D(filters=16,kernel_size=(3,3),padding="same", activation="relu"))
        model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
        model.add(Flatten())
        model.add(Dense(units=250,activation="relu"))
        model.add(Dense(units=100,activation="relu"))
        model.add(Dense(units=3, activation="softmax"))
        model.load_weights(model_weight)

        return model

    def predict(self, img):

       img = cv2.resize(img, (200, 50))/255
       img =np.expand_dims(img, axis=0)

       index=  np.argmax(self.model.predict(img)[0], axis=0)

       if index == 0 :
           return "L"
       elif index == 1:
           return "F"
       elif index==2:
           return "R"




