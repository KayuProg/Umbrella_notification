import socket
import gc


#########################################################
# Scraping cython使ってますがあまり早くなってません．
#########################################################
import scraping 

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

################# 音声ファイル作成 #######################
import os
from gtts import gTTS
japanese=text_full
tts = gTTS(japanese, lang='ja')
tts.save("./audio/readaloud.mp3")
gc.collect()#ガベージコレクションの強制実行

#########################################################
# Reading aloud cythonで読み上げは遅い
#########################################################

################# Japanese ###################
os.system("mplayer -speed 1.4 -af scaletempo ./audio/readaloud.mp3")

# ################# English ###################
# english='Japan\'s Health Ministry updated its Q&A page. You can find answers to such questions as how you can avoid catching/spreading the virus, what is the "cough etiquette". '
# tts = gTTS(english, lang='en')
# tts.save("./audio/english.mp3")
# os.system("mplayer ./audio/english.mp3")



gc.collect()#ガベージコレクションの強制実行