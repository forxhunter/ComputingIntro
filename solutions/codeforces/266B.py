'''
Input

    The first line contains two integers n and t (1≤n,t≤50),
    which represent the number of children in the queue and the time after which the queue will
    transform into the arrangement you need to find.

    The next line contains string s, which represents the schoolchildren's initial arrangement. If the i-th position in the
    queue contains a boy, then the i-th character of string s equals "B", otherwise the i-th character equals "G".
Output

    Print string a, which describes the arrangement after t seconds. If the i-th position has a boy after the needed time,
    then the i-th character a must equal "B", otherwise it must equal "G".
'''
n, t = list(map(int, input().split()))
queue = input()
skip = False
for d in range(t):
    for i in range(n-1):
        if skip == True:
            skip = False
            continue

        if queue[i] == 'B' and queue[i+1] == 'G':
            if i < n-2:
                skip = True

            if i == 0:
                queue = 'GB' + queue[2:]
            else:
                queue = queue[:i] + 'GB' + queue[i+2:]

print(queue)

