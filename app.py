from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["POST"])
def hello_world():  # put application's code here
    return request.get_json()


if __name__ == '__main__':
    app.run()
