import flask
import urllib.parse

from recursionFile import scanpath

app = flask.Flask(__name__)


# TODO
# 输入youtube list 名，则开始下载

# TODO
# URL 转义

@app.route('/')
def index():
    video_list = scanpath('static', 'mp4')
    # encode_video_list = []
    # for video in video_list:
    #     encode_video_list.append(urllib.parse.quote(video))
    # print(video_list, encode_video_list)
    template_list = ''
    for video in video_list:
        template_list += '<ul><li><a href="/video/'
        template_list += urllib.parse.quote(video[7:])
        template_list += '">'
        template_list += video[7:-4]
        template_list += '</a></li></ul>'

    return template_list
    # return flask.render_template('index.html', template_list=template_list)


@app.route('/video/<video_name>')
def play_video(video_name):
    video_name = urllib.parse.quote(video_name)
    print('播放  ' + video_name)
    return flask.render_template('playVideo.html', video_name=video_name)

