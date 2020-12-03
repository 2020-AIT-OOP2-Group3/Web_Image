import cv2
import numpy as np

def image_process_Canny(): #  引数として画像を追加する
    org_img = cv2.imread('/Users/k19109kk/src/Git/Web_Image/ImageProcessor/uchitane_far.png') #  追加した引数で読み込む
    # print(org_img)  #  ファイル読み込みの確認用

    edge_img = cv2.Canny(org_img,100,200) #  Canny法で加工した画像を保存

    cv2.namedWindow('org')
    cv2.namedWindow('edge')

    cv2.imshow('org', org_img)
    cv2.imshow('edge', edge_img)

    cv2.waitKey(0)
    cv2.destoloyAllWindows()

    

if __name__ == "__main__":
    image_process_Canny()