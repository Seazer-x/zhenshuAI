import cv2
import numpy as np
from PIL import Image
from rich.progress import track


def writeVideo2MP4(video_uri, file_name: str, fps=30):
    cap = cv2.VideoCapture(video_uri)  # 获取视频对象
    w, h = int(cap.get(3)), int(cap.get(4))
    out = cv2.VideoWriter(file_name, cv2.VideoWriter_fourcc(*'mp4v'),
                          fps, (w, h))
    while True:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def getCamera():
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


# 为视频添加水印
def addLogo2Video(video_url="纳西妲copy.mp4", logo_path="d4q26mBAqj.png", out_video="logo_video.mp4"):
    video = cv2.VideoCapture(video_url)
    w, h = int(video.get(3)), int(video.get(4))
    out = cv2.VideoWriter(out_video, cv2.VideoWriter_fourcc(*'mp4v'),
                          30, (w, h))
    Watermark = Image.open(logo_path)
    markw, markh = Watermark.size
    Watermark = Watermark.resize((markw // 3, markh // 3))
    markw, markh = Watermark.size
    while video.isOpened():
        ret, frame = video.read()
        if ret:
            pn_frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            pn_frame.paste(Watermark, (w - markw, h - markh), mask=Watermark)
            frame = cv2.cvtColor(np.asarray(pn_frame), cv2.COLOR_RGB2BGR)
            out.write(frame)
        else:
            break
    out.release()
    video.release()


# 获取图像的二值图
def getBImage(img):
    img = Image.open(img)
    gray_img = img.convert("L")
    w, h = gray_img.size
    for x in range(w):
        for y in range(h):
            if gray_img.getpixel((x, y)) < 128:
                img.putpixel((x, y), (0, 0, 0))
            else:
                img.putpixel((x, y), (255, 255, 255))
    return img


# 为图片添加国旗
def getStarAvatar(avatar, logo="img_1.png"):
    avatar_img = Image.open(avatar)
    w, h = avatar_img.size
    logo = Image.open(logo)
    logo.thumbnail((w, h))
    avatar_img.paste(logo, (0, 0), mask=logo)
    return avatar_img
