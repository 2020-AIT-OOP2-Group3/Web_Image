# Web_Imageでの役割分担
## 今回やること
 ## 画像処理プログラム側
  - 別プログラムにてアップロードディレクトリを監視し、アップロードされた画像を決められた方法で処理し保存
    - 担当:顔検出して枠で囲う　桑原くん
    - 担当:Cannyフィルタによる輪郭抽出　山口くん
    - 担当:画像のグレースケール化　森永さん
  - ファイル名
    - image_process_Gray.py...グレースケール化
    - image_process_Canny.py...Cannyフィルタを使用した
    - image_process_Kao.py...顔認識し囲う
    - image_process_Mozaiku.py...顔にモザイク
 ## Web側
  - ユーザーがWebページより画像をアップロードできる
    - 担当：（1人）　志村くん
  - ファイル名
    - web.py
  - ユーザーはアップロードされた画像と処理済みの画像をいつでもWebページ経由で閲覧できる
    - 担当：（1人）　篠原くん
  - ファイル名
    - index.html
    - ****.css
 ## コメント欄
  ### WacthDogのドキュメント
  1. [公式（英語）](https://pythonhosted.org/watchdog/)
  2. [フォルダの操作方法](https://ailog.site/2020/03/06/0306/)
  ### OpenCV
  1. [公式](http://opencv.jp/opencv-2svn/py/)
  2. [顔検出サイト](https://note.nkmk.me/python-opencv-face-detection-haar-cascade/)
  
# 提出物テンプレート
 ## 第１１回レポート(参考にして下さい）
  ### GitHubアカウント
  | Githubの名前  |
  ### 担当箇所
  - コメント文
  ### チーム作業のログ (git --no-pager log --graph)
  <pre>
  </pre>
  ### 感想
  - コメント文
