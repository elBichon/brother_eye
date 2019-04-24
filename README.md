# Brother_eye
###### Brother eye is a suite of different image processing tools (face detection, color detection, classification...) that perform analysis on a video stream coming from an ip webcam.
![alt text](https://thorne.uk.com/wp-content/uploads/2017/05/big-brother-eye.jpg)
## Motivation: 
The project is to extract as much info as possible from a livestream through a portable interface (android smartphone) that can be reused for later purposes.
## Tech/Frameworks used:
- [keras](https://keras.io/)
- [opencv](https://opencv.org/)
- [haarcscade](https://www.python.org/)
- [python](https://github.com/opencv/opencv/tree/master/data/haarcascades)

## Project Structure:
- webcam.py
- utils.py

## Features:
- [x] Interfacing with android ip webcam on smartphone through python
- [x] Detecting faces, eyes, upper body, lower body and full body using haarcascade
- [x] Creating a picture for each of the detected boxes
- [ ] For each picture, extract the dominant color
- [ ] For the face picture make it go through a cnn to extract gender, age, facial emotion
- [ ] Using tensorflow to grep some more information on the picture with built-in object detection
- [ ] Use the face picture to get the closest person in a dataset for person authentification
- [ ] Counting number of persons going through (in case of a building apply recognition for people going in and out)

## Workflow:
1. Connecting to the ip webcam through your local network
2. The image flow will be processed. At a frequency you provide, the curent frame will be saved as an image

## How to use:

```
git status
git add
git commit
```
