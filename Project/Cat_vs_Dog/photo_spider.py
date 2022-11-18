import os.path
import re

import cv2
import requests


class PhotoSpider:
    def __init__(self, url: str, out_path="data"):
        self.url = url
        self.out_path = out_path
        self.img_urls = []
        if not os.path.exists(out_path):
            os.makedirs(out_path)

    @staticmethod
    def __getPage(url):
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                      'application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': 'bid=FatDIieHFAE; ll="118318"; '
                      '_vwo_uuid_v2=DB22934FD7A8720492977EB830AA1C14C|47e41f8e73927f1cafafc1e69875f9f8; '
                      '_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1666768562%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; '
                      '_pk_ses.100001.4cf6=*; ap_v=0,6.0; '
                      '_pk_id.100001.4cf6=17fe2ade93092bcc.1665669560.2.1666770214.1665669560.',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52 '
        }
        session = requests.session()
        session.headers = header
        response = session.get(url)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response
        else:
            return "响应失败！"

    def downloadImage(self, cate):
        if len(self.img_urls) == 0:
            print("请先调用setImageUrl。")
            partner = input("请输入正则表达式：")
            self.setImgUrl(partner)
        length = len(self.img_urls)
        for index, img in enumerate(self.img_urls):
            print(f"正在下载第{index + 1}/{length}张图片...")
            content = self.__getPage(img).content
            img_path = os.path.join(self.out_path, cate)
            if not os.path.exists(img_path):
                os.makedirs(img_path)
            tail = img.split("/")[-1]
            with open(os.path.join(img_path, cate + str(index) + tail[tail.index("."):tail.index("?")]), "wb") as f:
                f.write(content)
                f.close()

    def setImgUrl(self, partner):
        res = self.__getPage(self.url).text
        # with open("response.txt", "w", encoding="utf-8") as f:
        #     f.write(res)
        #     f.close()
        # print(res)
        self.img_urls.extend(re.findall(partner, res))

    def getImgUrl(self):
        return self.img_urls


if __name__ == '__main__':
    ps = PhotoSpider("https://www.pexels.com/zh-cn/search/%E8%B2%93/")
    pre = re.compile('<img src="(.*?)"')
    ps.setImgUrl(pre)
    print(ps.getImgUrl())
    # print(len(ps.getImgUrl()))
    # ps.downloadImage("cat")
    img = cv2.resize(cv2.imread(r"E:\Fbp\zhenshuAI\Project\Cat_vs_Dog\data\cat\cat0.jpeg"), (400,400))
    cv2.imshow("img", img)
    cv2.moveWindow("img", 100, 500)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
