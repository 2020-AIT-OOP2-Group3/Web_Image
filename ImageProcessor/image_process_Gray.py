from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import os
import time
import sys
import cv2

# スクリプト実行用ディレクトリを絶対パスで指定する
BASEDIR = os.path.abspath(os.path.dirname(__file__))
OUT_DIR = "image_gray/"

# FileSystemEventHandler の継承クラスを作成
class ChangeHandler(FileSystemEventHandler):

    # ファイル変更時のイベント
    def on_modified(self, event):
        # 対象ファイル/フォルダのフルパスが取得できる
        filepath = event.src_path
        # ファイル名を取得
        filename = os.path.basename(filepath)
        img = cv2.imread(filepath)
        #グレースケール化
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        cv2.imwrite(OUT_DIR + filename,gray)

    # ファイル変更時のイベント
    def on_created(self, event):
        # 対象ファイル/フォルダのフルパスが取得できる
        filepath = event.src_path
        # ファイル名を取得
        filename = os.path.basename(filepath)
        img = cv2.imread(filepath)
        #グレースケール化
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        cv2.imwrite(OUT_DIR + filename,gray)

if __name__ in '__main__':
    while 1:
        # ファイル監視の開始
        event_handler = ChangeHandler()
        observer = Observer()
        # パスの監視をスケジュールし、ファイルシステムイベントに応答して、指定されたイベントハンドラーで指定された適切なメソッドを呼び出す
        # recursive　→　再帰的にトラバースされたサブディレクトリに対してイベントが発行される場合はTrue。それ以外の場合はFalse。
        observer.schedule(event_handler, BASEDIR + "/image_add", recursive=False)
        # 監視の実行
        observer.start()
        try:
            # 処理が終了しないようにスリープを挟んで無限ループ
            while True:
                # 1秒ごとに監視
                time.sleep(1)
        # 無限ループからキー入力で監視をやめる
        except KeyboardInterrupt:
            observer.stop()
        # observer.stop()だけでは裏で動くスレッドは停止してないので、完全に停止するまで待つためにjoin()を呼んでいる。
        observer.join()