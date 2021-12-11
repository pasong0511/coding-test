#5-7 교육과정 설계(자료구조-큐)
import sys
from collections import deque
sys.stdin = open("in1.txt", "r")
mandatory = input()
num = int(input())
courses_list = []
dq = []
dq = deque(dq)
sum = ''
print("의무 수강신청 과목", mandatory)
count = 0

for _ in range(num) :
    courses_list.append(input())
print(courses_list)

for courses in courses_list :
    count += 1
    for i in range(len(courses)) :              #수강과목 리스트에서 과목 하나씩 비교
        if courses[i] in mandatory:
            dq.append(courses[i])
    print("dq", dq)
    for i in range(len(dq)) :
        sum += dq.popleft()
    print("문자열 변환", sum)

    
    if sum == mandatory :
        print("#", count, " YES")
    else :
        print("#", count, " NO")

    print("------------")
    dq.clear()
    sum = ''