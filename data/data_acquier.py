import json
import sys

import requests


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
    try:
        result = requests.get(url=url, headers=headers, params=params)
        result = json.loads(result.content)
    except:
        print('请求出错')
        result = None
        pass
    return result


def make_message_list(result):
    msg_list = []
    for msg in result['message']:
        msg_list.append(msg['content'])
    return msg_list