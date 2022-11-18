import os
import pymysql

from Project.SpiderUtil.util import *

if __name__ == '__main__':
    write2excel(getData())
#
# image_dir = input("请输入要保存的文件夹（默认images）:\n") or "images"
# images_path = os.path.abspath('.') + "/" + image_dir + "/"
# if not os.path.exists(image_dir):
#     os.makedirs(images_path)
# print(images_path)
# for index, item in enumerate(image_urls):
#     print("正在下载第" + str(index + 1) + "张图片.....")
#     downloadImage(item, index, images_path)

# # 打开数据库连接
# db = pymysql.connect(host='localhost',
#                      user='root',
#                      password='52Myworld',
#                      database='doubantop250')
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
# name, director, starring, time, nation, mv_type, score, cover = "", "", "", "", "", "", "", ""
# # SQL 插入语句
# sql = "INSERT INTO Top250(name,director, starring, time, nation,type,score,cover) \
#        VALUES ('%s', '%s',  %s,  '%s',  %s,'%s', '%s','%s')" % \
#       (name, director, starring, time, nation, mv_type, score, cover)
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 执行sql语句
#     db.commit()
# except:
#     # 发生错误时回滚
#     db.rollback()
#
# # 关闭数据库连接
# db.close()
