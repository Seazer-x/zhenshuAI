from PIL import Image, ImageFilter, ImageFont, ImageDraw
import numpy as np
from Util.StringUtil import *

img = Image.open("/Volumes/Mac-vm/zhenshuAI/Project/spider/Photo_spider/images/wallhaven-5gdlw9.jpg")
w, h = img.size
# # dtype = np.uint8[0,255]
# print(img.getbands())
# print(img.mode)
# print(img.size)
# print(img.readonly)
# img.info["name"] = "WallHaven"
# print(img.info)


# imgNp = np.array(img, dtype=np.uint8)
# # W , H
# print(img.size)
# # H, W, C
# print(imgNp.shape)
# print(imgNp)

# print(img.mode)
# imgL = img.convert("L")
# print(imgL.mode)
# imgL.save("imgL.jpg")
# imgL.show()
#
# imgRGB = imgL.convert("RGB")
# print(imgRGB.mode)
# imgRGB.show()

# img1 = Image.new("L", (1920, 1080), 255)
# img2 = Image.new("L", (1920, 1080), 0)
# img3 = Image.new("RGB", (1920, 1080), (0, 0, 0))
# img1.show("img1")
# img2.show("img2")
# img3.show("img3")

# img.rotate(180).show()
# img.transpose(Image.FLIP_LEFT_RIGHT).show()

# 滤波器ImageFilter
# BLUR:均值滤波
# CONTOUR:轮廓滤波
# FIND_EDGES:边缘滤波
# EMBOSS:浮雕滤波
# img.filter(ImageFilter.BLUR).show(title="均值滤波")
# img.filter(ImageFilter.CONTOUR).show(title="轮廓滤波")
# img.filter(ImageFilter.FIND_EDGES).show(title="边缘滤波")
# img.filter(ImageFilter.EMBOSS).show(title="浮雕滤波")

# w1 = w // 3
# w2 = w * 2 // 3
# h1 = h // 3
# h2 = h * 2 // 3
# img.crop(box=(0, 0, w1, h1)).save(r"1.jpg")
# img.crop(box=(w1, 0, w2, h1)).save(r"2.jpg")
# img.crop(box=(w2, 0, w, h1)).save(r"3.jpg")
#
# img.crop(box=(0, h1, w1, h2)).save(r"4.jpg")
# img.crop(box=(w1, h1, w2, h2)).save(r"5.jpg")
# img.crop(box=(w2, h1, w, h2)).save(r"6.jpg")
#
# img.crop(box=(0, h2, w1, h)).save(r"7.jpg")
# img.crop(box=(w1, h2, w2, h)).save(r"8.jpg")
# img.crop(box=(w2, h2, w, h)).save(r"9.jpg")

# # 增亮
# img.point(lambda x: x * 2).show()
# #  取深色
# img.point(lambda x: x > 120 and 255).show()

# imgR, imgG, imgB = img.split()
# imgR.show()
# imgG.show()
# imgB.show()

logo = Image.open("logo2.png")
logow, logoh = logo.size
logo = logo.resize((logow // 3, logoh // 3))
logow, logoh = logo.size
# png透明背景mask
r, g, b, a = logo.split()
# Numpy显示长数据全部值
np.set_printoptions(threshold=np.inf)
print(np.array(a))

img.paste(logo, (w - logow, h - logoh), mask=a)
img.show()

# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype("HYWenHei-85W.ttf", 80)
# draw.text((200, 40), "赛车", font=font, fill=(255, 255, 255))
# img.show()

# img = Image.new("RGB", (920, 180), color=getBackColor())
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype("HYWenHei-85W.ttf", 80)
# draw.text((200, 40), getRandomStr()[0], font=font, fill=getFontColor())
# draw.text((280, 40), getRandomStr()[1], font=font, fill=getFontColor())
# draw.text((360, 40), getRandomStr()[2], font=font, fill=getFontColor())
# draw.text((420, 40), getRandomStr()[3], font=font, fill=getFontColor())
# img.show()
