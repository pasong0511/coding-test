#4-5 회의실 배정(그리디)
import sys
# sys.stdin = open("in3.txt", "r")
n = int(input())
meeting_time = []
count = 1

for i in range(n):
    a, b = map(int, input().split())
    meeting_time.append((a, b))
# print(meeting_time)

meeting_time.sort(key = lambda x : (x[1], x[0]))            #끝나는 시간 오름차순 정렬
# print(meeting_time)

catch_time = meeting_time[0][1]                             #잡은 회의 끝시간 선택(빨리 끝나는 회의 시간)

for i in range(1, len(meeting_time)) :                      #초기 회의 시작 부터 회의 시간 목록 전체 반복
    if catch_time <= meeting_time[i][0] :                   #제일 빨리 끝나는 회의 시간과 빨리 시작하는 회의 시간 비교
        count += 1
        catch_time = meeting_time[i][1]                     #잡은 회의 끝시간 교체
print(count)