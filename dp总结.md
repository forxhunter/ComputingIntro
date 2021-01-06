# dp问题

## 1759: 最长上升子序列

dp, http://cs101.openjudge.cn/practice/1759

一个数的序列*b~i~*，当*b~1~* < *b~2~* < ... < *b~S~*的时候，我们称这个序列是上升的。对于给定的一个序列(*a~1~*, *a~2~*, ..., *a~N~*)，我们可以得到一些上升的子序列(*a~i1~*, *a~i2~*, ..., *a~iK~*)，这里1  ≤   *i~1~* < *i~2~* < ... < *i~K~*  ≤   N。比如，对于序列(1, 7, 3, 5, 9, 4, 8)，有它的一些上升子序列，如(1, 7), (3, 4, 8)等等。这些子序列中最长的长度是4，比如子序列(1, 3, 5, 8).

你的任务，就是对于给定的序列，求出最长上升子序列的长度。

**输入**

输入的第一行是序列的长度N (1  ≤   N  ≤   1000)。第二行给出序列中的N个整数，这些整数的取值范围都在0到10000。

**输出**

最长上升子序列的长度。

样例输入

```
7
1 7 3 5 9 4 8
```

样例输出

```
4
```

来源：翻译自 Northeastern Europe 2002, Far-Eastern Subregion 的比赛试题



2020fall-cs101，王君宇。思路：和最大上升子序列和类似，都是需要双重循环的 dp，外循环确定每个元素 dp初始值为 1，内循环遍历小数进行转移方程。

```python
input()
b = [int(x) for x in input().split()]

n = len(b)
dp = [1]*n

for i in range(n):
    for j in range(i):
        if b[j]<b[i]:
            dp[i] = max(dp[j]+1, dp[i])
    
print(max(dp))
```

## 3532: 最大上升子序列和

dp, http://cs101.openjudge.cn/practice/3532/

一个数的序列bi，当b~1~ < b~2~ < ... < b~S~的时候，我们称这个序列是上升的。对于给定的一个序列(a~1~, a~2~, ...,a~N~)，我们可以得到一些上升的子序列(a~i1~, a~i2~, ..., a~iK~)，这里1 <= i1 < i2 < ... < iK <= N。比如，对于序列(1, 7, 3, 5, 9, 4, 8)，有它的一些上升子序列，如(1, 7), (3, 4, 8)等等。这些子序列中序列和最大为18，为子序列(1, 3, 5, 9)的和.

你的任务，就是对于给定的序列，求出最大上升子序列和。注意，最长的上升子序列的和不一定是最大的，比如序列(100, 1, 2, 3)的最大上升子序列和为100，而最长上升子序列为(1, 2, 3)

**输入**

输入的第一行是序列的长度N (1 <= N <= 1000)。第二行给出序列中的N个整数，这些整数的取值范围都在0到10000（可能重复）。

**输出**

最大上升子序列和

样例输入

```
7
1 7 3 5 9 4 8
```

样例输出

```
18
```



思路：从第一个数开始逐次递推，考虑第 i个数的情况时，再从第一个数开始逐个检验，如果第 i个数大于前 i个数中的第 j个数，那么将前 j个数的最大上升子序列和再加上第 i个数，即构成前 i个数上升子序列和的一种情况，再取这些情况中的最大值，即得到前 i个数的最大上升子序列和。最后依次递推，即可得到整个序列的最大上升子序列和。

主要思路就是记录把每个数作为序列最后一位时的序列和，取 max。即，以每一项为末项的最大上升子序列和。

2020fall-cs101，邹思清。感觉跟我之前做的dp不太一样。之前的dp大多是计算n位之前满足的答案，而这道题使用的递推公式也不仅仅是相邻几项，而且还使用了max，做的时候没有想到，又学到新方法了。

```python
input()
b = [int(x) for x in input().split()]

n = len(b)
dp = [0]*n

for i in range(n):
    dp[i] = b[i]
    for j in range(i):
        if b[j]<b[i]:
            dp[i] = max(dp[j]+b[i], dp[i])
    
print(max(dp))
```



## 1808: 最长公共子序列

dp, http://cs101.openjudge.cn/practice/1808

我们称序列Z = < z1, z2, ..., zk >是序列X = < x1, x2, ..., xm >的子序列当且仅当存在 **严格上升** 的序列< i1, i2, ..., ik >，使得对j = 1, 2, ... ,k, 有xij = zj。比如Z = < a, b, f, c > 是X = < a, b, c, f, b, c >的子序列。

