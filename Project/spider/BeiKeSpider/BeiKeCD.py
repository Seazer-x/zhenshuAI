import re

import requests
import xlwt
from bs4 import BeautifulSoup


# 采集器
def get(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/102.0.5005.63 Safari/537.36",
        "content-type": "text/html;charset=utf-8",
        "Cookie": "lianjia_uuid=b115639d-eb1a-4dfe-993e-e987b1098103; select_city=510100; "
                  "login_ucid=2000000001689088; lianjia_token=2.00125dc05668ed6bba03f0e967a9bd1513; "
                  "lianjia_token_secure=2.00125dc05668ed6bba03f0e967a9bd1513; "
                  "security_ticket=KdURlC+yI+qNePJWsx3DqMOGqd77IKlrUoHoBJccZW20cH/+Pyc2ca+S+QpNXav2IEbAur"
                  "+q7OlnGobGoMOKI4F9/iPnt67+vlftr4meDwvkyx5dkXq+S2nKEq/cDIPnX7F5Od3Ux/PhTB6GQt/YmvTeAK+IKbNPAQEu"
                  "/suuZGg=; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221813cf9c3ac6d-0467eb7684b105"
                  "-14333270-2073600-1813cf9c3ad5e3%22%2C%22%24device_id%22%3A%221813cf9c3ac6d-0467eb7684b105"
                  "-14333270-2073600-1813cf9c3ad5e3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22"
                  "%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22"
                  "%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88"
                  "%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C"
                  "%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wychengdu%22%2C%22"
                  "%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; "
                  "cy_ip=182.150.22.82; lianjia_ssid=cdf9cb85-03ff-4cd9-bac3-cf29b532b006; "
                  "f-token=fbGrq2rT0Fsd9VaOcYUJdcheeTZAC2fJGNeiT2TlWezIuUVBfJAm6IphsGjC+22uHq4oi"
                  "+FnFL1pLlWqFOYnFjr5SCOxJRyF1TJGCZlQRF9VffciNZodG8/DH75sN1FvHFe7ZhWoyWlEETVa/w== "
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response
    else:
        return "爬取异常"


def get_data():
    # 贝壳网成都地区分类房源链接，末尾加参数 [ 1 , 100 ]
    us = [
        "https://cd.ke.com/ershoufang/jinjiang/pg", "https://cd.ke.com/ershoufang/qingyang/pg",
        "https://cd.ke.com/ershoufang/wuhou/pg", "https://cd.ke.com/ershoufang/gaoxin7/pg",
        "https://cd.ke.com/ershoufang/chenghua/pg", "https://cd.ke.com/ershoufang/jinniu/pg",
        "https://cd.ke.com/ershoufang/tianfuxinqu/pg", "https://cd.ke.com/ershoufang/gaoxinxi1/pg",
        "https://cd.ke.com/ershoufang/shuangliu/pg", "https://cd.ke.com/ershoufang/wenjiang/pg",
        "https://cd.ke.com/ershoufang/pidou/pg", "https://cd.ke.com/ershoufang/longquanyi/pg",
        "https://cd.ke.com/ershoufang/xindou/pg", "https://cd.ke.com/ershoufang/tianfuxinqunanqu/pg",
        "https://cd.ke.com/ershoufang/qingbaijiang/pg", "https://cd.ke.com/ershoufang/doujiangyan/pg",
        "https://cd.ke.com/ershoufang/pengzhou/pg", "https://cd.ke.com/ershoufang/jianyang/pg",
        "https://cd.ke.com/ershoufang/xinjin/pg", "https://cd.ke.com/ershoufang/chongzhou1/pg",
        "https://cd.ke.com/ershoufang/dayi/pg", "https://cd.ke.com/ershoufang/jintang/pg",
        "https://cd.ke.com/ershoufang/pujiang/pg", "https://cd.ke.com/ershoufang/qionglai/pg"
    ]
    urls = []  # 循环添加之后，应有2400个链接，每个链接有30条数据。
    for u in us:
        for i in range(1, 101):
            urls.append(u + str(i))
    # 房源信息
    houses = []
    for url in urls:
        html = get(url).text
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("li", class_="clear"):
            house = []
            item = str(item)
            # 楼盘名称 <span class="positionIcon"></span><a href="https://cd.ke.com/xiaoqu/1611041535054/">万达锦华城</a>
            lnRe = re.findall(r'<span class="positionIcon"></span><a href=.*">(.*?)</a>', item)
            lp = ""
            if len(lnRe) > 0:
                lp = lnRe[0]
            house.append(lp)
            # 房源名称
            hnRe = r'<a class="VIEWDATA CLICKDATA maidian-detail".*>(.*?)</a>'
            house.append(re.findall(hnRe, item)[0])
            # 价格 <span class=""> 218</span>
            jg = '<span class=""> (.*?)</span>'
            jg = re.findall(jg, item)
            j = ""
            if len(jg) > 0:
                j = jg[0]
            house.append(j)
            js = r'<span class="houseIcon"></span>(.*?)</div>'
            jss = str(re.findall(re.compile(js, re.S), item)[0])
            jss = jss.replace(" ", "").replace("\n", "")
            house.append(jss)
            gzfb = r'<span class="starIcon"></span>(.*?)</div>'
            gzfb = re.compile(gzfb, re.S)
            gzfb = re.findall(gzfb, item)[0]
            gzfbs = str(gzfb).replace("\n", "").replace(" ", "").split("/")
            # 关注人数
            house.append(gzfbs[0])
            # 发布时间
            house.append(gzfbs[1])
            # 单价 <div class="unitPrice" data-hid="106111479586" data-price="">
            #                     <span>18,849元/平</span>
            #                   </div>
            dj = r'<span>(.*?)元/平</span>'
            d = ""
            t = re.findall(dj, item)
            if len(t) > 0:
                d = str(t[0]).replace(",", "")
            house.append(d)
            # 房源图片data-original="(.*?)"
            tu = r'data-original="(.*?)"'
            house.append(re.findall(tu, item)[0])
            houses.append(house)
    return houses


def write2excel(dataList):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('贝壳网数据.xls', cell_overwrite_ok=True)
    col = ('楼盘', '房源', '价格', '介绍', '关注', '发布时间', '单价', '图片')  # 表格标题
    for i in range(0, len(col)):  # 把列名写入第一行
        sheet.write(0, i, col[i])
    for i in range(0, len(dataList)):  # 把爬取的数据写入excel
        data = dataList[i]
        for j in range(0, len(col)):
            sheet.write(i + 1, j, data[j])
    book.save('贝壳网数据.xls')


write2excel(get_data())
