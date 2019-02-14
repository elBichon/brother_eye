import numpy as np
import cv2
import requests

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('/home/jeanedouard-rgz/Bureau/haarcascades/haarcascade_profileface.xml')
face_cascade2 = cv2.CascadeClassifier('/home/jeanedouard-rgz/Bureau/haarcascades/haarcascade_frontalcatface.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('/home/jeanedouard-rgz/Bureau/haarcascades/haarcascade_eye.xml')
full_body_cascade = cv2.CascadeClassifier('/home/jeanedouard-rgz/Bureau/haarcascades/haarcascade_fullbody.xml')
lower_body_cascade = cv2.CascadeClassifier('/home/jeanedouard-rgz/Bureau/haarcascades/haarcascade_lowerbody.xml')
upper_body_cascade = cv2.CascadeClassifier('/home/jeanedouard-rgz/Bureau/haarcascades/haarcascade_upperbody.xml')


url = "http://192.168.1.80:8080/shot.jpg"


while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    faces2 = face_cascade2.detectMultiScale(gray, 1.3, 5)
    full_body = full_body_cascade.detectMultiScale(gray, 1.3, 5)
    lower_body = lower_body_cascade.detectMultiScale(gray, 1.3, 5)
    upper_body = upper_body_cascade.detectMultiScale(gray, 1.3, 5)
     
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    for (x,y,w,h) in faces2:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray2 = gray[y:y+h, x:x+w]
        roi_color2 = img[y:y+h, x:x+w]
        
        eyes2 = eye_cascade.detectMultiScale(roi_gray2)
        for (ex,ey,ew,eh) in eyes2:
            cv2.rectangle(roi_color2,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    for (x,y,w,h) in full_body:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    for (x,y,w,h) in lower_body:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    for (x,y,w,h) in upper_body:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]


    cv2.imshow('androidcam',img)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()
