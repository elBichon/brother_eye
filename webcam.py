import numpy as np
import cv2
import requests

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade_profile = cv2.CascadeClassifier('/home/jeanedouard-rgz/Bureau/haarcascades/haarcascade_profileface.xml')
face_cascade_frontal = cv2.CascadeClassifier('/home/jeanedouard-rgz/Bureau/haarcascades/haarcascade_frontalcatface.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('/home/jeanedouard-rgz/Bureau/haarcascades/haarcascade_eye.xml')
full_body_cascade = cv2.CascadeClassifier('/home/jeanedouard-rgz/Bureau/haarcascades/haarcascade_fullbody.xml')
lower_body_cascade = cv2.CascadeClassifier('/home/jeanedouard-rgz/Bureau/haarcascades/haarcascade_lowerbody.xml')
upper_body_cascade = cv2.CascadeClassifier('/home/jeanedouard-rgz/Bureau/haarcascades/haarcascade_upperbody.xml')


url = "http://192.168.1.80:8080/shot.jpg"

def part_acquisition(img, part, title):
    for (x,y,w,h) in part:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        cv2.imwrite(title,roi_color)

def face_acquisition(img, part, title):
    for (x,y,w,h) in part:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        cv2.imwrite(title,roi_color)

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


i = 0
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if i == 0:
        cv2.imwrite('full_screen.jpg',img)
        i += 1

    profil = face_cascade_profile.detectMultiScale(gray, 1.3, 5)
    frontal = face_cascade_frontal.detectMultiScale(gray, 1.3, 5)
    full_body = full_body_cascade.detectMultiScale(gray, 1.3, 5)
    lower_body = lower_body_cascade.detectMultiScale(gray, 1.3, 5)
    upper_body = upper_body_cascade.detectMultiScale(gray, 1.3, 5)
     
     
    face_acquisition(img, profil, 'profile.jpg')
    face_acquisition(img, frontal, 'frontal.jpg')
    part_acquisition(img, full_body,'full.jpg')
    part_acquisition(img, lower_body,'lower.jpg')
    part_acquisition(img, upper_body,'upper.jpg')
    
    cv2.imshow('androidcam',img)

    if cv2.waitKey(1)==27:
        break

cap.release()  
