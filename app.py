import flask

from recursionFile import scanpath

app = flask.Flask(__name__)


# TODO
# 首页展示播放列表，详情页播放

@app.route('/')
def index():
    video_list = scanpath('static', 'mp4')
    print(video_list)
    return flask.render_template('index.html', video_list=video_list)


if __name__ == '__main__':
    app.run(debug='true')
