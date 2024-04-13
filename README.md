# HaardFall
Haar Cascades model creator<br/>

https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/

Build openCV inside opencv folder:
``` sh
mkdir build && cd build
```

``` sh
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_PYTHON_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules -D BUILD_EXAMPLES=ON ..
```

# Create Positive Samples
Replace \<IMAGENAME\> with name of image that the model will be trained to detect
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
Copy the output cascade.xml file from the data directory into your project for detection
