import re
strings = input()
strings = strings.lower()
count = []

pre = strings[0]
num = 0
for ele in strings:
    if ele == pre:
        num += 1

    else:
        formating = '('+pre+','+str(num)+')'
        count.append(formating)
        num = 1
        pre = ele
else:
    formating = '('+pre+','+str(num)+')'
    count.append(formating)
print(*count,sep='')