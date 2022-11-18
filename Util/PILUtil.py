from PIL import Image, ImageFont, ImageDraw
import cv2
import numpy as np


def put_chinese_opencv(im, chinese, pos=(100, 100), color=(255, 0, 0)):
    img_PIL = Image.fromarray(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    font = ImageFont.truetype("/Volumes/Mac-vm/zhenshuAI/Util/HYWenHei-85W.ttf", 60)
    fillColor = color
    position = pos
    draw = ImageDraw.Draw(img_PIL)
    draw.text(position, chinese, font=font, fill=fillColor)

    img = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)
    return img
