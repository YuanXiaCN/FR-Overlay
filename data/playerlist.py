# -*- coding: gbk -*-
import tkinter as tk
from tkinter import filedialog

# 创建对话框
root = tk.Tk()
root.withdraw()

# 弹出选择文件对话框
log_file = filedialog.askopenfilename(title="选择日志文件")

# 打开日志文件并读取内容
try:
 with open(log_file, "r", encoding="gbk") as file:
    log_data = file.read()
    # 处理日志内容
    # 在这里你可以根据具体需求进行日志处理、提取信息等操作
    # 例如，你可以按行拆分日志，统计关键词出现的次数等等

    # 输出处理后的结果
    print(log_data)

except FileNotFoundError:
    print("找不到指定的日志文件，请检查路径是否正确。")