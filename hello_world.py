"""
Hello World 示例模块

这个模块创建一个包含问候消息和随机数的字典，并将其打印出来。
用于演示Python基本语法和随机数生成。
"""

import random

def generate_data():
    """创建包含 "hello world" 和其他 7 个随机数的字典"""
    data = {"message": "hello world"}
    for i in range(1, 8):
        data[f"number{i}"] = random.randint(1, 100)
    return data

def main():
    # 生成并打印字典内容
    data = generate_data()
    print(data)

if __name__ == "__main__":
    main()