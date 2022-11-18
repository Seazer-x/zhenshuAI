from flask import Flask

app = Flask(__name__)


@app.route("/")
def display():
    return "<pre><h1/>    Python Web页面<br/></pre><pre><h6/>        flask页面</pre>"


@app.route("/<name>")
@app.route("/user=<name>")
def displayName(name):
    return "<h1/>你好！" + name + "."


if __name__ == '__main__':
    app.run()
