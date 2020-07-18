import cv2
import numpy as np 
import os, time

__author__ = 'abitran'

# first we define the folder that contains the images
my_folder = 'album'

# we create a blank list to store all images
images = []

# we define the location of the folder
my_location = "/Users/xxxx/" + my_folder

# we loop through all the files inside the folder
for file in os.listdir(my_location):
    img = cv.imread(os.path.join(my_location,file))
    
    # if file is an image file then add it to the list
    if img is not None:
        images.append(img)
        
        
i = 0
# selecting two consecutive images at a time
for img1,img2 in zip(images,images[1:]):
    imgfirst = images[i]
    img = images[i+1] 
    
    # resizing both the images in same dimension
    imgfirst = cv.resize(img1,(640,480))
    img = cv.resize(img2,(640,480))
    i = i+1
    
# blending formula from cv2 docs:
# dst = alpha*img1 + beta*img2 + gamma, where gamma = 0
# we create a loop from 1-10 (including 10) to apply alpha 
    for alpha in range(1, 11):

# we divide alpha by 10 to create a float
        alpha = alpha/10.0
# to create a transition effect, beta must be:
        beta = 1 - alpha
# we load the transition into the image canvas
        cv2.imshow('album', cv2.addWeighted(img, beta, imgfirst, alpha, 0.0))
        time.sleep(0.1)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    if cv2.waitKey(0) & 0xff == ord('q'):
        break

     
cv2.destroyAllWindows()
