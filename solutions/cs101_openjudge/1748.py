n, m = list(map(int, input().split()))
while n != 0:
    status = [x for x in range(n)]
    current = 0
    while len(status) != 1:
        current = (current + m-1 ) % (len(status))
        status.pop(current)
    # read new line
    print(status[0]+1)
    n, m = list(map(int, input().split()))