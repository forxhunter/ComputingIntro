'''
Hit the Lottery
'''
denominations = [100, 20, 10, 5, 1]
amount = int(input())
count = 0
for denom in denominations:
    count += amount // denom
    amount %= denom

print(count)