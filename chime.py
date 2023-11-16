import schedule
import time
import datetime
import pygame

# MP3を再生する関数
def play_mp3(file_path):
    pygame.init()
    try:
        # MP3ファイルの読み込みと再生
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # 再生中は待機
        while pygame.mixer.music.get_busy():
            continue
    except pygame.error as e:
        print("Error occurred: ", e)
    finally:
        # Pygameの終了
        pygame.mixer.quit()

# 12時に再生する関数
def play_1():
    file_path = "./1200.mp3"  # 12時に再生する曲のパス
    print("設定した時刻(12:00)になりました。",file_path,"を再生します。")
    play_mp3(file_path)
    print("再生を終了しました。")

# 17時に再生する関数
def play_2():
    file_path = "./1700.mp3"  # 17時に再生する曲のパス
    print("設定した時刻(17:00)になりました。",file_path,"を再生します。")
    play_mp3(file_path)
    print("再生を終了しました。")

# 18時に再生する関数
def play_3():
    file_path = "./1800.mp3"  # 18時に再生する曲のパス
    print("設定した時刻(18:00)になりました。",file_path,"を再生します。")
    play_mp3(file_path)
    print("再生を終了しました。")

# スケジュールに再生する時間を設定
schedule.every().day.at("12:00").do(play_1)  # 毎日12時にplay_1を実行
schedule.every().day.at("17:00").do(play_2)  # 毎日17時にplay_2を実行
schedule.every().day.at("18:00").do(play_3)  # 毎日18時にplay_3を実行

# 定期的にスケジュールをチェックし、再生する
while True:
    schedule.run_pending()
    time.sleep(1)
