import flask

from recursionFile import scanpath

app = flask.Flask(__name__)

# TODO
# 提供静态文件
# url_for('static', filename='style.css')


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/videoList')
def youtube():
    video_list = scanpath('video', 'mkv')
    return flask.jsonify(video_list)


if __name__ == '__main__':
    app.run()
