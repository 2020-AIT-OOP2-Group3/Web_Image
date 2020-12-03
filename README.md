# Web_Imageでの役割分担
## 今回やること
 ## 画像処理プログラム側
  1. 別プログラムにてアップロードディレクトリを監視し、アップロードされた画像を決められた方法で処理し保存
   ・ 担当:顔検出して枠で囲う　桑原くん
   ・ 担当:Cannyフィルタによる輪郭抽出　山口くん
   ・ 担当:画像のグレースケール化　森永さん
 ## Web側
  1. ユーザーがWebページより画像をアップロードできる
   ・ 担当：（1人）　志村くん
  2. ユーザーはアップロードされた画像と処理済みの画像をいつでもWebページ経由で閲覧できる
   ・ 担当：（1人）　篠原くん
 ## コメント欄
  ### WacthDogのドキュメント
  1. [公式（英語）](https://pythonhosted.org/watchdog/)
  2. [フォルダの操作方法](https://ailog.site/2020/03/06/0306/)
  ### OpenCV
  1. [公式](http://opencv.jp/opencv-2svn/py/)
  2. [顔検出サイト](https://note.nkmk.me/python-opencv-face-detection-haar-cascade/)
