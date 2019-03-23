# Face_detection-
The Face Detection model

Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and
Michael Jones in their paper,"Rapid Object Detection using a Boosted Cascade of Simple Features" in 2001. It is a machine
learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to 
detect objects in other images. Here we will work with face detection. 

Initially, the algorithm needs a lot of positive images (images of faces) and negative images (images without faces) to train 
the classifier. Then we need to extract features from it. For this, Haar features shown in the below image are used. They are
just like our convolutional kernel. Each feature is a single value obtained by subtracting sum of pixels under the white rectangle 
from sum of pixels under the black rectangle.

fore more Info check https://docs.opencv.org/3.4.3/d7/d8b/tutorial_py_face_detection.html
