from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import cv2
import time
import numpy as np

class ChangeHandler(FileSystemEventHandler):

    def on_created(self, event):
        addfile_name=str(event)
        addfile_name=addfile_name.replace('<FileCreatedEvent: src_path=','')
        addfile_name=addfile_name.replace(">",'')
        addfile_name=addfile_name.replace("'",'')
        addfile_name=addfile_name.replace("'",'')

        image_process_Canny(addfile_name)

def image_process_Canny(file_name): #  引数として画像を追加する
    cascade_path = "/Users/k19100kk/Documents/GitHub/Web_Image/ImageProcessor/haarcascade_frontalface_default.xml"
    org_img = cv2.imread(file_name) # 追加した引数で読み込む
    # print(org_img)  #  ファイル読み込みの確認用

    edge_img = cv2.Canny(org_img,100,200) #  Canny法で加工した画像を保存
    cv2.imwrite('/Users/k19100kk/Documents/GitHub/Web_Image/ImageProcessor/image_face/face_img.png',edge_img)

observer = Observer()
# 監視するフォルダを第２引数に指定
observer.schedule(ChangeHandler(), '/Users/k19100kk/Documents/GitHub/Web_Image/ImageProcessor/image_add', recursive=True)
# 監視を開始する
observer.start()

while True:
    time.sleep(5)