现在给出两个序列X和Y，你的任务是找到X和Y的最大公共子序列，也就是说要找到一个最长的序列Z，使得Z既是X的子序列也是Y的子序列。

输入

输入包括多组测试数据。每组数据包括一行，给出两个长度不超过200的字符串，表示两个序列。两个字符串之间由若干个空格隔开。

输出

对每组输入数据，输出一行，给出两个序列的最大公共子序列的长度。

样例输入

```
abcfbc         abfcab
programming    contest 
abcd           mnp
```

样例输出

```
4
2
0
```

来源：翻译自Southeastern Europe 2003的试题

```python
while True:
    try:
        a, b = input().split()
    except EOFError:
        break
    
    alen = len(a)
    blen = len(b)
    
    dp = [[0]*(blen+1) for i in range(alen+1)]

    for i in range(1, alen+1):
        for j in range(1, blen+1):
            if a[i-1]==b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])


    print(dp[alen][blen])
```

## 1775: 采药（01背包）

dp, http://cs101.openjudge.cn/practice/1775

辰辰是个很有潜能、天资聪颖的孩子，他的梦想是称为世界上最伟大的医师。为此，他想拜附近最有威望的医师为师。医师为了判断他的资质，给他出了一个难题。医师把他带到个到处都是草药的山洞里对他说：“孩子，这个山洞里有一些不同的草药，采每一株都需要一些时间，每一株也有它自身的价值。我会给你一段时间，在这段时间里，你可以采到一些草药。如果你是一个聪明的孩子，你应该可以让采到的草药的总价值最大。”

如果你是辰辰，你能完成这个任务吗？

输入

输入的第一行有两个整数T（1 <= T <= 1000）和M（1 <= M <= 100），T代表总共能够用来采药的时间，M代表山洞里的草药的数目。接下来的M行每行包括两个在1到100之间（包括1和100）的的整数，分别表示采摘某株草药的时间和这株草药的价值。

输出

输出只包括一行，这一行只包含一个整数，表示在规定的时间内，可以采到的草药的最大总价值。

样例输入

```
70 3
71 100
69 1
1 2
```

样例输出

```
3
```

来源：NOIP 2005



解题思路：0-1背包问题(Knapsack problem)。内层循环（列）时间T，外层循环（行）药草M。

图解，可以参照《算法图解》，作何：Aditya Bhargava，译者：袁国忠。2016年出版。

```python
T, M = map(int, input().split())
dp = [ [0] + [0]*T for _ in range(M+1)]

t = [0]
v = [0]
for i in range(M):
        ti, vi = map(int, input().split())
        t.append(ti)
        v.append(vi)

for i in range(1, M+1):			# 外层循环（行）药草M
        for j in range(0, T+1):	# 内层循环（列）时间T
                if j >= t[i]:
                        dp[i][j] = max(dp[i-1][j], dp[i-1][j-t[i]] + v[i])
                else:
                        dp[i][j] = dp[i-1][j]

print(dp[M][T])
```

## 90: 滑雪

dp/dfs similar, http://cs101.openjudge.cn/practice/90/

Michael喜欢滑雪百这并不奇怪， 因为滑雪的确很刺激。可是为了获得速度，滑的区域必须向下倾斜，而且当你滑到坡底，你不得不再次走上坡或者等待升降机来载你。Michael想知道载一个区域中最长的滑坡。区域由一个二维数组给出。数组的每个数字代表点的高度。下面是一个例子

```
 1  2  3  4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
```


一个人可以从某个点滑向上下左右相邻四个点之一，当且仅当高度减小。在上面的例子中，一条可滑行的滑坡为24-17-16-1。当然25-24-23-...-3-2-1更长。事实上，这是最长的一条。

**输入**

输入的第一行表示区域的行数R和列数C(1 ≤  R,C ≤  100)。下面是R行，每行有C个整数，代表高度h，0≤ h≤ 10000。

**输出**

输出最长区域的长度。

样例输入

```
5 5
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
```

样例输出

```
25
```

来源：USACO

![image-20210106082651238](dp%E6%80%BB%E7%BB%93.assets/image-20210106082651238.png)

2020fall-cs101，刘安澜。我对老师的代码进行了一个改进，因为本题说高度最大值不超过10000，所以保护圈元素取10001即可满足不超过边界，这样函数更加简洁。

2020fall-cs101，李元锋。正常思路是从第一个元素开始，判断滑雪最长距离，过一遍。但这里有很多重复计算的子问题，所以引入 dp函数，如果坐标周围有比自己低的坡道，判断滑哪条周围的坡道最长就滑哪条。然后直接遍历一遍二维数组即可，这里要添加保护圈以防万一滑出边界。

