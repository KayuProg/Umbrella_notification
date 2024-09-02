#!/usr/bin/env python3

import socket
import gc
import os

import logging

# ログ設定
# logging.basicConfig(
#     filename='/home/kayu/Desktop/weather/main.log',  # ログを記録するファイル名
#     level=logging.INFO,  # 記録するログのレベル（DEBUG, INFO, WARNING, ERROR, CRITICAL）
#     format='%(asctime)s - %(levelname)s - %(message)s',  # ログメッセージのフォーマット
# )

# logging.info("this is run by bash")
#########################################################
# TCP connection
#########################################################

def pico_connect():
    HOST = '192.168.0.12'  # Raspberry PiのIPアドレス
    PORT = 51123           # クライアントと同じポート番号

    # ソケットの設定
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    # try:
    #     sock.bind((HOST, PORT))
    # except Exception as e:
        # logging.info(f"Error binding socket: {e}")
    sock.listen(1)

    # logging.info("waitng for aconnection")
    print('Waiting for a connection...')



    # 接続の確立
    conn, addr = sock.accept()
    print(f'Connected by {addr}')
    # logging.info(f'Connected by {addr}')

    # ソケットを閉じる（通常は無限ループなので到達しません）
    sock.close()



#########################################################
# Reading aloud cythonで読み上げは遅い
#########################################################

################# Japanese ###################
def read_aloud():
    # logging.info("trying to read aloud")
    os.system("/usr/bin/mplayer -speed 1.1 -af scaletempo /home/kayu/Desktop/weather/audio/readaloud.mp3")
    # logging.info("read aloud end")
# ################# English ###################
# english='Japan\'s Health Ministry updated its Q&A page. You can find answers to such questions as how you can avoid catching/spreading the virus, what is the "cough etiquette". '
# tts = gTTS(english, lang='en')
# tts.save("./audio/english.mp3")
# os.system("mplayer ./audio/english.mp3")


################# mei ###################
# import subprocess

# # textfile
# TEXT_FILE = "a.txt"

# # openjtalk
# X_DIC = '/var/lib/mecab/dic/open-jtalk/naist-jdic'
# # M_VOICE = '/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice'
# # M_VOICE = '/usr/share/hts-voice/htsvoice-tohoku-f01-master/htsvoice-tohoku-f01-master/tohoku-f01-angry.htsvoice'# neutral happy angry sad 
# M_VOICE = '/usr/share/hts-voice/mei/mei_normal.htsvoice' # angry happy sad bashful normal
# R_SPEED = '1.0'
# OW_WAVFILE = '/tmp/tmp.wav'

# # aplay
# # CARD_NO = 1
# # DEVICE_NO = 0

# def talk_text(t):
#     open_jtalk = ['open_jtalk']
#     xdic = ['-x', X_DIC]
#     mvoice = ['-m', M_VOICE]
#     rspeed = ['-r', R_SPEED]
#     owoutwav = ['-ow',OW_WAVFILE]
#     cmd = open_jtalk + xdic + mvoice + rspeed + owoutwav
#     c = subprocess.Popen(cmd, stdin=subprocess.PIPE)
#     c.stdin.write(t.encode('utf-8'))
#     c.stdin.close()
#     c.wait()
# #   aplay = ['aplay', '-q', OW_WAVFILE, ('-Dplughw:'+str(CARD_NO)+','+str(DEVICE_NO))]
#     aplay = ['aplay', '-q', OW_WAVFILE]
#     wr = subprocess.Popen(aplay)
#     wr.wait()

# def main():
#     with open(TEXT_FILE) as f:
#         for line in f:
#             talk_text("今日ははれ")

# if __name__ == '__main__':
#     main()


#################################
# 実行
#################################
import schedule
import time
from datetime import datetime




def task2():#接続を待って読み上げまで
    pico_connect()
    # logging.info("connect successful")
    read_aloud()
    gc.collect()#ガベージコレクションの強制実行



while True:
    # logging.info("task2 start")
    task2()
    # logging.info("task2 end\n")
    # if datetime.now().hour==3:
    #     break#毎朝3時でmain.py終了
     

gc.collect()#ガベージコレクションの強制実行
