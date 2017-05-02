import cv2
import numpy as np 
import os, time

__author__ = 'abitran'

# first we define the folder that contains the images
my_folder = 'album'

# we create a blank image of the same dimension as the images inside de folder
imgfirst = np.zeros((453,604,3), np.uint8)

# we define the location of the folder
my_location = "/Users/xxxx/" + my_folder

# we loop through the files inside the folder
for file in os.listdir(my_location):

# we read a file    
    img = cv2.imread(my_location + '/' + file)

# blending formula from cv2 docs:
# dst = alpha*img1 + beta*img2 + gamma, where gamma = 0

# we create a loop from 1-10 (including 10) to apply alpha 
    for alpha in xrange(1, 11):

# we divide alpha by 10 to create a float
        alpha = alpha/10.0
# to create a transition effect, beta must be:
        beta = 1 - alpha
# we load the transition into the image canvas
        cv2.imshow('album', cv2.addWeighted(img, alpha, imgfirst, beta, 0.0))
        time.sleep(0.1)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    if cv2.waitKey(0) & 0xff == ord('q'):
        break
# we assign the img to the first one
    imgfirst = img
     
cv2.destroyAllWindows()
