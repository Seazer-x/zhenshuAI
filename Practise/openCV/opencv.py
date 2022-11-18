import os.path

from Util.PILUtil import *
from Util.OpenvUtil import *

img = cv2.imread("/Volumes/Mac-vm/zhenshuAI/Project/spider/Photo_spider/images/wallhaven-5gdlw9.jpg")
cv2.imshow("wallhaven", img)

print(img.shape)
B, G, R = img[100, 100]
print("B=%s, G=%s, R=%s" % (B, G, R))
# B, G, R = img[100, 100]
img[200, 200] = (255, 255, 255)
B, G, R = img[200, 200]
print("B=%s, G=%s, R=%s" % (B, G, R))

img2 = img[-100:, :400]
img[:100, :400] = img2
cv2.imshow("slice", img)

H, W, C = img.shape
M = cv2.getRotationMatrix2D((W // 2, H // 2), 80, 1)
dst = cv2.warpAffine(img, M, (W, H))
cv2.imshow('M10', dst)

# (163,30)左上角
# (244,124)右下角
# BGRh红色（0，0，255）
# 绘图函数
cv2.rectangle(img, (300, 90), (430, 180), (0, 0, 255), 10)
cv2.imshow('test', img)

cv2.circle(img, (400, 400), 200, (124, 23, 53), -1)
cv2.circle(img, (700, 700), 100, (34, 124, 64), thickness=10)
cv2.imshow('m10', img)

cv2.putText(img, "付柏萍", (60, 70), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 255), 2)
cv2.putText(img, "dogfight", (100, 90), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 255), 2)
cv2.imshow("text", img)

charimg = put_chinese_opencv(img, "付柏萍")
cv2.imshow("charimg", charimg)

cap = cv2.VideoCapture("纳西妲.flv")  # 获取视频对象
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FPS))
print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
pt, frame = cap.read()
cv2.imshow(" ", frame)

cap = cv2.VideoCapture("纳西妲.flv")  # 获取视频对象
while cap.isOpened():
    pt, frame = cap.read()
    if pt:
        cv2.imshow(" ", frame)
        cv2.waitKey(30)
    else:
        del pt
        del frame
cap.release()
writeVideo2MP4("纳西妲.flv", "纳西妲copy.mp4")

cap = cv2.VideoCapture(0)  # 获取视频对象
while cap.isOpened():
    pt, frame = cap.read()
    if pt:
        cv2.imshow(" ", frame)
        if cv2.waitKey(5) == 27:
            break
    else:
        del pt
        del frame
cap.release()

getCamera()  # 捕捉摄像头
img = cv2.imread("img.png")
faceCase = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCase.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5))
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
img = cv2.resize(img, (720, 420))
cv2.imshow("face", img)

