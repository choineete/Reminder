import requests
import json

url = 'http://127.0.0.1:5000'
headers = {
    'accountId': '12345678900'
}

r = requests.get(url, headers=headers)
content = json.loads(r.content)
msg_list = []
# content['message'][0]['content']
for msg in content['message']:
    print(msg['content'])
    msg_list.append(msg['content'])

str = 'c://010200002082'
print(len(str))
print(str[4: 16])
