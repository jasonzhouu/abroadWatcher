import flask

from recursionFile import scanpath

app = flask.Flask(__name__)


@app.route('/')
def index():
    video_list = scanpath('static', 'mp4')
    print(video_list)
    return flask.render_template('index.html', video_list=video_list)


@app.route('/videoList')
def youtube():
    video_list = scanpath('static', 'mkv')
    return flask.jsonify(video_list)


if __name__ == '__main__':
    app.run(debug='true')
