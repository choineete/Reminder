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
    level_list = []
    schedule_list = result['message']

    # 根据剩余天数做排序，逾期天数最长的 排到最前面
    msg_list_len = len(schedule_list)
    for i in range(msg_list_len - 1):
        for j in range(msg_list_len - i - 1):
            if schedule_list[j]['remaining_days'] > schedule_list[j + 1]['remaining_days']:
                schedule_list[j], schedule_list[j + 1] = schedule_list[j + 1], schedule_list[j]

    for msg in schedule_list:
        msg_list.append(msg['content'])
        level_list.append(msg['level'])
    return msg_list, level_list
