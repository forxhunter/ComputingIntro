'''
OJ18224: 找魔数 (math), cs10118 Final Exam
http://cs101.openjudge.cn/practice/18224/
'''
m = int(input())

squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961]
magics = set()
for i in range(len(squares)):
    for j in range(i,len(squares)):
        temp = squares[i]+squares[j]
        if temp <= 1000:
            magics.add(squares[i]+squares[j])
        else:
            break

numbers = [int(x) for x in input().split()]
for num in numbers:
    if num in magics:
        print(bin(num),oct(num),hex(num),sep=' ')

''' to find all squares <= 1000
i = 1
square = i**2
while square <= 1000:
    squares.append(square)
    i += 1
    square = i ** 2
print(squares)
'''