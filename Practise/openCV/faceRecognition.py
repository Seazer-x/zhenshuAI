import cv2

haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
people = ['fbp', 'fbp', 'lyk', 'fbp']


face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainer.yml')

cap = cv2.VideoCapture("http://admin:admin@fukashiwaiPhone.local:8081/video")
while True:
    ret, img = cap.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the face in the image
        face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in face_rect:
            face_roi = gray[y:y + h, x:x + w]

            label, confidence = face_recognizer.predict(face_roi)
            print(label)
            # confidence :'0' indicates an exact match,value less than 50 is considered acceptable
            # value greater than 85 means the difference is huge
            cv2.putText(img, str(people[label]), (x+5, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), thickness=1)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
        cv2.imshow('Detected Face', img)
        if cv2.waitKey(5) == 27:
            break
    else:
        del ret
        del img
