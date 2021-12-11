#5-7 교육과정 설계(자료구조-큐)
#dong
import sys
import re
from collections import deque
sys.stdin = open("in2.txt", "r")
mandatory = input()
num = int(input())
courses_list = []
#print("의무 수강신청 과목", mandatory)
count = 0

for _ in range(num) :
    courses_list.append(input())
# print(courses_list)

text="([A-Z]*)?"
regex = text
for subject in mandatory:
    regex += subject + text
# print(regex)

for courses in courses_list :
    count += 1
    m = re.search(regex, courses)
    if m is None:
        print("#", count, " NO")
    else:
        print("#", count, " YES")