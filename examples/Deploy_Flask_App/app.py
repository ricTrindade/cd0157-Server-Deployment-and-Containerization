from flask import Flask
APP = Flask(__name__)


@APP.route('/')
def hello_world():
    return 'Hello, My name is Ricardo and I love Ellie!\n'



if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
