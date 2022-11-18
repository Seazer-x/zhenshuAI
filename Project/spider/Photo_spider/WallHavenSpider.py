import os
import re
import time

import requests
from bs4 import BeautifulSoup


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


def getPage(website_url):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif'
                  ',image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh-HK;q=0.9,zh;q=0.8',
        'Cookie': '_pk_id.1.01b8=55a08c2361eedce1.1666842008.; _pk_ses.1.01b8=1; '
                  'XSRF-TOKEN'
                  '=eyJpdiI6InQ5WnplSGpSYnp1akkzaXh1Rk9iemc9PSIsInZhbHVlIjoie'
                  'GJwRGpYY25UTFlMZWJVQWZObFN1SmdrbjJndDQ2bXdHWjI5R1hxVkc3akE0MWlycnY4Tn'
                  'UwSWFmanRwOXZ5RiIsIm1hYyI6IjNkZjU3ZWE0NjNiOGQyNzBiNGY2ZDk3MzgwOTM2YWJjY'
                  'WFmZDZhMDdiMDFlZTQ1NWI1MTE5ZmNiNDE4YzgwMGIifQ==; wallhaven_session=eyJpd'
                  'iI6Ijg0TjBCMUN5bzRhSlpvTEwycnFURnc9PSIsInZhbHVlIjoid1FoREtqSGNvXC9QeFU3Zm'
                  'o3ZWxyTmE2ZmlxTVhjckF1NG1hcE1JbFo5bGNSSHpRa3RuTHNQeGZ6dHdMYnIxRlwvIiwibWFj'
                  'IjoiZGY4MjEwNWI1NzQ3MjdiNTZkN2E0MGZiMWY0NmM0OTRiYWZmYjVlNjhjZWU0MTlmMzIwOW'
                  'Q3YTY3NzA0YjUwNSJ9',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Int'
                      'el Mac OS X 10_15_7) AppleWebKit/537.36 (K'
                      'HTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    session = requests.session()
    session.headers = header
    response = None
    retry_count = 5
    # proxy = get_proxy().get("proxy")
    while retry_count > 0:
        try:
            response = session.get(website_url)
            # response = session.get(url, proxies={"http": "http://{}".format(proxy)})
            if response.status_code == 200:
                response.encoding = 'utf-8'
                return response
        except Exception:
            retry_count -= 1
    # # 删除代理池中代理
    # delete_proxy(proxy)
    if response is None:
        return "响应失败！"


def downloadImage(img_url: str, image_path):
    content = getPage(img_url).content
    index1 = len(img_url) - img_url[::-1].index("/")
    suffix = img_url[index1:]
    print(suffix)
    with open(image_path + suffix, "wb") as img_f:
        img_f.write(content)
        img_f.close()
    with open("img_list.txt", 'a', encoding='utf-8') as list_f:
        list_f.write("\n" + img_url)
        list_f.close()


def gettypePNG(section):
    re.findall('<img.*?data-src="(.*?)" src=""/>', str(section))


def getWHImgUrl(html):
    soup = BeautifulSoup(html, "html.parser")
    urls = set({})
    photo_section = soup.find_all("section", class_="thumb-listing-page")
    for section in photo_section:
        figure = BeautifulSoup(str(section), "html.parser")
        figure_txt = figure.find_all("figure")
        for figure_i in figure_txt:
            url_list = re.findall('<img.*?data-src="(.*?)".*/>', str(figure_i))
            png = re.findall('<span class="png">.*<span>(.*?)</span>.*</span>', str(figure_i))
            for url_item in url_list:
                index1 = len(url_item) - url_item[::-1].index("/")
                suffix = url_item[index1:]
                if len(png) != 0:
                    png_suffix = suffix.replace("jpg", "png")
                    urls.add(
                        str(url_item).replace('th', 'w').replace('small', 'full').replace(suffix,
                                                                                          "wallhaven-" + png_suffix))
                else:
                    urls.add(str(url_item).replace('th', 'w').replace('small', 'full').replace(suffix,
                                                                                               "wallhaven-" + suffix))
    return urls


if __name__ == '__main__':
    image_dir = input("请输入要保存的文件夹（默认images）:\n") or "images"
    images_path = os.path.abspath('') + "/" + image_dir + "/"
    if not os.path.exists(image_dir):
        os.makedirs(images_path)
    top_set = []
    for i in range(29, 61):
        url_str = "https://wallhaven.cc/toplist?page=" + str(i)
        print("url:" + str(url_str))
        res_txt = getPage(url_str).text
        image_urls = getWHImgUrl(res_txt)
        top_set += image_urls
        time.sleep(1)
    top_set = list(set(top_set))
    img_list = []
    print("正在查询已下载图片...")
    with open(r"img_list.txt", 'r') as f:
        img_urls = f.readlines()
        for url in img_urls:
            img_list.append(url.replace('\n', ''))
    not_dw = []
    for m in top_set:
        if m not in img_list:
            not_dw.append(m)
    all_len = str(len(not_dw))
    for index, item in enumerate(not_dw):
        print("正在下载第" + str(index + 1) + "/" + all_len + "张图片,URL:" + str(item))
        downloadImage(item, images_path)
        time.sleep(1)
