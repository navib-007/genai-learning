# -*- coding: utf-8 -*-
from keras.applications.vgg16 import VGG16
import matplotlib.pyplot as plt

model= VGG16()

model.summary()

from keras.utils import plot_model

plot_model(model)

for i in range(len(model.layers)):
  if 'conv' not in model.layers[i].name:
    continue

  filters, biases= model.layers[i].get_weights()
  print("Layer Number",i, " ", model.layers[i].name, " ", filters.shape)

filters, bias = model.layers[1].get_weights()

f_min, f_max= filters.min(), filters.max()
filters= (filters-f_min)/ (f_max-f_min)

n_filters=6
ix=1
fig= plt.figure(figsize=(15,10))
for i in range(n_filters):
  f= filters[:,:,:,i]
  for j in range(3):
    plt.subplot(n_filters,3,ix)
    plt.imshow(f[:,:,j],cmap='gray')
    ix+=1

plt.show()

