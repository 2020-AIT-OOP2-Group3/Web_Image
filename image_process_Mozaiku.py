import cv2
import time
import os
import sys

# スクリプト実行用ディレクトリを絶対パスで指定する
BASEDIR = os.path.abspath(os.path.dirname(__file__))
OUT_DIR = "image_mozaiku/"

#入力画像ディレクトリにある画像を処理
def Turn_image_add_into_Mozaiku():
    #image_addディレクトリにあるファイル名のリスト
    add_files = os.listdir("image_add")
    #image_mozaikuディレクトリにあるファイル名のリスト
    mozaiku_files = os.listdir("image_mozaiku")
    #image_addにある画像の中で画像処理されてない画像を見つける
    notmozaiku_files = [i for i in add_files if not i in mozaiku_files]
    #全て画像処理
    for notmozaiku_file in notmozaiku_files:
        #画像を読み込む
        mozaiku = cv2.imread("image_add/" + notmozaiku_file)
        #顔認識処理
        gray = cv2.cvtColor(mozaiku, cv2.COLOR_BGR2GRAY)
        cascade_path = BASEDIR + "/haarcascade_frontalface_default.xml"
        cascade = cv2.CascadeClassifier(cascade_path) 
        facerect = cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=4, minSize=(100, 100))
        
        if len(facerect) > 0:
            for face in facerect:
                x, y, w, h = face
                roi = mozaiku[y:y+h, x:x+w]
                roi = cv2.resize(roi, (w//10, h//10))
                roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_NEAREST)
                mozaiku[y:y+h, x:x+w] = roi          
    
        #画像保存
        cv2.imwrite(OUT_DIR + notmozaiku_file,mozaiku)

#出力画像ディレクトリにある画像を処理
def Turn_image_mozaiku_into_Mozaiku():
    mozaiku_files = os.listdir("image_mozaiku")
    for mozaiku_file in mozaiku_files:
        #画像を読み込む
        mozaiku2 = cv2.imread(OUT_DIR + mozaiku_file)
        os.remove(OUT_DIR + mozaiku_file)
        #顔認識処理
        gray = cv2.cvtColor(mozaiku2, cv2.COLOR_BGR2GRAY)
        cascade_path = BASEDIR + "/haarcascade_frontalface_default.xml"
        cascade = cv2.CascadeClassifier(cascade_path) 
        facerect = cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=4, minSize=(100, 100))
        
        if len(facerect) > 0:
            for face in facerect:
                x, y, w, h = face
                roi = mozaiku2[y:y+h, x:x+w]
                roi = cv2.resize(roi, (w//10, h//10))
                roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_NEAREST)
                mozaiku2[y:y+h, x:x+w] = roi         
        #画像保存
        cv2.imwrite(OUT_DIR + mozaiku_file,mozaiku2)

#入力、出力ディレクトリにある画像数を揃える
def Adjust_the_number_of_files():
    adds_files = os.listdir("image_add")
    mozaiku_files = os.listdir("image_mozaiku")
    none_exit_in_add_files = [i for i in mozaiku_files if not i in adds_files]
    for none_exit_in_add_file in none_exit_in_add_files:
        os.remove(OUT_DIR + none_exit_in_add_file)

if __name__ in '__main__':
    # 処理が終了しないようにスリープを挟んで無限ループ
    while True:
        # 1秒ごとに監視
        time.sleep(1)
        Turn_image_add_into_Mozaiku()
        Turn_image_mozaiku_into_Mozaiku()
        Adjust_the_number_of_files()
