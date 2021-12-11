#5-5 응급실(자료구조-큐)
import sys
from collections import deque
sys.stdin = open("in1.txt", "r")
n, pick = map(int, input().split())
patient_dq = deque(list(map(int, input().split())))
count = 0
cure_list = []

print(n, pick, patient_dq)

while patient_dq:
    ergency = max(patient_dq)           #우선순위 높은 긴급 환자 체크
    if patient_dq[0] < ergency :                #맨 앞에 있는 환자가 우선순위가 긴급환자보다 작으면
        patient_dq.append(patient_dq.popleft())        #앞에 있던 환자 뒤로 보내기
        print(patient_dq)
    elif patient_dq[0] >= ergency :
        cure = patient_dq.popleft()     #치료받음
        cure_list.append(cure)
        count += 1

print(cure_list)