```python
r, c = map(int, input().split())
node = []       # height of each element
node.append( [100001 for _ in range(c+2)] )
for _ in range(r):
    node.append([100001] +[int(_) for _ in input().split()] + [100001])
    
node.append( [100001 for _ in range(c+2)] )

dp = [[0]*(c+2) for _ in range(r+2)]
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0,-1]

def dfs(i,j):
    if dp[i][j]>0:
        return dp[i][j]
    
    for k in range(4):       
        if node[i+dx[k]][j+dy[k]] < node[i][j]:
            dp[i][j] = max( dp[i][j], dfs(i+dx[k], j+dy[k])+1 )

    return dp[i][j]

ans = 0
for i in range(1, r+1):
    for j in range(1, c+1):
        ans = max( ans, dfs(i,j) )

print(ans+1)
```



2020fall-cs101，王康安。虽然开了个叫 dp的数组，但我感觉解法其实更像贪心。刚巧昨天在 oj上写了一道 Huffman树的题（18164：剪绳子），这里我的策略就很相似。把所有区域的高度和坐标存到一个栈里，排序，每次都把栈内高度最高的区域弹出去并处理。当前这个区域是到不了那些之前已经弹出的，比当前这个区域更高的区域的，也就是说，之前那些区域都不会影响这一步的策略，具有无后效性和最优子结构性质。状态转移方程非常直白就不多说了。上代码，毕竟没有按 dfs去写所以标了注释：

```python
r,c = [int(x) for x in input().split()]
rgn = [[20000]*(c+2)] 
for i in range(r):    
    rgn.append([20000]+[int(x) for x in input().split()]+[20000])
rgn.append([20000]*(c+2))       #读入上保护圈方便处理边界情况

stack = []
for i in range(1,r+1):
    for j in range(1,c+1):        
        stack.append([rgn[i][j], i, j])
stack.sort()                    #所有节点按从小到大排序

loc = [[1,0],[-1,0],[0,1],[0,-1]]   #方向数组

dp = [[1]*(c+2) for x in range(r+2)] #dp数组初始化全为1 上保护圈只是为了和rgn数组下标保持一致

while stack != []:    
    temp = stack.pop()  #用temp数组保存出栈值该值也是当前栈内最大值
    for i in range(4):
        if rgn[temp[1]+loc[i][0]][temp[2]+loc[i][1]]<rgn[temp[1]][temp[2]]: 
            #由于是栈内最大值此条件一定成立这里仅是为了处理保护圈情况            
            dp[temp[1]+loc[i][0]][temp[2]+loc[i][1]] = \
            max(dp[temp[1]+loc[i][0]][temp[2]+loc[i][1]],dp[temp[1]][temp[2]]+1)
            #状态转移方程
out = 0
for i in range(1,r+1):    
    out = max(out,max(dp[i]))
print(out)
```

## POJ2373:灌溉草场(直线的条件动态分割)

```python
from collections import deque
import math

input = __import__('sys').stdin.readline
n, l = map(int, input().split())
a, b = map(int, input().split())
cow = [False] * (l + 1)
for i in range(n):
    s, e = map(int, input().split())
    for j in range(s + 1, e):
        cow[j] = True
if l % 2 == 1:
    print(-1)
elif l < 2 *a:
    print(-1)
elif l <= 2 * b:
    print(1)
else:
    dp = [float('inf')] * (l + 1)
    for i in range(2 * a, 2 * b + 1, 2):
        if not cow[i]:
            dp[i] = 1
    o_list = deque([dp[0]])
    o_site = deque([0])
    k = (b - a) * 2  + 1
    for i in range(2, k, 2):
        cur = dp[i]
        try:
            while cur <= o_list[-1]:
                o_list.pop()
                o_site.pop()
        except:
            pass
        o_list.append(cur)
        o_site.append(i)
    for i in range(2 * (b + 1), l + 1, 2):
        cur = dp[i - 2 * a]
        try:
            while cur <= o_list[-1]:
                o_list.pop()
                o_site.pop()
        except:
            pass
        o_list.append(cur)
        o_site.append(i - 2 * a)
        while o_site[0] < i - 2 * b:
            o_list.popleft()
            o_site.popleft()
        if not cow[i]:
            dp[i] = o_list[0] + 1
    if math.isinf(dp[l]):
        print(-1)
    else:
        print(dp[l])
```

