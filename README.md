# Brother_eye
###### Brother eye is a suite of different image processing tools (face detection, color datection, classification...) that perform analysis on a video stream coming from an ip webcam.

## Motivation: 
The project is to extract as much info as possible from a livestream through a portable interface (android smartphone) that can be reused for later purposes. It will be one of the brick (with sound, speech, language analysis and reinforcement learning) of a bigger experimental project.

## Tech/Frameworks used:
- [keras](https://keras.io/)
- opencv
- haarcscade
- python

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
- [ ] Using CNN to add points for pose estimation at specific parts of the whole picture for relationships classification *(experimental)*

## Workflow:
1. Connecting to the ip webcam through your local network
2. The image flow will be processed. At a frequency you provide, the curent frame will be saved as an image
3. The different part of the pictur ein bounding boxes will be saved as different images
4. The global picture will go through segmentation script
5. Each segment will be saved as a picture
6. All the different pictures will go through the different ad hoc modules to extract data

## How to use:

```
git status
git add
git commit
```
