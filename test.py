# Importing all required packages
import cv2
import numpy as np
import matplotlib.pyplot as plt #% matplotlib inline
import argparse

# Define the parser
parser = argparse.ArgumentParser(description='Haar Cascade detector with XML cascade file and png image to match against')

# field, and using a default value if the argument 
# isn't given
parser.add_argument('--cascade', action="store", dest='cascade', default='test.xml')
parser.add_argument('--inputImage', action="store", dest='inputImage', default='testFullMatch.PNG')
parser.add_argument('--outputImage', action="store", dest='outputImage', default='CascadeMatchFull.jpg')

# Now, parse the command line arguments and store the 
# values in the `args` variable
args = parser.parse_args()

# Individual arguments can be accessed as attributes...
print (args.algo)
 
 
# Read in the cascade classifiers for face and eyes
test_cascade = cv2.CascadeClassifier(args.cascade)

def detect_test(img):
     
    test_img = img.copy()    
    test_rect = test_cascade.detectMultiScale(tes_img, 
                                            scaleFactor = 1.2, 
                                            minNeighbors = 5)    
    for (x, y, w, h) in test_rect:
        cv2.rectangle(test_img, (x, y), 
                      (x + w, y + h), (255, 255, 255), 10)        
    return test_img


img = cv2.imread(args.inputImage)
test = detect_test(img)
plt.imshow(test)
cv2.imwrite(args.outputImage, test)
