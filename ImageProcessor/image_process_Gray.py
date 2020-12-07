import os
import time
import sys
import cv2

OUT_DIR = "image_gray/"

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
    
    #image_grayディレクトリにあるファイル名のリスト
    gray_files = os.listdir("image_gray")
    #全てグレースケール化
    for gray_file in gray_files:
        #画像を読み込む
        img2 = cv2.imread(OUT_DIR + gray_file)
        #上記で読み込んだファイルを削除
        os.remove(OUT_DIR + gray_file)
        #グレースケール化
        gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
        #画像保存
        cv2.imwrite(OUT_DIR + gray_file,gray)


if __name__ in '__main__':
    # 処理が終了しないようにスリープを挟んで無限ループ
    while True:
        # 1秒ごとに監視
        time.sleep(1)
        ready()
