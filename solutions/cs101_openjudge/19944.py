'''
What day is it today?

'''
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
n = int(input())
for fake_i in range(n):
    date = input()
    year = int(date[0:4])

    m = int(date[4:6])
    d = int(date[6:])

    if m == 1:
        m = 13
        year -= 1
    elif m == 2:
        m = 14
        year -= 1
    year = str(year)

    y = int(year[2:4])
    c = int(year[0:2])
    result = (y + y//4 + c//4 - 2*c + 26*(m+1)//10 + d - 1) % 7
    result = int(result)
    if fake_i != n-1:
        print(days[result]+' ')
    else:
        print(days[result], end='')