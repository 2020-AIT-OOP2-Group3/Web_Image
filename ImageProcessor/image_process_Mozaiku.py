import cv2

def image_process_Mozaiku():
    cascade_path = "/Users/k19100kk/Documents/GitHub/Web_Image/ImageProcessor/haarcascade_frontalface_default.xml"

    mozaiku_img = cv2.imread('/Users/k19100kk/Documents/GitHub/Web_Image/ImageProcessor/uchitane_far.png') 
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
    

if __name__ == "__main__":
    image_process_Mozaiku()