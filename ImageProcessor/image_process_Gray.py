import os
import time
import sys
import cv2

OUT_DIR = "image_gray/"

"""
関数説明：入力画像ディレクトリにある画像を全てグレースケール化する
"""
def Turn_image_add_into_Gray():
    #入力画像ディレクトリにあるファイル名のリスト
    add_files = os.listdir("image_add")
    #出力画像ディレクトリにあるファイル名のリスト
    gray_files = os.listdir("image_gray")
    #入力画像ディレクトリにある画像の中でグレースケール化されてない画像を見つける
    notgray_files = [i for i in add_files if not i in gray_files]
    #全てグレースケール化する
    for notgray_file in notgray_files:
        #画像を読み込む
        img = cv2.imread("image_add/" + notgray_file)
        #グレースケール化
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        #画像保存
        cv2.imwrite(OUT_DIR + notgray_file,gray)

"""
関数説明：出力画像ディレクトリにある画像を全てグレースケール化する
"""
def Turn_image_gray_into_Gray():   
    #出力画像ディレクトリにあるファイル名のリスト
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

"""
関数説明：入力画像ディレクトリにある画像の数と出力画像ディレクトリにある画像の数を等しくする関数
"""
def Adjust_the_number_of_files():
    #入力画像ディレクトリにあるファイル名のリスト
    add_files = os.listdir("image_add")
    #出力画像ディレクトリにあるファイル名のリスト
    gray_files = os.listdir("image_gray")
    #出力画像ディレクトリから入力画像ディレクトリに存在しないファイル名を削除
    none_exit_in_add_files = [i for i in gray_files if not i in add_files]
    for none_exit_in_add_file in none_exit_in_add_files:
        #上記で読み込んだファイルを削除
        os.remove(OUT_DIR + none_exit_in_add_file)
    


if __name__ in '__main__':
    # 処理が終了しないようにスリープを挟んで無限ループ
    while True:
        # 1秒ごとに監視
        time.sleep(1)
        Turn_image_add_into_Gray()
        Turn_image_gray_into_Gray()
        Adjust_the_number_of_files()
