# -*- encoding: UTF-8 -*-
'''
@File    :  main.py
@Time    :  2021/02/27 23:18:17
@Author  :  Kearney
@Contact :  191615342@qq.com
@Desc    :  定时触发脚本
'''
import schedule
import time
import datetime


def job():
    with open('love.txt', 'a') as f:
        f.write(str(datetime.datetime.now()) + '\n')


schedule.every(10).seconds.do(job)
# schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
