n, m =list(map(int, input().split()))
magics = list(map(int, input().split()))
magics.sort()
diff = []
for i in range(1,n):
    diff.append( [magics[i] - magics[i-1],i])

diff.sort(key=(lambda x:x[0]), reverse=True)

cut = [0]
delta = 0
for i in range(m-1):
    cut.append(diff[i][1])

cut.sort()
cut.append(n)

for i in range(m):
    min_d = min(magics[cut[i]:cut[i+1]])
    max_d = max(magics[cut[i]:cut[i+1]])
    #print(magics[cut[i]:cut[i+1]])
    d = max_d - min_d
    delta += d
print(delta)
