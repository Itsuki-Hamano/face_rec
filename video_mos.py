# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 21:22:02 2019

@author: IstukiHamano
"""

#動画ファイル内の顔を検出し、モザイク加工した動画ファイル書き出し

import cv2
 
#画像パスから入力
cap = cv2.VideoCapture('sample1.mp4')
 

#動画の保存
output_width=int(cap.get(3))
output_height=int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
video = cv2.VideoWriter('output_video.mp4', fourcc, 20.0, (int(cap.get(3)*0.5),int(cap.get(4)*0.5)))
#解像度が元画像に近いほど精度良い
#video = cv2.VideoWriter('output_video.mp4', fourcc, 20.0, (int(cap.get(3)),int(cap.get(4))))


# opencvの顔検出重みファイル読み込み
face_cascade_file = "haarcascade_frontalface_alt.xml"
face_cascade = cv2.CascadeClassifier(face_cascade_file)
 
#モザイクを作る関数
def mosaic(img, rect, size):
    (x1, y1, x2, y2) = rect
    w = x2 - x1
    h = y2 - y1
    i_rect = img[y1:y2, x1:x2]
 
    i_small = cv2.resize(i_rect, (size, size))
    i_mos = cv2.resize(i_small, (w, h), interpolation=cv2.INTER_AREA)
 
    img2 = img.copy()
    img2[y1:y2, x1:x2] = i_mos
    return img2
 
#画像で保存したいときに、画像ファイル名用ループ変数
i=0
while True:
    #画像を取得
    ret,frame = cap.read()
    if ret:
        #元画像の解像度で動画を出力するときにはリサイズいらない
        #処理を軽くするために解像度を圧縮
        frame=cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #faces = face_cascade.detectMultiScale(gray, 1.5, 3)
        faces = face_cascade.detectMultiScale(frame, 1.5, 3)
 
        for (x, y, w, h) in faces:
            frame = mosaic(frame, (x, y, x+w, y+h), 10)
        #保存
        video.write(frame)
        #画像にして保存
        #cv2.imwrite('img'+str(i)+'.jpg', img)
        i+=1
    else:
        break

#リソースの解放
video.release()
cap.release()