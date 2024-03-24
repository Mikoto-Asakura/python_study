# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 22:04:47 2024

@author: user
"""

import requests
import json
from datetime import datetime,timedelta,timezone
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'Noto Sans CJK JP']

url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Naha,jp",key="82f17bb6ab2cd1d011a1ec986aa4fd66")

#データを整形して読み込む
data = requests.get(url).json()

#空の表データを作成
df = pd.DataFrame(columns=["気温"])

#日本標準時へ変換
tz = timezone(timedelta(hours=+9),"JST")

for dat in data["list"]:  #　読み込んだデータのlistに紐づくデータ
    #読み込んだリストの中のタイムスタンプ
    jst = datetime.fromtimestamp(dat["dt"],tz)
    jst = str(jst)[:-9]
    
    #dt_txt = dat["dt_txt"]
    temp = dat["main"]["temp"]
    # インデックスを設定して気温を入れる
    df.loc[jst] = temp
  
# 折れ線グラフ
df.plot(figsize=(15,8))
#　気温の最小値、最大値を決める
plt.ylim(-10,40)
#　目盛り線を表示させる
plt.grid()
plt.show()