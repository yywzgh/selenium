#!/usr/bin/python
# -*-coding:utf-8-*-

import re, os
import json
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


binary_location = '/usr/bin/google-chrome'
chrome_driver_binary = '/usr/bin/chromedriver'

chrome_options = Options()
chrome_options.binary_location = binary_location
chrome_options.add_argument("start-maximized")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument("--remote-debugging-port=9222")

#chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

chrome_options.add_experimental_option("useAutomationExtension", False)

#chromedriver = chrome_driver_binary

#os.environ["webdriver.chrome.driver"] = chromedriver


#BROWSER = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)

BROWSER = webdriver.Chrome(chrome_options=chrome_options)

#WAIT = WebDriverWait(BROWSER, 5)

BROWSER.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})",})

BROWSER.get("https://console.cloud.tmall.com")

print "打开聚石塔登录页面"

#BROWSER.maximize_window()

BROWSER.find_element_by_partial_link_text("使用淘宝账号登录").click()

print "使用淘宝账号登录"

BROWSER.find_element_by_name("fm-login-id").send_keys(u'测试账号')

print "输入用户名"

BROWSER.find_element_by_name("fm-login-password").send_keys("测试密码")

print "输入密码"

#driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()

#source = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')

time.sleep(1)

# 登录
BROWSER.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()

print "登录"

time.sleep(5)

# 转到应用列表

print "跳转到应用列表"

BROWSER.find_element_by_xpath('//*[@id="App"]/div/div/div/div[2]/div[5]/div[1]/div/div/div[2]/div/div/div[2]/div/div').click()

time.sleep(5)

# 转到所有应用

#print "选择所有应用"

#BROWSER.find_element_by_xpath('//*[@id="App"]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div/ul/li[2]/div').click()

# 操作发布

print "正在跳转到发布页面"

print BROWSER.current_url

#print BROWSER.page_source

# BROWSER.find_element_by_xpath('//*[@id="App"]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr/td[8]/div/div/button[2]/span').click()

#BROWSER.find_element_by_xpath('//*[@id="App"]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr/td[8]/div/div/button[2]/span').click()

#BROWSER.find_element_by_xpath('//*[@id="App"]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[8]/div/div/button[2]/span').click()

#BROWSER.find_elements_by_partial_link_text("发布")[0].click()
BROWSER.get("https://console.cloud.tmall.com/#/app/deploy/13187/2?statusKey=progress")

print "正在新建发布单"

time.sleep(5)

#num = BROWSER.window_handles

#BROWSER.switch_to.window(num[1])

BROWSER.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/button/span').click()

print "正在输入发布单名称"

time.sleep(1)

# 发布单名称
release_name = "JS-" + time.strftime("%Y%m%d%H%M")

BROWSER.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/span/div[1]/div[2]/span/input').send_keys(release_name)



BROWSER.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/span/div[2]/div[2]/div/span/input').send_keys("/JC/jc-api-web.jar")

print "正在上传Jar包"

time.sleep(60)


print "正在提交发布单"

time.sleep(5)

print "发布完成"

BROWSER.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/span/button[1]').click()

time.sleep(5)

BROWSER.quit()

