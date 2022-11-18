import hashlib
import webbrowser


from flask import Flask, render_template, request, make_response, session, redirect, url_for
from werkzeug.utils import secure_filename

from Util.JWTUtil import *

app = Flask(__name__)

users = {"fubaiping": "123456", "qiuwulun": "123456", "liuyukang": "123456", "wanxiaohu": "123456"}


# md5加密
def password_hash(password):
    hash_md5 = hashlib.md5()
    hash_md5.update(str(password).encode('utf-8'))
    return hash_md5.hexdigest()


# 模板变量
@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)


# 请求方式
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        passwd = request.form.get("passwd")
        if users.get(username) is not None and passwd == users.get(username):
            print("登录成功。")
            session["username"] = username
            return render_template("index.html", username=username)
        else:
            print("登录失败！")
            return render_template("index.html")


# 文件上传
@app.route("/upload", methods=["POST"])
def upload():
    if request.method == 'POST':
        file = request.files.get("the_file")
        file.save(secure_filename(file.filename))
    return "上传成功！"


# 写入cookie
@app.route("/write_cookie", methods=["POST"])
def write_cookie():
    if request.method == 'POST':
        username = request.form.get("username")
        res = make_response("write_cookie")
        res.set_cookie('Cypress', getJWT(username), max_age=36000)
        return res


# cookie
@app.route("/read_cookie")
def read_cookie():
    cookie = request.cookies.get("Cypress")
    return cookie


@app.route("/check_login")
def check_login():
    return session.get("username")


@app.route('/redirect')
def redirectHtml():
    return redirect(url_for('redirect2'))


@app.route('/redirect2')
def redirect2():
    webbrowser.open("https://www.baidu.com")
    return "重定向之后的页面"


# @app.route('/jieba', methods=['GET', 'POST'])
# def jiebaCut():
#     words = request.form.get("message")
#     cut_words = jieba.cut(words, cut_all=False)
#     print("Default Mode: " + " ".join(cut_words))  # 精确模式
#     return render_template("jieba.html", result=" ".join(cut_words))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404_3.html'), 404


if __name__ == '__main__':
    app.secret_key = "Cypress"
    app.run()
