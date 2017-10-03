import flask

from recursionFile import scanpath

app = flask.Flask(__name__)


# TODO
# 输入youtube list 名，则开始下载

@app.route('/')
def index():
    video_list = scanpath('static', 'mp4')
    print(video_list)
    return flask.render_template('index.html', video_list=video_list)


@app.route('/video/<video_name>')
def play_video(video_name):
    return flask.render_template('playVideo.html', video_name=video_name)


if __name__ == '__main__':
    # app.run(debug='true')
    app.run(host='0.0.0.0')
