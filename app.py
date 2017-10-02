from flask import Flask
app = Flask(__name__)


@app.route('/youtube')
def youtube():
    return 'hello'


if __name__ == '__main__':
    app.run()
