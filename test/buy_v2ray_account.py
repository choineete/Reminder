import os
from time import sleep
from selenium import webdriver  # 从selenium中引入webdriver
from selenium.webdriver.common.by import By


def login_mantis():
    option = webdriver.EdgeOptions()
    option.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'  # 这里添加edge的启动文件=>chrome的话添加chrome.exe的绝对路径
    driver = webdriver.Edge(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe', options=option)  # 这里添加的是driver的绝对路径

    driver.maximize_window()  # 浏览器窗口最大化

    # driver.implicitly_wait(3)  # 隐式等待

    driver.get("https://okgg.top/auth/login")  # 获取URL，打开页面
    sleep(1)  # 直接等待

    username = driver.find_element(By.XPATH, '/html/body/div[1]/div/form/div/div[2]/div/input')  # 通过Xpath定位获取输入账号框
    username.send_keys("hrtnrnVCWEVrddn@qq.com")  # 输入账号
    sleep(1)

    password = driver.find_element(By.XPATH, "/html/body/div[1]/div/form/div/div[3]/div/input")  # 通过Xpath定位获取输入密码框
    password.send_keys("12345678")  # 输入密码
    sleep(1)

    login = driver.find_element(By.XPATH, "/html/body/div[1]/div/form/div/div[5]/button")  # 通过Xpath定位获取登录按钮
    login.click()  # 点击登录按钮

    sleep(3)

    vip1 = driver.find_element(By.XPATH,
                               '/html/body/main/div[2]/section/div[1]/div[1]/div/div[1]/div[1]/div[2]/div/dd')  # 定位VIP等级

    if 'VIP 1' != vip1.text:
        buy1 = driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[1]/ul[2]/li[2]/a')  # 定位 套餐购买按钮
        buy1.click()
        sleep(1)

        buy2 = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/section/div[3]/div[2]/div/a')  # 定位 公益3购买按钮
        buy2.click()
        sleep(1)

        buy3 = driver.find_element(By.XPATH,
                                   '/html/body/main/div[2]/div/section/div[5]/div/div/div[3]/p/button')  # 定位 优惠码确认
        buy3.click()
        sleep(3)

        buy4 = driver.find_element(By.XPATH,
                                   '/html/body/main/div[2]/div/section/div[6]/div/div/div[3]/p/button')  # 定位 订单确认
        buy4.click()
        sleep(1)
    else:
        print("账户已经是 VIP 1")
        os.system("pause")


if __name__ == '__main__':
    login_mantis()
