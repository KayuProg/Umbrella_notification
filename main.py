import socket
import gc


#########################################################
# Scraping
#########################################################











#########################################################
# TCP connection
#########################################################

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
# Reading aloud
#########################################################

#mei
import subprocess

# textfile
TEXT_FILE = "a.txt"

# openjtalk
X_DIC = '/var/lib/mecab/dic/open-jtalk/naist-jdic'
# M_VOICE = '/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice'
# M_VOICE = '/usr/share/hts-voice/htsvoice-tohoku-f01-master/htsvoice-tohoku-f01-master/tohoku-f01-angry.htsvoice'# neutral happy angry sad 
M_VOICE = '/usr/share/hts-voice/mei/mei_normal.htsvoice' # angry happy sad bashful normal
R_SPEED = '1.0'
OW_WAVFILE = '/tmp/tmp.wav'

# aplay
# CARD_NO = 1
# DEVICE_NO = 0

def talk_text(t):
    open_jtalk = ['open_jtalk']
    xdic = ['-x', X_DIC]
    mvoice = ['-m', M_VOICE]
    rspeed = ['-r', R_SPEED]
    owoutwav = ['-ow',OW_WAVFILE]
    cmd = open_jtalk + xdic + mvoice + rspeed + owoutwav
    c = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    c.stdin.write(t.encode('utf-8'))
    c.stdin.close()
    c.wait()
#   aplay = ['aplay', '-q', OW_WAVFILE, ('-Dplughw:'+str(CARD_NO)+','+str(DEVICE_NO))]
    aplay = ['aplay', '-q', OW_WAVFILE]
    wr = subprocess.Popen(aplay)
    wr.wait()

def main():
    with open(TEXT_FILE) as f:
        for line in f:
            talk_text("今日ははれ")

if __name__ == '__main__':
    main()


gc.collect()#ガベージコレクションの強制実行