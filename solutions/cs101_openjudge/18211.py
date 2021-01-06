'''
18211: 军备竞赛
greedy/two pointer, http://cs101.openjudge.cn/practice/18211
'''
revenue = int(input())
schemes = [int(x) for x in input().split()]
schemes.sort()
# two pointers
made = 0
sold = len(schemes) - 1
eme_out = False
while made != sold:
    # if not meet criteria
    if eme_out is True:
        break

    if revenue >= schemes[made]:
        revenue -= schemes[made]
        made += 1
    else:
        temp = sold
        temp_rev = revenue

        while revenue < schemes[made]:
            if sold == made or len(schemes) - 1 - sold +1 > made:
                sold = temp
                revenue = temp_rev
                eme_out = True
                break

            revenue += schemes[sold]
            sold -= 1

else:
    # made == sold
    if revenue >= schemes[made]:
        revenue -= schemes[made]
        made += 1

more = made - (len(schemes)-1 - sold)
print(more)