#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Python3 常见编码模式精简模板
包含日常80%高频使用场景
"""

import json
from typing import List, Dict, Optional
from pathlib import Path

#1. 数据结构操作（列表推导/字典操作）
numbers = [1,2,3,4,5]
squares = [x**2 for x in numbers]  #列表推导式
even_squares = {x: x**2 for x in numbers if x % 2 == 0}  #字典推导式

#2. 文件操作(读写/上下文管理)
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)  #JSON读取

with open('output.txt', 'w') as f:
    f.write('\n'.join(map(str, squares)))   # 文本写入

#3. 函数定义(类型注解/默认参数)
def process_data(data: List[int], multiplier: int = 1) -> Optional[Dict]:
    """典型函数模板:类型注解、默认参数、文档字符串"""
    try:
        return {item: item * multiplier for item in data}
    except Exception as e:
        print(f"Error: {e}")  # f-string格式化
        return None

#4. 类定义
class DataProcessor:
    """典型类模板: 初始化/实例方法/属性"""
    def __init__(self, data: List[int]):
        self.data = data
        self.processed = False

    def process(self) -> None:
        self.result = [x * 2 for x in self.data]
        self.processed = True

#5. 条件判断和循环
if __name__ == "__main__":
    # 路径操作
    file_path = Path("test.txt")

    # 异常处理
    try:
        processor = DataProcessor(numbers)
        processor.process()
        print(processor.result)

        #条件表达式
        status = "Success" if processor.processed else "Failed"
        print(f"Status: {status}")

    except Exception as e:
        print(f"Unexpected error: {e}")
