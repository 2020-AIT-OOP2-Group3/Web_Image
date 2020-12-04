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

        image_process_Kao(addfile_name)

def image_process_Kao(file_name):
    cascade_path = "/Users/k19044kk/Documents/GitHub/Web_Image/ImageProcessor/haarcascade_frontalface_default.xml"
    face_img = cv2.imread(file_name) 
    gry_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
    
    cascade = cv2.CascadeClassifier(cascade_path) 
    facerect = cascade.detectMultiScale(gry_img, scaleFactor=1.05, minNeighbors=4, minSize=(100, 100))
    
    rectangle_color = (0, 0, 255)
    
    if len(facerect) > 0:
        for rect in facerect:
            cv2.rectangle(face_img, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), rectangle_color, thickness=2)

    cv2.imwrite('/Users/k19044kk/Documents/GitHub/Web_Image/ImageProcessor/image_face/face_img.png',face_img)
    

observer = Observer()
# 監視するフォルダを第２引数に指定
observer.schedule(ChangeHandler(), '/Users/k19044kk/Documents/GitHub/Web_Image/ImageProcessor/image_add', recursive=True)
# 監視を開始する
observer.start()

while True:
    time.sleep(5)