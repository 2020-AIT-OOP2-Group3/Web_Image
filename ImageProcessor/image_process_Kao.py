import cv2
import numpy as np

def image_process_Kao():#  引数として画像を追加する
    cascade_path = "/Users/k19100kk/Documents/GitHub/Web_Image/ImageProcessor/haarcascade_frontalface_default.xml"

    result_img = cv2.imread('/Users/k19100kk/Documents/GitHub/Web_Image/ImageProcessor/uchitane_far.png') 
    gry_img = cv2.cvtColor(result_img, cv2.COLOR_BGR2GRAY)
    
    cascade = cv2.CascadeClassifier(cascade_path) 
    facerect = cascade.detectMultiScale(gry_img, scaleFactor=1.05, minNeighbors=4, minSize=(100, 100))
    
    rectangle_color = (0, 0, 255)
    
    if len(facerect) > 0:
        for rect in facerect:
            cv2.rectangle(result_img, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), rectangle_color, thickness=2)

    cv2.namedWindow('result')
    cv2.imshow('result',result_img)
    cv2.waitKey(0)
    cv2.destoloyAllWindows()

if __name__ == "__main__":
    image_process_Kao()