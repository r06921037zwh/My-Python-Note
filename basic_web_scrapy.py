#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 11:07:35 2019

@author: zhewei
"""
#===== 1 =====#
''' play with requests module '''
import requests 
r = requests.get('http://www.flag.com.tw') 

if r.status_code == 200:   
    print(r.text)          
else:
    print(r.status_code, r.reason) 

# get example
url = 'https://httpbin.org/get'
hd = {'user-key': '7ADGS9S'}  # 標頭參數(以字典儲存)
pm = {'id': 1023, 'neme': 'joe'}   # 網址參數(以字典儲存)
r = requests.get(url, headers = hd, params = pm)   # 加入 headers 及 params 參數
print(r.text)   

# post example
url = 'http://httpbin.org/post' # 使用測試服務網站, POST 方法網址要加 /post
r = requests.post(url, data = 'Hello')  # 送出字串資料
print(r.text)
r = requests.post(url, data = {'id':'123', 'name':'Joe'})
print(r.text)



#===== 2 =====#
''' play with beautifulsoup '''
page = """
<html>
  <head><title>Flag Tech</title></head>
  <body>
    <div class="section" id="main">
      <img alt="Flag Figure" src="http://flag.tw/logo.png">
      <p>Product</p>
      <button id="books"><h4 class="bk">Book</h4></button>
      <button id="maker"><h4 class="pk">Creator</h4></button>
      <button id="teach"><h4 class="pk">Tools</h4></button>
    </div>
    <div class="section" id="footer">
      <p>Our Address</p>
      <a href="http://flag.tw/contact">Contact us</a>
    </div>
  </body>
</html>
"""

from bs4 import BeautifulSoup
bs = BeautifulSoup(page, 'lxml')

# method 1
print(bs.title)
print(bs.a)

print(bs.a.text)
print(bs.a.get('href'))
print(bs.a['href'])

# method 2
print(bs.find('h4'))
print(bs.find('h4', {'class': 'pk'}))
print(bs.find('h4').text)

# method 3
print(bs.find_all('h4'))
print(bs.find_all('h4', {'class': 'pk'}))

print(bs.find_all(['title', 'p']))
print(bs.find_all(['title', 'p'])[1].text)

# method 4
print('h4:', bs.select('h4'))         #←查詢所有 h4 標籤
print('#book:', bs.select('#books'))  #←查詢所有 id 為 'books' 的標籤
print('.pk:', bs.select('.pk'))       #←查詢所有 class 為 'pk' 的標籤
print('h4.bk', bs.select('h4.bk'))    #←查詢所有 class 為 'bk' 的 h4 標籤
print(bs.select('#main button .pk'))
print(bs.select('#main button .pk')[1].text)
print(bs.select('#footer a')[0]['href'])
                

#===== 2 =====#
''' play with selenium '''
from selenium import webdriver # 匯入 selenium 的 webdriver
from time import sleep         # 匯入內建 time 模組的 sleep() 函式

browser = webdriver.Chrome()            # 建立 Chrome 瀏覽器物件
browser.get('http://www.google.com')    # 開啟 Chrome 並連到 Google 網站
# browser.forward()                     # next page
# browser.back()                        # previous page
# browser.refresh()                     # refresh the page
print('標題：' + browser.title)         # 輸出網頁標題
print('網址：' + browser.current_url)   # 輸出網頁網址
print('內容：' + browser.page_source[0:50]) # 輸出網頁原始碼的前 50 個字
print('視窗：', browser.get_window_rect())  # 輸出視窗的位置及寬高
browser.save_screenshot('d:/scrcap.png')   # 截取網頁畫面
sleep(3) # 暫停 3 秒
browser.set_window_rect(200, 100, 500, 250)   # 改變視窗位置及大小
sleep(3)
browser.fullscreen_window()     # 將視窗設為全螢幕
sleep(3)
browser.quit() # 關閉視窗結束驅動
# browser.close() # close page


'''operate on particular element on the page'''
browser = webdriver.Chrome() # 建立 Chrome 瀏覽器物件
browser.get('http://www.google.com') # 開啟 Chrome 並連到旗標網站
e1 = browser.find_element_by_tag_name('head')  # 尋找 head 標籤
print(e1.tag_name)  # 輸出 head 確認已找到 (tag_name 屬性為標籤名稱, 詳見下表)
e2 = e1.find_element_by_tag_name('title')  # 在 head 元素中尋找 title 標籤
print(e2.tag_name)  # 輸出 tite 確認已找到
browser.quit()     # 關閉視窗結束驅動


'''auto login in facebook'''
from selenium import webdriver  # 匯入 selenium 的 webdriver

opt =  webdriver.ChromeOptions()      #←建立選項物件
opt.add_experimental_option('prefs',  #←在選項物件中加入「禁止顯示訊息框」的選項
    {'profile.default_content_setting_values': {'notifications' : 2}})
browser = webdriver.Chrome(options = opt)    #←以 options 指名參數來建立瀏覽器物件

browser.get('http://www.facebook.com')    
browser.find_element_by_id('email').send_keys('您的帳號') 
browser.find_element_by_id('pass').send_keys('您的密碼')  
browser.find_element_by_id('loginbutton').click()         


'''auto login in google'''
from selenium import webdriver  # 匯入 selenium 的 webdriver
from time import sleep          # 匯入內建的 time 模組的 sleep() 函式

opt =  webdriver.ChromeOptions()      #建立選項物件
opt.add_experimental_option('prefs',  #加入「禁止顯示訊息框」的選項
    {'profile.default_content_setting_values': {'notifications' : 2}})
browser = webdriver.Chrome(options = opt) #以 options 參數來建立瀏覽器物件

browser.get('http://www.google.com')    #←開啟 Chrome 並連到 Google 網站
browser.maximize_window()  #←將視窗最大化以避免最右邊的登入鈕沒顯示出來

browser.find_element_by_id('gb_70').click()   #←按登入鈕
sleep(3)       #←暫停 3 秒等待進入下一頁
browser.find_element_by_id('identifierId').send_keys('您的帳號') #}←輸入帳號
browser.find_element_by_id('identifierNext').click()   #←按繼續鈕
sleep(3)       #←暫停 3 秒等待進入下一頁
browser.find_element_by_name('password').send_keys('您的密碼')  #←輸入帳密
browser.find_element_by_id('passwordNext').click()   #←按繼續鈕
