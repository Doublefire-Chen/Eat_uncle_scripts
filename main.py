#!/usr/bin/python
#coding=utf-8
import webbrowser
import time
import os
from selenium import webdriver
import selenium.webdriver.support.ui as ui
browser = webdriver.Chrome() #指定浏览器
browser.get("https://deyi233.github.io/EatRui/index.html") #打开游戏网页
time.sleep(2) #等待网站打开
num=4 #初始方块
id=1 #每40个方块后会更改id
browser.find_element_by_id("ready-btn").click() #点击开始游戏
def read(num,id): #读取元素id的函数
    num_str="GameLayer"+str(id)+"-"+str(num)
    return browser.find_element_by_id(num_str).get_attribute("class")
while num<10000:
    t=0
    for t in range(0,4): #逐个检测方块是否是叔叔
        temp_num=num
        temp_num=temp_num+t
        tem_str=read(temp_num,id)
        if "t" in tem_str: #判断是否为叔叔
            num_str = "GameLayer"+str(id)+"-"+str(temp_num) #组成包含叔叔的元素的id
            browser.find_element_by_id(num_str).click() #点击吃叔叔
            time.sleep(0.0155) #缓冲时间
            break #吃掉一个叔叔后开始下一轮
    num=num+4 #进入下一轮
    if num==40: #更改id
        if id==0:
            id=1
        elif id==1:
            id=2
        elif id==2:
            id=1
        num=0