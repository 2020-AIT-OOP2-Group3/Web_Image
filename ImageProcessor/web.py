from flask import Flask, request, render_template, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
import glob


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                    endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

#それぞれのフォルダを定義
ADD_FOLDER = './image_add'
app.config['ADD_FOLDER'] = ADD_FOLDER

GRAY_FOLDER = './image_gray'
app.config['GRAY_FOLDER'] = GRAY_FOLDER

CARRY_FOLDER = './image_carry'
app.config['CARRY_FOLDER'] = CARRY_FOLDER

FACE_FOLDER = './image_face'
app.config['FACE_FOLDER'] = FACE_FOLDER

MOZAIKU_FOLDER = './image_mozaiku'
app.config['MOZAIKU_FOLDER'] = MOZAIKU_FOLDER


#1.アップロード画像の一覧の出力フォーム
@app.route('/add_list/')
def add_list():
    #image_addの画像を取得
    files = glob.glob("./image_add/*")
    urls = []
    #fileにfilesで取得した画像のurlを格納
    for file in files:
        urls.append("/add/" + os.path.basename(file))
    return render_template("list_add.html", image_files = urls)

#image_addのファイルダウンロード
@app.route('/add/<path:filename>')
def add_file(filename):
    return send_from_directory(app.config['ADD_FOLDER'], filename)

#2.グレースケール画像の一覧の出力フォーム
@app.route('/gray_list/')
def gray_list():
    #image_grayの画像を取得
    files = glob.glob("./image_gray/*")
    urls = []
    #fileにfilesで取得した画像のurlを格納
    for file in files:
        urls.append("/gray/" + os.path.basename(file))
    return render_template("list_gray.html", image_files = urls)

#image_grayのファイルダウンロード
@app.route('/gray/<path:filename>')
def gray_file(filename):
    return send_from_directory(app.config['GRAY_FOLDER'], filename)

#3.carry画像の一覧の出力フォーム
@app.route('/carry_list/')
def carry_list():
    #image_carryの画像を取得
    files = glob.glob("./image_carry/*")
    urls = []
    #fileにfilesで取得した画像のurlを格納
    for file in files:
        urls.append("/carry/" + os.path.basename(file))
    return render_template("list_carry.html", image_files = urls)

#image_carryのファイルダウンロード
@app.route('/carry/<path:filename>')
def carry_file(filename):
    return send_from_directory(app.config['CARRY_FOLDER'], filename)

#4.顔認証画像の一覧の出力フォーム
@app.route('/face_list/')
def face_list():
    #image_carryの画像を取得
    files = glob.glob("./image_face/*")
    urls = []
    #fileにfilesで取得した画像のurlを格納
    for file in files:
        urls.append("/face/" + os.path.basename(file))
    return render_template("list_face.html", image_files = urls)

#image_addのファイルダウンロード
@app.route('/face/<path:filename>')
def face_file(filename):
    return send_from_directory(app.config['FACE_FOLDER'], filename)

#5.モザイク画像の一覧の出力フォーム
@app.route('/mozaiku_list/')
def mozaiku_list():
    #image_addの画像を取得
    files = glob.glob("./image_mozaiku/*")
    urls = []
    #fileにfilesで取得した画像のurlを格納
    for file in files:
        urls.append("/add/" + os.path.basename(file))
    return render_template("list_mozaiku.html", image_files = urls)

#image_addのファイルダウンロード
@app.route('/add/<path:filename>')
def mozaiku_file(filename):
    return send_from_directory(app.config['ADD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(host="localhost", port=8080)
