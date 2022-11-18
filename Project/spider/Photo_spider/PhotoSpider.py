import os

from Project.SpiderUtil.util import *

if __name__ == '__main__':
    url_str = input("请输入要爬取的网址:\n")
    res_txt = getPage(url_str).text
    image_urls = getImgUrl(res_txt)
    image_dir = input("请输入要保存的文件夹（默认images）:\n") or "images"
    images_path = os.path.abspath('') + "/" + image_dir + "/"
    if not os.path.exists(image_dir):
        os.makedirs(images_path)
    print(images_path)
    for index, item in enumerate(image_urls):
        print("正在下载第" + str(index + 1) + "张图片.....")
        downloadImage(item, index, images_path)
