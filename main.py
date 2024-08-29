import socket
import gc


#########################################################
# Scraping cython使ってますがあまり早くなってません．
#########################################################
import scraping 

def make_text():
    result=scraping.scrape()

    text_time=[]
    text_umb=None

    if (result['yowa']!=None or result['ame']!=None or result['tuyo']!=None or result['gou']!=None):
        text_umb="今日は傘を持っていきましょう．"
    elif result['ko']!=None and (result['yowa']==None and result['ame']==None and result['tuyo']==None and result['gou']==None):
        text_umb="今日は折り畳み傘を持っていきましょう．"
    elif not any(result):
        text_umb="今日は傘を持って行かなくて大丈夫です．"

    keys=list(result.keys())

    for key in keys:
        if result[key]!=None:
            if key=='ko':
                time=str(result['ko'])+"時から小雨．"
            elif key=='yowa':
                time=str(result['yowa'])+"時から弱雨．"
            elif key=='ame':
                time=str(result['ame'])+"時から雨．"
            elif key=='tuyo':
                time=str(result['tuyo'])+"時から強雨．"
            elif key=='gou':
                time=str(result['gou'])+"時から豪雨．"

            text_time.append(time)

    text_full=text_umb+''.join(text_time)+"です．"
    return text_full

################# 音声ファイル作成 #######################
import os
from gtts import gTTS

def make_audio(text):
    japanese=text
    tts = gTTS(japanese, lang='ja')
    tts.save("./audio/readaloud.mp3")



#########################################################
# TCP connection
#########################################################

def pico_connect():
    HOST = '192.168.0.12'  # Raspberry PiのIPアドレス
    PORT = 51000           # クライアントと同じポート番号


    # ソケットの設定
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(1)

    print('Waiting for a connection...')



    # 接続の確立
    conn, addr = sock.accept()
    print(f'Connected by {addr}')

    # ソケットを閉じる（通常は無限ループなので到達しません）
    sock.close()



#########################################################
# Reading aloud cythonで読み上げは遅い
#########################################################

################# Japanese ###################
def read_aloud():
    os.system("mplayer -speed 1.4 -af scaletempo ./audio/readaloud.mp3")

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

def task1():#audioの作成まで行う．
     text_full=make_text()
     make_audio(text_full)
     gc.collect()#ガベージコレクションの強制実行


def task2():#接続を待って読み上げまで
    pico_connect()
    read_aloud()
    gc.collect()#ガベージコレクションの強制実行



while True:
    task2()
    if datetime.now().hour==3:
        break#毎朝3時でmain.py終了
     




gc.collect()#ガベージコレクションの強制実行
