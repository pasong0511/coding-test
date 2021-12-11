#5-7 교육과정 설계(자료구조-큐)
#dong
import sys
from collections import deque
#sys.stdin = open("in0.txt", "r")
mandatory = input()
num = int(input())
courses_list = []
count = 0

for _ in range(num) :
    courses_list.append(input())

for courses in courses_list :
    count += 1
    target = deque(mandatory)
    for i in courses :              #수강과목 리스트에서 과목 하나씩 비교
        if len(target) == 0:
            break
        if i == target[0]:
            target.popleft()
    if len(target) != 0:
        print("#", count, " NO")
    else:
        print("#", count, " YES")