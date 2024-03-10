# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:46:42 2023

@author: user
"""
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk
import sklearn.datasets
import sklearn.svm
import numpy

def imageToData(filename):
    #画像を８ｘ８のグレースケールに変換
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8,8),PIL.Image.Resampling.LANCZOS)
    
    #画像をラベルに表示
    #dispImage = PIL.ImageTk.photoImage(grayImage)
    dispImage = PIL.ImageTk.PhotoImage(grayImage.resize((300,300)))
    imageLabel.configure(image = dispImage)
    imageLabel.image = dispImage
    
    #数値リストに変換する処理の追加
    numImage = numpy.asarray(grayImage,dtype = float)
    numImage = numpy.floor(16-16*(numImage / 256))
    numImage = numImage.flatten()
    
    return numImage

#　数字を予測する関数
def predictDigits(data):
    #学習用データを読み込む
    digits = sklearn.datasets.load_digits()
    
    #機械学習を行う
    clf = sklearn.svm.SVC(gamma = 0.001)
    clf.fit(digits.data,digits.target)
    
    #予測結果を表示する
    n = clf.predict([data])  #予測
    textLabel.configure(text = "この画像は" + str(n) + "です！")
    
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        #画像ファイルを数値リストに変換する
        data = imageToData(fpath)
        #数字予測関数predictDigitsへデータを渡して、数字を予測
        predictDigits(data)

root = tk.Tk()
root.geometry("400x400")

btn = tk.Button(root,text="ファイルを開く",command=openFile)
imageLabel = tk.Label()

btn.pack()
imageLabel.pack()

#予測結果を表示するラベル
textLabel = tk.Label(text="手書きの数字を認識します！")
textLabel.pack()

tk.mainloop()
