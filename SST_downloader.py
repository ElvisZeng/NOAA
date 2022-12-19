#! python3.7
#_*_ coding: utf-8, unicode

print(
"""
从NOAA下载Sea Surface Tempreture的PNG图片
@ Time: 2021-10-28
@ Author: Elvis_Zeng
@ File: SST_Downloader.py
@ Version: 0.0.1
"""
)

import requests as rq, pandas as pd, os
from datetime import datetime, timedelta
from time import sleep
from random import randrange


url = 'https://www.ospo.noaa.gov/data/cb/sst/daily/'  #SST url

filelist = os.listdir()
filelist = [i for i in filelist if i[-3:] == 'png']
filelist.sort()
start_date = '{:.8}'.format(filelist[-1])
end_date = datetime.today()-timedelta(1)
dates = [datetime.strftime(x,'%Y%m%d') for x in list(pd.date_range(start=start_date, end=end_date))]

def downloader(rtf):
    img_url = url + rtf[:4] + "/ct5km_sst_v3.1_global_"+ rtf +".png"
    img = rq.get(img_url)
    sleep(randrange(0,3))
    if img.ok == True:
        img_name = str(i) + ".png"
        with open(img_name, 'wb') as f:
            f.write(img.content)
    result = str(img_url+' download='+str(img.ok)+' img_save=True')
    return result

def log(text):
    with open('log.txt','w') as f:
        f.write(text)
    return text
        
for i in dates:
    print(log(downloader(i)))


#results = [downloader()]
#input(results)
"""with open('log.txt','w') as f:
    f.write(str(results))"""
    