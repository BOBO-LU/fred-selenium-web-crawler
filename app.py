"""參考資料
https://pythonspot.com/selenium-click-button/ selenium按鈕典籍
https://medium.com/@Epicure1709/使用python的selenium時遇到的一些小問題-7fb5de198ff7  
https://www.itread01.com/content/1542826684.html Python3+Selenium爬取動態網頁資料
https://blog.csdn.net/zwq912318834/article/details/78933910 selenium+python配置chrome浏览器的选项
https://blog.csdn.net/caibaoH/article/details/78335094 存檔路徑 unicode escape
http://python-learnnotebook.blogspot.com/2018/10/chrome-headless.html headless 瀏覽器教學
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 

from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup


import time
import csv
import os

weburl = "https://fred.stlouisfed.org/series/W520RC1A027NBEA" #放網址的地方 如果是檔案就這樣寫"file:web.html"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--window-size=1600,900")
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--disable-infobars")
# options.add_argument("--disable-extensions")
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': r'C:\Users\USER\Desktop\資料\py爬蟲\上課資料\TQC題庫練習\fred動態爬蟲\download'}
#設定下載路徑
options.add_experimental_option('prefs', prefs)
# options.binary_location = "/usr/bin/chromium"

driver = webdriver.Chrome(executable_path='./chromedriver' ,options=options)
try:
    driver.get(weburl)
except Exception as e:
    print(e)
# click download button
download_button = driver.find_elements_by_xpath('//*[@id="download-button"]')[0]
time.sleep(7)
print("before clicked")

download_button.click()
time.sleep(4)
# html = driver.page_source
# html = driver.execute_script("return document.documentElement.outerHTML")
# html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")

# f = open('fred.html', "w", encoding = 'utf-8-sig', newline = "")
# f.write(html)


# bsObj = BeautifulSoup(html, "html.parser")

# os.makedirs('./download/', exist_ok = True) #建立目錄存放檔案

# for download_url in bsObj.find('div',id = "download-button-container").findAll('li'):
driver.find_element_by_xpath('//*[@id="download-data-csv"]').click()

    
    
print(driver.find_element_by_xpath('//*[@id="download-data-csv"]'))

# urlretrieve(download_url,'./download/1.csv') #將什麼檔案存放到什麼位置			
time.sleep(3)
driver.quit()
print("finish")