import socket
import gc
import time
from datetime import datetime
################# 音声ファイル作成 #######################
import os
from gtts import gTTS

def make_audio(text):
    japanese=text
    tts = gTTS(japanese, lang='ja')
    tts.save("/home/kayu/Desktop/weather/audio/readaloud.mp3")
    print("making audio finish")

#########################################################
# Scraping cython使ってますがあまり早くなってません．
#########################################################
import scraping 

def make_text():
    result=scraping.scrape()
    print("scraping finish")

    text_time=[]
    text_umb=None

    if (result['yowa']!=None or result['ame']!=None or result['tuyo']!=None or result['gou']!=None):
        text_umb="今日は傘を持っていきましょう．"
    elif result['ko']!=None and (result['yowa']==None and result['ame']==None and result['tuyo']==None and result['gou']==None):
        text_umb="今日は折り畳み傘を持っていきましょう．"
    elif not any(result):
        text_umb="今日は傘を持って行かなくて大丈夫です．"

    keys=list(result.keys())

    now_hour=int(datetime.now().hour)
    for key in keys:
        if result[key]!=None:
            #現在以降の天気を反映させる
            if key=='ko':
                if  result['ko']>=now_hour:
                    time=str(result['ko'])+"時から小雨．"
            elif key=='yowa':
                if  result['yowa']>=now_hour:                
                    time=str(result['yowa'])+"時から弱雨．"
            elif key=='ame':
                if  result['ame']>=now_hour:
                    time=str(result['ame'])+"時から雨．"
            elif key=='tuyo':
                if  result['tuyo']>=now_hour:
                    time=str(result['tuyo'])+"時から強い雨．"
            elif key=='gou':
                if  result['gou']>=now_hour:
                    time=str(result['gou'])+"時から豪雨．"

            text_time.append(time)
    
    if text_umb==None:
        text_full=("今日は傘を持っていく必要はありません．")
    else:
        text_full=text_umb+''.join(text_time)+"です．"
    print("text making finish")
    return text_full


def task1():#audioの作成まで行う．
     text_full=make_text()
     make_audio(text_full)
     gc.collect()#ガベージコレクションの強制実行