# Importing all required packages
import cv2
import argparse

def detect_test(img):
     
    test_img = img.copy()    
    test_rect = test_cascade.detectMultiScale(test_img, 
                                            scaleFactor = 1.2, 
                                            minNeighbors = args.neighbors)    
    for (x, y, w, h) in test_rect:
        cv2.rectangle(test_img, (x, y), 
                      (x + w, y + h), (255, 255, 255), args.lineSize)        
    return test_img
 

# Define the parser
parser = argparse.ArgumentParser(description='Haar Cascade detector with XML cascade file and png image to match against')

# field, and using a default value if the argument 
# isn't given
parser.add_argument('-c', '--cascade', action="store", dest='cascade', default='test.xml', help="Cascade classifier file in xml format")
parser.add_argument('-i', '--inputImage', action="store", dest='inputImage', default='testInputFull.PNG', help="Input image that contains object to detect")
parser.add_argument('-o', '--outputImage', action="store", dest='outputImage', default='testOutputFull.jpg', help="Output image with rectangle around detected object")
parser.add_argument('-n', '--neighbors', action="store", dest='neighbors', default=5, help="Cascade classifier parameter- higher is more sensitive, see openCV docs for more details")
parser.add_argument('-l', '--lineSize', action="store", dest='lineSize', default=2, help="Size of rectangle around detected object")

# Now, parse the command line arguments and store the 
# values in the `args` variable
args = parser.parse_args()
 
print(args)
# Read in the cascade classifiers for face and eyes
test_cascade = cv2.CascadeClassifier(args.cascade)

img = cv2.imread(args.inputImage)
test = detect_test(img)
cv2.imwrite(args.outputImage, test)
