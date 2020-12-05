from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import cv2
import time

class ChangeHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        addfile_name=str(event)
        addfile_name=addfile_name.replace('<FileCreatedEvent: src_path=','')
        addfile_name=addfile_name.replace(">",'')
        addfile_name=addfile_name.replace("'",'')
        addfile_name=addfile_name.replace("'",'')

        image_process_Mozaiku(addfile_name)

def image_process_Mozaiku(file_name):
    cascade_path = "/Users/k19100kk/Documents/GitHub/Web_Image/ImageProcessor/haarcascade_frontalface_default.xml"

    mozaiku_img = cv2.imread(file_name) 
    gry_img = cv2.cvtColor(mozaiku_img,cv2.COLOR_BGR2GRAY)

    cascade = cv2.CascadeClassifier(cascade_path)
    faces = cascade.detectMultiScale(gry_img, scaleFactor=1.05, minNeighbors=4, minSize=(100, 100))

    if len(faces) > 0:
        for face in faces:
            x, y, w, h = face
            roi = mozaiku_img[y:y+h, x:x+w]
            roi = cv2.resize(roi, (w//10, h//10))
            roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_NEAREST)
            mozaiku_img[y:y+h, x:x+w] = roi               

    cv2.imwrite('/Users/k19100kk/Documents/GitHub/Web_Image/ImageProcessor/image_mozaiku/mozaiku_img.png',mozaiku_img)
    
observer = Observer()
# 監視するフォルダを第２引数に指定
observer.schedule(ChangeHandler(), '/Users/k19100kk/Documents/GitHub/Web_Image/ImageProcessor/image_add', recursive=True)
# 監視を開始する
observer.start()

while True:
    time.sleep(5)