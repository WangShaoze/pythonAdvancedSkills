import random
import time

# 整数
x = random.randint(0, 1000)
print("随即整数x是:{}".format(x))

# 随机偶数
x = random.randrange(0, 1000, 2)  # 2代表步长
print("随即偶数x是{}".format(x))

# 随即浮点数
x = random.uniform(1, 3)
print("随即浮点数x是{}".format(x))

# 随即生成字符或字符串或数字组成的随即码
print(chr(65 + random.randint(0, 25)))
print(chr(97 + random.randint(0, 25)))
for i in range(0, 10):
    for j in range(8):
        a = random.randint(0, 9)
        b = chr(97 + random.randint(0, 25))
        c = chr(65 + random.randint(0, 25))
        print(random.choice([a, b, c]), end="")
    print()
    time.sleep(0.2)
