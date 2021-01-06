'''
It seems like the year of 2013 came only yesterday. Do you know a curious fact?
The year of 2013 is the first year after the old 1987 with only distinct digits.

Now you are suggested to solve the following problem: given a year number,
find the minimum year number which is strictly larger than the given one and has only distinct digits.
'''


def isdistinct(year):
    judge = str(year)
    result = True
    for i in range(4):
        for j in range(i):
            if judge[i] == judge[j]:
                result = False
                break
    return result


year = int(input())
year += 1
while not isdistinct(year):
    year += 1
print(year)