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



gc.collect()#ガベージコレクションの強制実行