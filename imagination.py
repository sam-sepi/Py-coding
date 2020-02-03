import numpy as np
from PIL import Image
import binascii

# RGB images are usually stored as 3 dimensional arrays of 8-bit unsigned integers.
# Each pixel contains 3 bytes (representing the red, green and blue values of the pixel colour)

width = 4
height = 4

array = np.zeros([height, width, 3], dtype = np.uint8) # 8-bit unsigned integers

# black white black white
array[0] = [0, 0, 0]
array[1] = [255, 255, 255]
array[2] = [0, 0, 0]
array[3] = [255, 255, 255]

# save img
img = Image.fromarray(array)
img.save('testrgb.png')

# img to np array
conv = Image.open('testrgb.png')
pix = np.array(conv)

# open img and convert in hex
with open('testrgb.png', 'rb') as f:
    content = f.read()

print(binascii.hexlify(content))
