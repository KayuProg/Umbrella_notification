from main2 import task1
from datetime import datetime
import time

while True:
    # 現在の「時」を取得
    current_hour = datetime.now().hour
    
    # 偶数時間であれば関数を実行
    if current_hour % 2 == 0:
        task1()
        
        # 次の奇数時間になるまで待機
        while datetime.now().hour == current_hour:
            time.sleep(600)  # 10分待機して再チェック
    else:
        # 偶数時間まで待機
        print("Waiting for the next even hour...")
        time.sleep(600)  # 10分待機して再チェック

    if current_hour==3:#朝3時で一度タスク終了
        break

#毎朝4時にこのファイル実行．

cron側でできるようにする