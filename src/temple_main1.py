import json
import sys
import threading
import requests

from src.gui.UICreator import create_root_window, create_root_frame, create_sys_tray, create_message_item


def get_params():
    emp_num = (sys.argv[0])[4: 16]
    params = {
        'account': emp_num
    }
    return params


def get_result(params):
    url = 'http://127.0.0.1:5000'
    headers = {
        'accountId': '12345678900'
    }
    result = requests.get(url=url, headers=headers, params=params)
    result = json.loads(result.content)
    return result


def make_message_list(result):
    msg_list = []
    for msg in result['message']:
        msg_list.append(msg['content'])
    return msg_list


if __name__ == '__main__':
    root = create_root_window()
    tray = create_sys_tray(root)
    root_frame = create_root_frame(root)

    # 获取用户工号，构建请求参数
    params = get_params()
    # 请求数据，返回结果字典
    result = get_result(params)
    # 构造消息列表
    msg_list = make_message_list(result)

    for i in range(0, len(msg_list)):
        create_message_item(root_frame=root_frame, msg=msg_list[i], num=i+1)

    threading.Thread(target=tray.run, daemon=True).start()
    root.mainloop()
