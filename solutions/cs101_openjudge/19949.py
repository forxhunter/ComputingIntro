'''
19949提取实体v0.2
删除算一个实体中间的### ###形式
匹配###[^#]*###
'''
import re
n = int(input())
all = 0
for fake_i in range(n):
    sentence = input()
    det = r'###\s###'
    detpattern = re.compile(det)
    p = r'###[^#]*###'
    pattern = re.compile(p)
    sentence = re.sub(detpattern, '', sentence)
    lists = re.findall(pattern, sentence)
    all += len(lists)

print(all)