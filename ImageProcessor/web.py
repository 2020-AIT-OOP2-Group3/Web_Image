from flask import Flask, request, render_template, url_for, redirect
import os
import imghdr

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    fs = request.files['file']

    if fs.filename == '':
        return render_template("index.html", fileUp='ファイルが未指定です')

    ALLOWED_TYPES = ['jpeg', 'png']
    file_type = imghdr.what(fs.stream)
    if not file_type in ALLOWED_TYPES:
        return render_template("index.html", fileUp="画像ファイルを指定してください")

    dir = "./image_add/"
    fs.save(dir + fs.filename)

    return render_template("index.html", fileUp="ファイルのアップロードに成功しました")

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


if __name__ == '__main__':
    app.run(host="localhost", port=8080)
