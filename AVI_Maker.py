#! python3.7
#_*_ coding: utf-8, unicode
print(
"""
用来把多张图像转化成avi，需要把图像和本文件放在同一个文件夹下
@ Time: 2021-10-28
@ Author: Elvis_Zeng
@ File: mp4_maker.py
@ Version: 0.0.1
"""
)

from cv2 import cv2
import os
os.chdir = os.getcwd()

def mp4_maker():
    fps = 7
    filetype = ".png"
    size = (1787, 1085)
    dir = os.listdir()
    files = [i for i in dir if i.endswith(filetype)]
    avi = cv2.VideoWriter("Result.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), int(fps), size)    
    for i in files:
       img = cv2.imread(i)
       avi.write(img)
    avi.release()
    cv2.destroyAllWindows()
    input("AVI视频制作完成！\nFPS={} \n分辨率={}*{}\n按Enter退出".format(fps,size[0],size[1]))

mp4_maker()