# HaardFall
Haar Cascades model creator<br/>

https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/


# Create Positive Samples
Replace <IMAGENAME> with name of image that the model will be trained to detect
``` sh
opencv_createsamples -img <IMAGENAME> -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950
```
Transform positive images into vector:
``` sh
opencv_createsamples -info info/info.lst -num 1950 -w 20 -h 20 -vec positives.vec
```
Train model with 10 levels:
``` sh
opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20
```
