from flask import Flask
from flask import jsonify
from recursionFile import scanpath

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'


@app.route('/videoList')
def youtube():
    video_list = scanpath('video', 'mkv')
    return jsonify(video_list)


if __name__ == '__main__':
    app.run()
