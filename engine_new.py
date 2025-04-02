import keras,os
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D , Flatten
import numpy as np
import cv2
import tensorflow as tf
import torch 
import torchvision.transforms as transforms
from PIL import Image

class Engine:


    def __init__(self, path='tf_model.h5'):
        
        self.modeltype = "tf"
        if "tf_" in path:
            self.model = self.gettfModel(path)
        else:
            self.model =torch.jit.load(f'./models/{path}')
            self.modeltype ="pt"

    def gettfModel(self, path):
        # change this function , inorder to use your model

        model_weight = f"./models/{path}"
        model = tf.keras.models.load_model(model_weight)
      
        return model

    def predict(self, img):

       if self.modeltype == "tf":

        img = cv2.resize(img, (200, 50))/255
        img =np.expand_dims(img, axis=0)

        index=  np.argmax(self.model.predict(img)[0], axis=0)

        if index == 0 :
           return "L"
        elif index == 1:
           return "F"
        elif index==2:
           return "R"

       else:

          transform = transforms.Compose([transforms.ToTensor(),   transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)) ])
          self.model.eval()
          image = Image.fromarray(img).resize((200, 50))
          image =transform(image).unsqueeze(0)
          _, predicted = torch.max(self.model(image), 1)
          if predicted.item() == 0:
               return  "L"
          elif predicted.item() == 1:
               return "F"
          elif predicted.item() == 2:
                return "R"




