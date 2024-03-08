# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 15:33:47 2023

@author: user
"""

import tkinter as tk
import calendar as cl

def pre_month():
    global y
    global m
    
    if m == 1:
        m = 12
        y = y-1
    else:
        m = m-1     
    
    lbl1.configure(text=cl.month(y,m))
    
def add_month():
    global y
    global m
    
    if m == 12:
        m = 1
        y = y+1
    else:
        m = m + 1
        
    lbl1.configure(text=cl.month(y,m))
    

root=tk.Tk()
root.title("カレンダー")
root.geometry("300x200")

y=2023
m=4

#ラベル
lbl1 = tk.Label(text=cl.month(y,m))

#配置
lbl1.pack()

#ボタン
btn1= tk.Button(text="←",command=pre_month)
btn2= tk.Button(text="→",command=add_month)

#配置
btn1.place(x=100,y=150)
btn2.place(x=180,y=150)

#ボタン

tk.mainloop()
