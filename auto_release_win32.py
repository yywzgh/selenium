from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time
import datetime
import os
import sys

# 获取环境信息 prod生产环境
release_env = sys.argv[1]

exec_start = datetime.datetime.now()

result = os.system("D:\\JC-Release.bat")

#print(result)

time.sleep(3)

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})",})

#driver = webdriver.Chrome()

driver.get("https://console.cloud.tmall.com")

#driver.find_elements_by_class_name("vc-link link_k7n3pr4s").click

#driver.maximize_window()

time.sleep(1)

driver.find_element_by_partial_link_text("使用淘宝账号登录").click()

driver.find_element_by_name("fm-login-id").send_keys("阿里云计算")

driver.find_element_by_name("fm-login-password").send_keys("00000000")

#driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()

#source = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')

time.sleep(1)

# 验证码滑条
# source = driver.find_element_by_id("nc_1_n1z")
# ActionChains(driver).drag_and_drop_by_offset(source, 300, 0).perform()

# 登录
driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()

time.sleep(3)

# 转到应用列表
#driver.find_element_by_xpath('//*[@id="App"]/div/div/div/div[2]/div[5]/div[1]/div/div/div[2]/div/div/div[2]/div/div').click()

# 转到所有应用
# driver.find_element_by_xpath('//*[@id="App"]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div/ul/li[2]/div').click()

# 操作发布
#driver.find_element_by_xpath('//*[@id="App"]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[8]/div/div/button[2]/span').click()

#num = driver.window_handles

#driver.switch_to.window(num[1])

# 直接跳转到发布页面
print("正在跳转到发布页面")

if release_env == "prod":
    #正式环境
    driver.get("https://console.cloud.tmall.com/#/app/deploy/13187/2?statusKey=progress&envId=9256")
else:
    #预发环境
    driver.get("https://console.cloud.tmall.com/#/app/deploy/13187/2?statusKey=progress")

time.sleep(3)

# 打开新建发布单
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/button/span').click()

time.sleep(1)

# 发布单名称
release_name = "JS-" + time.strftime("%Y%m%d%H%M")

driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/span/div[1]/div[2]/span/input').send_keys(release_name)

#打开上传窗口
# driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/span/div[2]/div[2]/div/span/div').click()

time.sleep(1)

# os.system("D:\\upload.exe")

driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/span/div[2]/div[2]/div/span/input').send_keys("D:\\git\\jc-front-api\\jc-api-web\\target\\jc-api-web.jar")

time.sleep(1)

upload = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/span/div[2]/div[2]/div/div/div').get_attribute("class")

time.sleep(3)

print("正在上传Jar包")

while True:
    upload_flag = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/span/div[2]/div[2]/div/div/div').get_attribute("class")
    if "done" in upload_flag:
        print('-')
        break
    else:
        time.sleep(1)
        print('-', end='')

print("上传完成")

time.sleep(1)

#提交发布单
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/span/button[1]').click()

time.sleep(3)

driver.quit()

exec_end = datetime.datetime.now()

print("耗时：", exec_end - exec_start)

#driver.get("https://console.cloud.tmall.com/#/app/deploy/13187/2?statusKey=progress")

#driver.
#action = ActionChains(driver)
#action.click_and_hold(source).perform()
#action.reset_actions()
#action.move_by_offset(200, 0).perform()  # 移动滑块

#while True:
#    try:
   #定位滑块元素
        #source = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")
   #定义鼠标拖放动作
        #driver.drag_and_drop_by_offset(source,400,0).perform()
        #等待JS认证运行,如果不等待容易报错
   #     sleep(2)
        #查看是否认证成功，获取text值

   # text=driver.find_element_by_xpath("//div[@id='nc_1__scale_text']/span") #目前只碰到3种情况：成功（请在在下方输入验证码,请点击图）；无响应（请按住滑块拖动)；失败（哎呀，失败了，请刷新）

   #     if text.text.startswith(u'请在下方'):
   #         print('成功滑动')
   #         break
   #     if text.text.startswith(u'请点击'):
   #         print('成功滑动')
   #         break
   #     if text.text.startswith(u'请按住'):
   #         continue
