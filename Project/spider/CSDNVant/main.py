import json
import os.path
import sqlite3
import sys
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# 设置参数
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# 带入参数和插件地址 并执行Chrome
driver = webdriver.Chrome(options=options, executable_path='chromedriver')
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
    """
})


def get_track(distance):  # distance为传入的总距离
    # 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 50

    while current < distance:
        if current < mid:
            # 加速度为2
            a = 70
        else:
            # 加速度为-2
            a = 60
        v0 = v
        # 当前速度
        v = v0 + a * t
        # 移动距离
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += move
        # 加入轨迹
        track.append(round(move))
    return track  # list 返回的是整个滑动条的多个焦点，可以模拟鼠标的缓慢滑动


def move_to_gap(ele_driver, slider, tracks):  # slider是要移动的滑块,tracks是要传入的移动轨迹
    ActionChains(ele_driver).click_and_hold(slider).perform()
    for x in tracks:
        ActionChains(ele_driver).move_by_offset(xoffset=x, yoffset=0).perform()
    time.sleep(0.5)
    ActionChains(ele_driver).release().perform()


def dbCreate():
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE User
           (NAME   TEXT UNIQUE  NOT NULL,
           PASSWD         TEXT     NOT NULL);''')
    print("数据表创建成功")
    db.commit()
    db.close()


def insertUser(username, passwd):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("INSERT INTO User (NAME,PASSWD) VALUES(?,?)", (username, passwd))
    db.commit()
    print("数据插入成功")
    db.close()


def getUser():
    username = []
    passwd = []
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    users = cursor.execute("SELECT * FROM User")
    for i in users:
        username.append(i[0])
        passwd.append(i[1])
    db.commit()
    db.close()
    return username, passwd


def CSDN_Login():
    username, password = getUser()
    user = ""
    passwd = ""
    if len(username) != 0:
        if username[0] is not None and password[0] is not None:
            user = username[0]
            passwd = password[0]
    else:
        user = input("请输入用户名：")
        passwd = input("请输入密码：")
        insertUser(user, passwd)
    if user.replace(" ", "") == "" or passwd.replace(" ", "") == "":
        print("请输入用户名和密码")
        sys.exit(0)
    driver.get("https://passport.csdn.net/account/login")
    time.sleep(3)
    print("请手动刷新并登录后继续")
    # 点击登录
    # driver.find_element(By.XPATH, "//div[@class='login-form-item']/button").click()
    # sli_ele = driver.find_element(By.XPATH, "//span[@id='nc_1_n1z']")
    # sli_div = driver.find_element(By.XPATH, "//div[@id='nc_1__scale_text']")
    # slider = sli_ele.size.get("width")
    # div = sli_div.size.get("width")
    # move_to_gap(driver, sli_ele, get_track(div - slider + 10))
    time.sleep(10)
    login = input("是否已经登录？回车确认：")
    cookies = driver.get_cookies()
    print(cookies)
    with open("cookies.txt", "w") as fp:
        json.dump(cookies, fp)


def like(url_list):
    for url in url_list:
        driver.get(url)
        with open("cookies.txt", "r") as fp:
            cookies = json.load(fp)
            # cookie["path"] = url[url.index(".net") + 4:]
            # cookie["domain"] = "blog.csdn.net"
            for cookie in cookies:
                print(cookie)
                driver.add_cookie(cookie)
            print("cookies加载完成，成功登录")
        print(driver.get_cookies())
        time.sleep(3)
        driver.find_element(By.XPATH, "//li[@id='is-like']").click()
        print("点赞完成！")
        time.sleep(3)


if __name__ == '__main__':
    if not os.path.exists("db.sqlite3"):
        dbCreate()
    urls = []
    get_cookie = "1"
    switch = input("1.一篇文章，2.多篇文章：")
    if switch == "1":
        urls.append(input("请输入url："))
    elif switch == "2":
        if not os.path.exists("urls.txt"):
            f = open("urls.txt", 'w')
            f.write("")
            f.close()
        while True:
            flag = input("请将url放入urls.txt（每行一条url）后键入y继续：")
            if not open("urls.txt", 'r').readline().replace(" ", "") == "":
                break
        if flag.upper() == "Y":
            url_file = open("urls.txt", 'r')
            urls = [x for x in url_file.readlines()]
            url_file.close()
        else:
            print("退出")
            sys.exit(0)
    else:
        print("参数错误！")
        sys.exit(0)
    if os.path.exists('cookies.txt'):
        with open("cookies.txt", 'r') as f:
            if type(json.load(f)) == dict:
                get_cookie = input("存在cookies文件是否重新获取？1.重新获取，任意其他键继续：")
    if get_cookie == "1":
        CSDN_Login()
    like(urls)
