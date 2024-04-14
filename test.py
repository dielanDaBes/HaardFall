# Importing all required packages
import cv2
import numpy as np
import matplotlib.pyplot as plt #% matplotlib inline
 
 
# Read in the cascade classifiers for face and eyes
test_cascade = cv2.CascadeClassifier('test.xml')

def detect_test(img):
     
    test_img = img.copy()    
    test_rect = test_cascade.detectMultiScale(tes_img, 
                                            scaleFactor = 1.2, 
                                            minNeighbors = 5)    
    for (x, y, w, h) in test_rect:
        cv2.rectangle(test_img, (x, y), 
                      (x + w, y + h), (255, 255, 255), 10)        
    return test_img


img = cv2.imread('testMatchFull.PNG')
test = detect_test(img)
plt.imshow(test)
cv2.imwrite('CascadeMatchFull.jpg', test)
