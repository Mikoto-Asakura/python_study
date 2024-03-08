# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 15:21:15 2023

@author: user
"""

import tkinter as tk

def keisan():
    try:
       a=txtbox1.get()
       b=txtbox2.get()
       
       if a.isdigit():　　#数字に変換出来るか
           if b.isdigit():
               ans= int(a) * int(b)
               lbl3.conhigure(text="答えは")
           else:
               print("数字で入力してね")
　　　  　else:
         　print("数字で入力してね")
       
             
    except:
           print("Error！")
       
root = tk.Tk()
root.geometry("500x400")
root.title("かけ算アプリ")

#ラベル
lbl1=tk.Label(text="数字を入力してください")
lbl1.pack()

txtbox1=tk.Entry()
txtbox1.place(x=60,y=100)

txtbox2=tk.Entry()
txtbox2.place(x=300,y=100)

lbl2=tk.Label(text="x")
lbl2.place(x=230,y=100)

lbl3=tk.Label(text="答えは")
lbl3.place(x=230,y=150)

btn=tk.Button(text="計算",command=keisan)
btn.place(x=230,y=200)

tk.mainloop()