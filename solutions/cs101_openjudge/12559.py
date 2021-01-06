n = int(input())
given = input().split()


class LargerNumKey(str):
    def __lt__(self,  y):
        return self + y > y + self
class SmallerNumKey(str):
    def __lt__(self,  y):
        return self + y < y + self

def largestNumber(nums):
    largest_num = ''.join(sorted(nums, key=LargerNumKey))
    return '0' if largest_num[0] == '0' else largest_num

def smallestNumber(nums):
    smallest_num = ''.join(sorted(nums, key=SmallerNumKey))
    return '0' if smallest_num[0] == '0' else smallest_num

print(largestNumber(given),smallestNumber(given),sep=' ')
