# Brother_eye
######Brother eye is a suite of different image processing tools (face detection, color datection, classification...) that perform analysis on a video stream coming from an ip webcam.

---------------Motivation:
The project is to extract as much info as possible from a livestream through a portable interface (android smartphone) that can be reused for later purposes. It will be one of the brick (with sound, speech, language analysis and reinforcement learning) of a bigger experimental project.

##Tech/Frameworks used:
- [keras](https://keras.io/)
- opencv
- haarcscade
- python

##Project Structure:
- webcam.py
- utils.py

##Features:
- [x] Interfacing with android ip webcam on smartphone through python
- [x] Detecting faces, eyes, upper body, lower body and full body using haarcascade
- [ ] Creating a picture for each of the detected boxes
- [ ] For each picture, make it go through the fashion mnist classifier to detect the clothes
- [ ] For each picture, extract the dominant color
- [ ] For the face picture make it go through a cnn to extract gender, age, facial emotion
- [ ] Perform segmentation on the whole picture and extract each segment containing objects *(not containing people)* to make it go through an object images classifier and extract the dominant colors
- [ ] Perform segmentation on the whole picture and extract each segment containing people to make it go through an image classifier for group classification
- [ ] Using CNN to add points for pose estimation at specific parts of the whole picture for relationships classification *(experimental)*

##Workflow:

##How to use:

```
git status
git add
git commit
```
