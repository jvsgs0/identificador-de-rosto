import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/User/Desktop/Indentificador de rostos/haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('C:/Users/User/Desktop/Indentificador de rostos/haarcascade_eye.xml')

smile_cascade = cv2.CascadeClassifier('C:/Users/User/Desktop/Indentificador de rostos/haarcascade_smile.xml')

upper_cascade = cv2.CascadeClassifier('C:/Users/User/Desktop/Indentificador de rostos/haarcascade_upperbody.xml')


vid = cv2.VideoCapture(0)

while(True):

    ret, frame = vid.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    eyes = eye_cascade.detectMultiScale(gray, 1.1, 5)

    smile = smile_cascade.detectMultiScale(gray, 1.1, 5)

    upper = upper_cascade.detectMultiScale(gray, 1.1, 5)

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 146), 2)

    for(x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 7, 17), 2)

    for(x, y, w, h) in smile:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 180, 255), 2)

    for(x, y, w, h) in upper:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(25) == 32:
        break

vid.release()