import unicodedata


def is_number(n):
    try:
        float(n)
        return True
    except Exception as e:
        str(e)
        pass
    try:
        unicodedata.numeric(n)
        return True
    except Exception as e1:
        str(e1)
        pass
    return False


result = '{} is number :{}'.format
print(result(12, is_number(12)))

args = ["11", "12", "13"]
kwargs = {"o1": "hello", "o2": "python"}
print("{o1} world,{} {} {} {o2}".format(*args, **kwargs))
