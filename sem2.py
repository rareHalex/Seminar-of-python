"""
Найти самое длинное предложение в тексте
"""
with open('.txt') as wpf:
    wpt = wpf = wpf.read()

end_element = ['.', '?', '!'] # конец предложения
tmp_str = ""
size = 0
long_string = ""
for c in wpt:
    if c not in end_element:
        tmp_str+=c
    elif len(tmp_str) >= len(long_string):
        long_string = tmp_str + c
        tmp_str = ""
"""
Найти предложение с наибольшим колличеством запятых
"""

import re
sentences = re.split(r'[\.!?]', wpt.replace('\n'," "))
print(max(sentences,key=lambda s: s.count(',')))
