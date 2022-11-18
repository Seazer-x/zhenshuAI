import re

import requests
import xlrd
import xlwt
from bs4 import BeautifulSoup


def getPage(url):
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


def downloadImage(img_url: str, index, images_path):
    content = getPage(img_url).content
    with open(images_path + str(index) + img_url[img_url.index("."):], "wb") as f:
        f.write(content)
        f.close()


def getOlText(res):
    pattern = re.compile('<ol class="grid_view">.*<li>(.*)</li>', re.S)
    return re.findall(pattern, res)


def getImgUrl(res):
    return re.findall('<img.*src="(.*?)">', res)


def getLinkUrl(res):
    return re.findall('<a href="(.*?)">', res)


def getCoverUrl(res):
    return re.findall(r'<img.*src="(.*?)"', res)


def getName(res):
    pattern = re.compile('<span class="title">(.*?)</span>', re.S)
    return re.findall(pattern, res)


def getOtherName(res):
    return re.findall('<span class="other">(^[A-Za-z]+$)</span>', res)


def getRate(res):
    return re.findall('<span class="rating_num" property="v:average">(.*?)</span>', res)


def getCount(res):
    return re.findall('<span>(.*?)人评价</span>', res)


def getInfo(res):
    return re.findall('<span class="inq">(.*?)</span>', res)


def getContent(res):
    pattern = re.compile('<p class="">(.*?)</p>', re.S)
    return re.findall(pattern, res)


def getData():
    datas = []
    for i in range(10):
        url = "https://movie.douban.com/top250?start=" + str(i * 25) + "&filter="
        html = getPage(url).text
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):
            data = []
            item = str(item)
            link = getLinkUrl(item)[0]
            data.append(link)
            img = getCoverUrl(item)[0]
            data.append(img)
            names = getName(item)
            other_name = getOtherName(item)
            if len(names) >= 2:
                data.append(str(names[0]))  # 中文
                data.append(str(names[1]).replace("/", "").strip())
            else:
                data.append(str(names[0]))  # 中文
                if other_name:
                    data.append(str(other_name).replace("/", "").strip())
                else:
                    data.append("")
            rating = getRate(item)[0]
            data.append(rating)
            count = getCount(item)
            data.append(count)
            if len(getInfo(item)) != 0:
                info = getInfo(item)[0]
                data.append(info)
            content = getContent(item)[0]
            content = str(content).replace("/...<br/>", "").replace("...<br/>", "").replace(" ", "").strip()
            data.append(content)
            datas.append(data)
    return datas


def write2excel(dataList):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet("豆瓣电影Top250", cell_overwrite_ok=True)
    col = ('电影详情连接', '图片链接', '影片中文名', '影片英文名', '评分', '评价数', '概括', '影片相关信息')
    for i in range(0, len(col)):
        sheet.write(0, i, col[i])
    for i in range(0, len(dataList)):
        data = dataList[i]
        for j in range(0, len(col)):
            try:
                sheet.write(i + 1, j, data[j])
            except Exception:
                book.save("豆瓣网数据.xls")
                break
    book.save("豆瓣网数据.xls")


def readExcel():
    douban = xlrd.open_workbook("豆瓣网数据.xls")
    sheet = douban.sheets()[0]
    for i in range(0, sheet.nrows):
        for j in range(0, sheet.ncols):
            print(sheet.cell(i, j).value, end="\t")
        print()


if __name__ == '__main__':
    readExcel()
