# -*- coding: utf-8 -*-
"""Model_Training.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WKbbEbnD5Sav6G47rwrzs7UM8aLT398g
"""

import pandas as pd
import numpy as np
from keras.models import load_model

from google.colab import drive
drive.mount('/content/drive')

df_train=pd.read_csv('/content/drive/MyDrive/train_3.csv',index_col=False)
df_train = df_train.sample(frac = 1, random_state=42).reset_index(drop=True)
labels=df_train[['784']]

df_train.drop(df_train.columns[[784]],axis=1,inplace=True)
df_train.head()

df_train.tail()

train_x = df_train[:46000]
train_y = labels[:46000]

train_x.shape

train_y.shape

valid_x = df_train[46000:49000]
valid_y = labels[46000:49000]

test_x = df_train[49000:]
test_y = labels[49000:]

test_x.shape

test_y.shape

np.random.seed(1212)
import keras
from keras.models import Model
from keras.layers import *
from keras import optimizers
from keras.layers import Input, Dense
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras.layers import BatchNormalization as Batchnormalization

train_y=np.array(train_y)
valid_y=np.array(valid_y)
test_y=np.array(test_y)

from keras.utils.np_utils import to_categorical
cat=to_categorical(train_y,num_classes=15)
cat_1=to_categorical(valid_y,num_classes=15)
cat_2=to_categorical(test_y,num_classes=15)

print(cat[0])

cat_2.shape

l=[]
for i in range(46000):
    l.append(np.array(train_x[i:i+1]).reshape(1,28,28))

l2=[]
for i in range(3000):
    l2.append(np.array(valid_x[i:i+1]).reshape(1,28,28))

len(l2)

l3=[]
for i in range(3699):
    l3.append(np.array(test_x[i:i+1]).reshape(1,28,28))

len(l3)

np.random.seed(7)

model = Sequential()
model.add(Conv2D(30, (5, 5), input_shape=(1, 28, 28), activation='relu', data_format='channels_first'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Batchnormalization())
model.add(Conv2D(15, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Batchnormalization())
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(92, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(15, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

start = int(round(time.time() * 1000))
history = model.fit(np.array(l),cat, validation_data=(np.array(l2),cat_1), epochs=10, batch_size=200)
end = int(round(time.time() * 1000))
print("-- fitting finished in ", (end-start), "ms--------------")

model.save("/content/drive/MyDrive/models_7_1.h5")

import matplotlib.pyplot as plt
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Plot')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['train', 'valid'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

model = load_model('/content/drive/MyDrive/models_7_1.h5')
loss_and_metrics = model.evaluate(np.array(l3), cat_2, verbose=2)
print('Test loss:', loss_and_metrics[0]) 
print('Test accuracy:', loss_and_metrics[1])

predictions = np.argmax(model.predict(np.array(l3)), axis=-1)

from sklearn.metrics import classification_report
print(classification_report(test_y,predictions))
