#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()  # 将剪贴板上的内容传给text变量

# Separate lines and add stars.
lines = text.split('\n')  # 将text分割成一个列表

'''
for i in range(len(lines)):  # loop through all indexs in the "lines" list
    lines[i] = '* ' + lines[i]  # add star to each string in "lines" list
'''
newlines = []  # 申明一个空列表
for line in lines:  # 遍历lines中的所有元素
    newlines.append('* '+line)  # 将lines中的各个元素前加上"* "加入新列表

text = '\n'.join(newlines)  # 将列表重新连接成text

pyperclip.copy(text)  # 将处理后的text传给剪贴板