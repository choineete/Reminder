import os
import urllib
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

def get_soup(url):
    html_doc = url
    req = urllib.request.Request(html_doc)
    webpage = urllib.request.urlopen(req)
    html = webpage.read()

    soup = BeautifulSoup(html, 'html.parser')  # 文档对象

    return soup

# 两台服务器地址
logs_url_1 = "http://10.24.1.121:8888/easlog/"
logs_url_2 = "http://10.24.1.122:8888/easlog/"


print("********************************** 请选择服务器 *************************************")
print()
print("******************* 1、121服务器 http://10.24.1.121:8888/easlog/ *******************")
print()
print("******************* 2、122服务器 http://10.24.1.122:8888/easlog/ *******************")
print()

url = ''
def choose_server():
    opt = input("请选择 1 或者 2：")
    if opt == '1':
        return logs_url_1
    elif opt == '2':
        return logs_url_2
    else:
        print("请输入 1 或 2")
        choose_server()

url = choose_server()

current_dir = os.getcwd() + "\\"+ "easlogs\\"
server_list_soup = get_soup(url)
for s in server_list_soup.find_all('a'):
    # dir = current_dir + s.string[-2:] + "\\"
    # os.makedirs(dir)
    if "./" not in s.string:
        log_list_soup = get_soup(url + s.string + "logs")

        for l in log_list_soup.find_all('a'):

            if "apusic" in l.string:

                file_path = url + s.string + "logs/" + l.string

                f = requests.get(file_path)

                # 下载文件
                dir = current_dir + s.string[:-1]
                if not os.path.exists(dir):  # 判断是否存在文件夹如果不存在则创建为文件夹
                    os.makedirs(dir)

                with open(dir +"\\"+ l.string + ".log", "wb") as code:
                    code.write(f.content)
    print("下载" + s.string + "日志" + "成功")
print("全部日志下载成！！！")
# 打包语句
# pyinstaller -F test/get_eas_logs.py