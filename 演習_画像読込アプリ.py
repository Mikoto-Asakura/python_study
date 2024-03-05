# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 11:15:01 2023

@author: user
"""

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispLabel(newImage):
    #読み込んだ画像をラベルに表示
    imageData=PIL.ImageTk.PhotoImage(newImage)
    lbl.configure(image=imageData)
    lbl.image=imageData
    

def dispPhoto(path):
    newImage = PIL.Image.open(path).resize((200,200))
    
    #imageData = PIL.ImageTk.PhotoImage(newImage)
    #lbl.configure(image=imageData)
    #lbl.image=imageData
    dispLabel(newImage)
    
    txtbox.delete(0,tk.END) #文字の削除
    txtbox.insert(tk.END,path) #パスの挿入
    
def openFile():
    fpath =fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        
#回転させる関数        
def rotatePhoto():
    rpath = txtbox.get() # テキストボックスからファイルパスを取得
    if rpath:
        newImage= PIL.Image.open(rpath).resize((400,300)).rotate(30)
        
        #読み込んだ画像をラベルに表示
        #imageData=PIL.ImageTk.PhotoImage(newImage)
        #lbl.configure(image=imageData)
        #lbl.image=imageData
        dispLabel(newImage)
       
def convphoto():
    cpath = txtbox.get()
    if cpath:
        newImage= PIL.Image.open(cpath).resize((100,100)).convert("L")
        
        #imageData=PIL.ImageTk.PhotoImage(newImage)
        #lbl.configure(image=imageData)
        #lbl.image=imageData
        dispLabel(newImage)
        

root=tk.Tk()
root.title("画像読込アプリ")
root.geometry("500x450")

txtbox = tk.Entry()

btn1 = tk.Button(text="ファイルを開く",command=openFile)
btn2 = tk.Button(text="画像を変更する",command=openFile)
btn3 = tk.Button(text="回転",command=rotatePhoto)
btn4 = tk.Button(text="白黒",command=convphoto)

lbl  = tk.Label()

btn1.pack()
txtbox.pack()
btn2.place(x=150,y=50)
btn3.place(x=250,y=50)
btn4.place(x=300,y=50)
lbl.place(x=200,y=100)

tk.mainloop()