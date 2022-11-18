from flask import Flask, request

app = Flask(__name__)


@app.route("/get_method", methods=["GET", "POST"])
def index():
    return "<h1/>请求方式：" + request.method + \
           "<br/>用户名：" + request.form.get("username") + \
           "<br/>密码：" + request.form.get("passwd")


if __name__ == '__main__':
    app.run()
