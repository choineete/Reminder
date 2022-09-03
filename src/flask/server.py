from flask import Flask

app = Flask(__name__)

data1 = {
    'code': 0,
    'header': '张三',
    'message': [
        {
            'content': '你好，你的周计划【周计划提醒工具开发】将于2022-09-05到期，请及时提交成果物，谢谢！'
        },
        {
            'content': '你好，你的周计划【合同履约系统搬迁】今天到期，请及时提交成果物，谢谢！'
        },
        {
            'content': '你好，你的周计划【运维知识库及问题汇总系统开发】于2022-09-02到期、已逾期3天，请及时提交成果物，谢谢！'
        }
    ]
}


@app.route('/', methods=['GET'])
def json_demo():
    return data1


if __name__ == '__main__':
    app.run()
