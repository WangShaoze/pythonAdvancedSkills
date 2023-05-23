import json
from pythonSkills.netEngine import getMean

info_str = """
### 英语单词

|    单词     |      词性和意思 |
|:---------:|-----------:|
"""

with open(file="wordsEnglish.txt", mode="r", encoding="utf-8") as f:
    for uni in f.readlines():
        uni_ = uni.strip("\n").strip("")

        try:
            with open("db.json", mode="r", encoding="utf-8") as fi:
                words_li: list = json.load(fi)
                for word in words_li:
                    if word["word"] == uni_:
                        info_str += f"|{uni_}|{word['mean']}|\n"
                        break
                else:
                    getMean(uni_)
                    with open("db.json", mode="r", encoding="utf-8") as fi:
                        words_li: list = json.load(fi)
                        for word in words_li:
                            if word["word"] == uni_:
                                info_str += f"|{uni_}|{word['mean']}|\n"
                                break
        except Exception as e:
            print(e)

    with open(file="S-2.md", mode="w", encoding="utf-8") as fo:
        fo.write(info_str)
