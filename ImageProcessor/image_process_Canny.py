import os
import cv2
import time
import sys

OUT_DIR = "image_carry/"

'''
関数説明：入力画像ディレクトリにある画像を全てcarry法で加工
'''

def Turn_image_add_into_carry():
    path = './image_add'
    add_files = os.listdir(path)
    carry_files = os.listdir("image_carry/")
    notcarry_files = [i for i in add_files if not i in carry_files]
    for notcarry_files in notcarry_files:
        img = cv2.imread("image_add/" + notcarry_files)
        carry = cv2.Canny(img,100,200)
        cv2.imwrite(OUT_DIR + notcarry_files,carry)

'''
関数説明：出力画像ディレクトリにある画像を全てcarry法で加工
'''

def Turn_image_carry_into_carry():
    carry_files = os.listdir("image_carry")
    for carry_files in carry_files:
        img2 = cv2.imread(OUT_DIR + carry_files)
        os.remove(OUT_DIR + carry_files)
        carry = cv2.Canny(img2,100,200)
        cv2.imwrite(OUT_DIR + carry_files,carry)

"""
関数説明：入力画像ディレクトリにある画像の数と出力画像ディレクトリにある画像の数を等しくする関数
"""
def Adjust_the_number_of_files():
    #入力画像ディレクトリにあるファイル名のリスト
    add_files = os.listdir("image_add")
    #出力画像ディレクトリにあるファイル名のリスト
    carry_files = os.listdir("image_carry")
    #出力画像ディレクトリから入力画像ディレクトリに存在しないファイル名を削除
    none_exit_in_add_files = [i for i in carry_files if not i in add_files]
    for none_exit_in_add_file in none_exit_in_add_files:
        #上記で読み込んだファイルを削除
        os.remove(OUT_DIR + none_exit_in_add_file)

if __name__ in '__main__':
    # 処理が終了しないようにスリープを挟んで無限ループ
    while True:
        # 1秒ごとに監視
        time.sleep(1)
        Turn_image_add_into_carry()
        Turn_image_carry_into_carry()
        Adjust_the_number_of_files()