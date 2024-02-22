import cv2

img = cv2.imread("C:/Users/User/Desktop/Indentificador de rostos/image/solo.jpg")
img2 = cv2.imread("C:/Users/User/Desktop/Indentificador de rostos/image/grupo.jpg")

choice = int(input("Digite 1 ou 2 para escolher a imagem "))

if choice == 1:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(gray,1.1, 5)

    print(len(faces))

    for (x,y,w,h) in faces:

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,146),2)

        roi_color = img[y:y+h, x:x+w]
        cv2.imwrite("face.jpg",roi_color)

    cv2.imshow('img',img)
    cv2.waitKey(0)
else:
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    face_cascade2 = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    faces2 = face_cascade2.detectMultiScale(gray2,1.1, 5)

    print(len(faces2))

    for (x,y,w,h) in faces2:

        cv2.rectangle(img2,(x,y),(x+w,y+h),(255,0,146),2)

        roi_color2 = img2[y:y+h, x:x+w]
        cv2.imwrite("faces.jpg",roi_color2)

    cv2.imshow('img2',img2)
    cv2.waitKey(0)