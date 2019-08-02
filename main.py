from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/u')
def hello1():
    d = {"okk":1,"test":3}
    return jsonify(d)

if __name__ == '__main__':
    app.run()
