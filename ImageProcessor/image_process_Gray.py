import os
import time
import sys
import cv2

# スクリプト実行用ディレクトリを絶対パスで指定する
BASEDIR = os.path.abspath(os.path.dirname(__file__))
OUT_DIR = "image_gray/"

#初期状態の処理
def ready():
    #image_addディレクトリにあるファイル名のリスト
    add_files = os.listdir("image_add")
    #image_grayディレクトリにあるファイル名のリスト
    gray_files = os.listdir("image_gray")
    #image_addにある画像の中でグレースケール化されてない画像を見つける
    notgray_files = [i for i in add_files if not i in gray_files]
    #全てグレースケール化する
    for notgray_file in notgray_files:
        #画像を読み込む
        img = cv2.imread("image_add/" + notgray_file)
        #グレースケール化
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        #画像保存
        cv2.imwrite(OUT_DIR + notgray_file,gray)

if __name__ in '__main__':
    while True:
        try:
            # 処理が終了しないようにスリープを挟んで無限ループ
            while True:
                # 1秒ごとに監視
                time.sleep(1)
                ready()
        # 無限ループからキー入力で監視をやめる
        except KeyboardInterrupt:
            observer.stop()
        # observer.stop()だけでは裏で動くスレッドは停止してないので、完全に停止するまで待つためにjoin()を呼んでいる。
        observer.join()
