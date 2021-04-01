from PIL import Image
import os
import numpy as np

image = Image.open('choice.jpg')
image.show()
print('size :' {}.format(image.size))
print('image mode : {}'.format(image.mode))
print('image format : {}'.format(image.format))

image.convert('RGB').resize(600,400).save('icon.jpeg')
