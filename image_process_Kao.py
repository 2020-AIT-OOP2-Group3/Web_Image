import cv2
import time
import os
import sys

# スクリプト実行用ディレクトリを絶対パスで指定する
BASEDIR = os.path.abspath(os.path.dirname(__file__))
OUT_DIR = "image_face/"

#入力画像ディレクトリにある画像を処理
def Turn_image_add_into_Face():
    #image_addディレクトリにあるファイル名のリスト
    add_files = os.listdir("image_add")
    #image_faceディレクトリにあるファイル名のリスト
    face_files = os.listdir("image_face")
    #image_addにある画像の中で画像処理されてない画像を見つける
    notface_files = [i for i in add_files if not i in face_files]
    #全て画像処理
    for notface_file in notface_files:
        #画像を読み込む
        face = cv2.imread("image_add/" + notface_file)
        #顔認識処理
        gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        cascade_path = BASEDIR + "/haarcascade_frontalface_default.xml"
        cascade = cv2.CascadeClassifier(cascade_path) 
        facerect = cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=4, minSize=(100, 100))
        
        rectangle_color = (0, 0, 255)
    
        if len(facerect) > 0:
            for rect in facerect:
                cv2.rectangle(face, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), rectangle_color, thickness=2)
    
        #画像保存
        cv2.imwrite(OUT_DIR + notface_file,face)

#出力画像ディレクトリにある画像を処理
def Turn_image_face_into_Face():
    face_files = os.listdir("image_face")
    for face_file in face_files:
        #画像を読み込む
        face2 = cv2.imread(OUT_DIR + face_file)
        os.remove(OUT_DIR + face_file)
        #顔認識処理
        gray = cv2.cvtColor(face2, cv2.COLOR_BGR2GRAY)
        cascade_path = BASEDIR + "/haarcascade_frontalface_default.xml"
        cascade = cv2.CascadeClassifier(cascade_path) 
        facerect = cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=4, minSize=(100, 100))
        
        rectangle_color = (0, 0, 255)
    
        if len(facerect) > 0:
            for rect in facerect:
                cv2.rectangle(face2, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), rectangle_color, thickness=2)
    
        #画像保存
        cv2.imwrite(OUT_DIR + face_file,face2)

#入力、出力ディレクトリにある画像数を揃える
def Adjust_the_number_of_files():
    adds_files = os.listdir("image_add")
    face_files = os.listdir("image_face")
    none_exit_in_add_files = [i for i in face_files if not i in adds_files]
    for none_exit_in_add_file in none_exit_in_add_files:
        os.remove(OUT_DIR + none_exit_in_add_file)

if __name__ in '__main__':
    # 処理が終了しないようにスリープを挟んで無限ループ
    while True:
        # 1秒ごとに監視
        time.sleep(1)
        Turn_image_add_into_Face()
        Turn_image_face_into_Face()
        Adjust_the_number_of_files()