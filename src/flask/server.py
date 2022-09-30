from flask import Flask

app = Flask(__name__)

data1 = {
    'code': 0,
    'header': '张三',
    'message': [
        {
            'type': 'ExpiringSoon',
            'level': 4,
            'remaining_days': 1,
            'content': '你好，你的周计划【周计划提醒工具开发】将于2022-10-03到期，请及时提交成果物，谢谢！'
        },
        {
            'type': 'ExpiresToday',
            'level': 3,
            'remaining_days': 0,
            'content': '你好，你的周计划【合同履约系统搬迁】今天到期，请及时提交成果物，谢谢！'
        },
        {
            'type': 'Expired',
            'level': 2,
            'remaining_days': -3,
            'content': '你好，你的周计划【EAS定价单同步上下游单据订货数量】已经逾期3天，请及时提交成果物，谢谢！'
        },
        {
            'type': 'LongOverdue',
            'level': 1,
            'remaining_days': -7,
            'content': '你好，你的周计划【EAS定价单添加来源单据类型】已经逾期7天，超时完成将不计入条数，请及时提交成果物，谢谢！'
        }

    ]
}


@app.route('/', methods=['GET'])
def json_demo():
    return data1


if __name__ == '__main__':
    app.run()
