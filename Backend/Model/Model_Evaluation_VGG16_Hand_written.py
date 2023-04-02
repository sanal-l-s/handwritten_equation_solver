from google.colab import drive
drive.mount('/content/drive')

import numpy as np 
import matplotlib.pyplot as plt
# here we are working on Tensorflow version 2.1.0 so we need to write tensorflow.keras.
#keras is in built function in Tensorflow.
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Input, Dropout,Flatten, Conv2D
from tensorflow.keras.layers import BatchNormalization, Activation, MaxPooling2D
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.utils import plot_model
from IPython.display import SVG, Image

train_location = "/content/drive/MyDrive/Hand Written/DataSet" 
test_location = "/content/drive/MyDrive/Hand Written/DataSet"
filepath = '/content/drive/MyDrive/Hand Written/CNN/VGG16/Model/Hand_written_VGG16_model1.h5'

from tensorflow.keras.models import load_model
Detection=load_model(filepath)

img_size=224
batch_size=25
num_class=49

# Complete Dataset images can be loaded using ImageDataGenerator function

datagen_train=ImageDataGenerator(horizontal_flip=True)
train_generator=datagen_train.flow_from_directory(train_location,target_size=(img_size,img_size),batch_size=batch_size,class_mode='categorical',shuffle=True)

datagen_test=ImageDataGenerator(horizontal_flip=True)
validation_generator=datagen_test.flow_from_directory(test_location,target_size=(img_size,img_size),batch_size=batch_size,class_mode='categorical',shuffle=True)


classes=train_generator.class_indices
classes

category=[]
for i in classes:
          category.append(i)

category

from skimage import io
import os
from tensorflow.keras.preprocessing import image

image_directory=test_location
dataset = []
predict_result=[]
label =[]


my_folders = os.listdir(image_directory)
for i, folder_name in enumerate(my_folders):
    #print(str(i)+': ' +folder_name) 

    loc=0
    for j in category:
      if(j==folder_name):
        lab=loc
      loc+=1
    lab

    my_images = os.listdir(image_directory+'/'+folder_name)
    for j,image_name in enumerate(my_images):
      #print(str(j)+': ' +image_name) 

      file_name = image_directory+'/'+folder_name + '/' + image_name

      test_img=image.load_img(file_name,target_size=(img_size,img_size))
      test_img=image.img_to_array(test_img)
      test_img=np.expand_dims(test_img,axis=0)
      result=Detection.predict(test_img)

      label.append(lab)
      predict_result.append(result.argmax())

      print(f'{folder_name} : {str(lab)} , Predicted : {result.argmax()}  ')


      

correct=0
Wrong=0


for i in range(len(label)):
  if(predict_result[i]==label[i]):
    correct+=1
  else:
    Wrong+=1

print(f'correct: {correct} , Wrong: {Wrong}')



Acc= correct/(correct+Wrong)
Acc*100


y_test = label
y_pred = predict_result


from sklearn.metrics import confusion_matrix, precision_score, recall_score
from sklearn.metrics import classification_report
from sklearn import metrics

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print('Test set accuracy: ',metrics.accuracy_score(y_test, y_pred))


confusion = metrics.confusion_matrix(y_test, y_pred)
confusion.ravel() 


accuracy = metrics.accuracy_score(y_test, y_pred)
accuracy

