'''
Minimum Capacity
exit before get in
Input

    The first line contains a single number n (2≤n≤1000) — the number of the tram's stops.

    Then n lines follow, each contains two integers ai and bi (0≤ai,bi≤1000)
    — the number of passengers that exits the tram at the i-th stop,
        and the number of passengers that enter the tram at the i-th stop.

        The stops are given from the first to the last stop in the order of tram's movement.

        The number of people who exit at a given stop does not exceed the total number of people in the tram immediately
        before it arrives at the stop. More formally, . This particularly means that a1=0.
        At the last stop, all the passengers exit the tram and it becomes empty. More formally, .
        No passenger will enter the train at the last stop. That is, bn=0.

Output

    Print a single integer denoting the minimum possible capacity of the tram (0 is allowed).
'''
n = int(input())
minimum = 0
current = 0
for i in range(n):
    peopleout, peoplein = list(map(int, input().split()))
    netin = peoplein - peopleout
    current = current + netin
    if current > minimum :
        minimum += (current - minimum)

print(minimum)




