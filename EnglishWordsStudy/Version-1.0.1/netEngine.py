import json
import random

import requests


def getMean(word):
    url = "https://fanyi.baidu.com/sug"
    data = {
        "kw": word
    }
    ua_li = ["Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0",
             "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36",
             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38",
             "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36",
             "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"]
    ua = random.choice(ua_li)
    headers = {
        'User-Agent': ua
    }

    resp = requests.post(url, headers=headers, data=data)
    data_list = resp.json()['data']
    with open("db.json", mode="r", encoding="utf-8") as fi:
        data_: list = json.load(fi)

    for item in data_list:
        dic = dict()
        dic["word"] = item['k']
        dic["mean"] = item['v']
        data_.append(dic)

    with open("db.json", mode="w", encoding="utf-8") as fo:
        json.dump(obj=data_, fp=fo, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    getMean("cool")
