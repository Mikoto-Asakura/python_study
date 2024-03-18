# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:39:44 2024

@author: user
"""

import pandas as pd
import folium

df = pd.read_csv("shisetsushakaikyouiku.csv",encoding = "shift-jis")

shisetsu = df[["緯度","経度","名称","住所","電話番号"]].values

m = folium.Map(location=[35.34271845065953, 132.90591108853113],zoom_start=16)
folium.Marker([35.34271845065953, 132.90591108853113]).add_to(m)
m.save("asakurajitaku.html")

for data in shisetsu:
    folium.Marker([data[0],data[1]],tooltip=(data[2],data[3],data[4])).add_to(m)
m.save("shisetsu_lamer.html")