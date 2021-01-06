'''
16532: 上机考试（cs10117 Final Exam）
matrix, http://cs101.openjudge.cn/practice/16531/
“与周围任一同学做题情况相同的学生人数”和“班级优秀的人数”
'''
m, n = list(map(int,input().split()))
student_id = []
# status 用字符串格式储存,scores存储分数
status = []
scores = []

# 加保护圈并读取数据
student_id.append([-1]*(n+2))
for i in range(m):
    student_id.append([-1]+[int(x) for x in input().split()]+[-1])
student_id.append([-1]*(n+2))
for fake_i in range(m*n):
    t_status = input()
    correct = t_status.count('1')
    status.append(t_status)
    scores.append(correct)
# print(student_id)
# print(status)

#当前优秀率
max_great = 0.4
great_num = 0
students_num = m*n
scores.sort(reverse=True)
high = max(scores)
for score in range(high,0,-1):
    temp = scores.count(score)
    if (great_num+temp)/students_num <= max_great:
        great_num+=temp
    else:
        break

#相同判断矩阵
direct = [[0,1],[0,-1],[1,0],[-1,0]]
same_status = 0

for y in range(1,m+1):
    for x in range(1,n+1):
        self_id = student_id[y][x]
        self_status = status[self_id]

        for dy, dx in direct:
            oth_id = student_id[y+dy][x+dx]
            if oth_id != -1:
                oth_status = status[oth_id]
                if oth_status == self_status:
                    same_status += 1
                    break

print(same_status,great_num)