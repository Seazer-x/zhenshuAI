import os
import cv2 as cv
from PIL import Image
import numpy as np

person_index = {'fbp': 1, 'lyk': 2}


# 人脸识别训练
def getImageAndlabels(img_path):
    # 人脸数据数据
    facesSamples = []
    # 人标签
    face_ids = []
    # 读取所有的照片的名称（os.listdir读取根目录下文件的名称返回一
    # 个列表，os.path.join将根目录和文件名称组合形成完整的文件路径）
    imagePaths = [os.path.join(img_path, f) for f in os.listdir(img_path)]
    # 调用人脸分类器（注意自己文件保存的路径，英文名）
    face_detect = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    # 循环读取照片人脸数据
    for imagePath in imagePaths:
        # 用灰度的方式打开照片
        PIL_img = Image.open(imagePath).convert('L')
        # 将照片转换为计算机能识别的数组OpenCV（BGR--0-255）
        img_numpy = np.array(PIL_img, 'uint8')
        # 提取图像中人脸的特征值
        faces = face_detect.detectMultiScale(img_numpy)
        # 将文件名按“.”进行分割
        id = person_index.get(os.path.split(imagePath)[1].split('.')[0])
        # 防止无人脸图像
        for x, y, w, h in faces:
            face_ids.append(id)
            facesSamples.append(img_numpy[y:y + h, x:x + w])
    return facesSamples, face_ids


# 人脸图片存放的文件夹
path = 'imagedata'
faces, ids = getImageAndlabels(path)
# 调用LBPH算法对人脸数据进行处理
# 报错，安装：pip install opencv-contrib-python
recognizer = cv.face.LBPHFaceRecognizer_create()
# 训练数据
recognizer.train(faces, np.array(ids))
# 将训练的系统保存在特定文件夹
recognizer.write('trainer.yml')
