import random

# 创建包含 "hello world" 和其他 7 个随机数的字典
data = {
    "message": "hello world",
    "number1": random.randint(1, 100),
    "number2": random.randint(1, 100),
    "number3": random.randint(1, 100),
    "number4": random.randint(1, 100),
    "number5": random.randint(1, 100),
    "number6": random.randint(1, 100),
    "number7": random.randint(1, 100)
}

# 打印字典内容
print(data)