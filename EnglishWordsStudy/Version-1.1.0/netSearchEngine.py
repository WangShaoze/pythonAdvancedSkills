import json
import random
import requests


def engine(word):
    url = "https://fanyi.baidu.com/sug"
    ua_li = [
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    ]
    headers = {
        "User-Agent": random.choice(ua_li)
    }
    data = {
        'kw': word
    }
    resp = requests.post(url, headers=headers, data=data)
    # 用Json模块把得到的json数据（其实它就是一种str字符串）转成Python中字典
    data_ = json.loads(resp.content.decode("unicode_escape"))['data']
    return [f"insert into word_for_cet6 values('{uni['k']}', '{uni['v']}');" for uni in data_]


if __name__ == '__main__':
    for uni_ in engine("英语"):
        print(uni_)
