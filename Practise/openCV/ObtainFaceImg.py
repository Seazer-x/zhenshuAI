import time

import cv2
import os.path

faceCase = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face_id = input("请输入姓名:")
face_idnum = input("请输入编号:")
if not os.path.exists("imagedata"):
    os.makedirs("imagedata")
print("正在打开摄像头......")
cap = cv2.VideoCapture(0)  # 获取视频对象
num = 0
while cap.isOpened():
    pt, frame = cap.read()
    if pt:
        img = cv2.resize(frame, (720, 420))
        cv2.imshow("face", img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCase.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5))
        if cv2.waitKey(10) == 27:
            break
        elif len(faces) > 0:
            num += 1
            print("正在保存第", num, "张图片...")
            cv2.imencode(".jpg", frame)[1].tofile("imagedata//" + face_id + "." + str(num) + ".jpg")
    else:
        del pt
        del frame
cap.release()
cv2.destroyAllWindows()
