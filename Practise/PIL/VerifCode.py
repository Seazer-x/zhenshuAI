from PIL import Image, ImageFont, ImageDraw
from Util.StringUtil import *
import numpy as np


def getCode(num=4, w=300, h=120):
    drawBack = np.array([getBackColor() for x in range(w * h)], np.uint8)
    drawBack = drawBack.reshape(h, w, 3)
    img = Image.fromarray(drawBack)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("HYWenHei-85W.ttf", 60)
    rStr = getRandomStr(num)
    font_h = font.getsize(rStr[0])[1]
    for index, item in enumerate(rStr):
        # 写字
        draw.text((15 + index * (w // num), (h - font_h) // 2), item, getFontColor(), font=font)
    return img


getCode(7, w=480).show()
