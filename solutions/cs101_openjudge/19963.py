import re
n = int(input())
positions = input().split(' ')
prices = [int(x) for x in input().split()]

xjb = []
pi= []
for i in range(n):
    x,y = [int(x) for x in re.findall(r'\d+', positions[i])]
    xjb.append([(x+y)/prices[i],i])
    pi.append([prices[i],i])
pi.sort(key=(lambda x: x[0]),reverse=True)
xjb.sort(key=(lambda x: x[0]))
xjb_m = (xjb[(n-1)//2][0]+xjb[n//2][0])/2
price_m = (pi[(n-1)//2][0]+pi[n//2][0])/2
index_xjb = []
count = 0

for i in range(n//2,n):
    if xjb[i][0] > xjb_m:

        for m in range(i,n):
            index_xjb.append(xjb[m][1])
        break


for i in range(n//2, n):
    if pi[i][0] < price_m:
        for j in range(i,n):

            if pi[j][1] in index_xjb:
                count +=1
        break
    if pi[i][0] > price_m:
        break
print(count)