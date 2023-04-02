from google.colab import drive
drive.mount('/content/drive')


from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import cv2


train_location = "/content/drive/MyDrive/Hand Written/DataSet" 
test_location = "/content/drive/MyDrive/Hand Written/DataSet"
filepath = '/content/drive/MyDrive/Hand Written/CNN/VGG16/Model/Hand_written_VGG16_model1.h5'


Detection=load_model(filepath)


img_size=224
batch_size=25
num_class=49


#img_size=48
#batch_size=64
datagen_train=ImageDataGenerator(horizontal_flip=True)
train_generator=datagen_train.flow_from_directory(test_location,
target_size=(img_size,img_size),
batch_size=batch_size,
class_mode='categorical',
shuffle=True)



classes=train_generator.class_indices
classes


category=[]
for i in classes:
          category.append(i)


category


file_name = "/content/drive/MyDrive/Hand Written/5_1760.jpg"


test_img=image.load_img(file_name,target_size=(img_size,img_size))
plt.imshow(test_img)
test_img=image.img_to_array(test_img)
test_img=np.expand_dims(test_img,axis=0)
result=Detection.predict(test_img)
a=result.argmax()
classes=train_generator.class_indices

category=[]
for i in classes:
          category.append(i)
for i in range(len(classes)):
          if(i==a):
              output=category[i]
print(output)


a

a=result.argmax()
a
result

result.argmax()

