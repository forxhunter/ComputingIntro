english = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10,
           'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14,
           'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19,
            'twenty': 20, 'thirty':30, 'forty':40,
           'fifty': 50 , 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90,  }
level = {'hundred', 'thousand',}
lines = input().split()
negative = False
if lines[0] == 'negative':
    lines = lines[1:]
    negative = True
total = 0
number = 0
for ele in lines:

    if ele == 'million':
        number *= 1000000
        total += number
        number = 0
    elif ele == 'hundred':
        number *= 100

    elif ele == 'thousand':
        number *= 1000
        total += number
        number = 0
    else:
        number += english[ele]
else:
    total += number
if negative is True:
    total = - total
print(total)