#4-8 침몰하는 타이타닉(그리디)
import sys
sys.stdin = open("in5.txt", "r")
n, limit = map(int, input().split())
weight = list(map(int, input().split()))
safe_boat = 0

print(n, limit)
print(weight)

weight.sort()

print(weight)
start_index = 0
end_index = n-1

print(start_index)
print(end_index)

while start_index < end_index :
    if weight[start_index] + weight[end_index] > limit:            #두명 더했을때 limit 초과인경우
        print(limit, "초과", weight[start_index] + weight[end_index])
        print("변경전 초과 인덱스 : ", start_index, end_index)
        safe_boat += 1                                              #limit 보다 큰 값인경우 safe_boat 보트 단독 추가
        end_index -= 1                                              #뒤에 있는 값 단독으로 보트 주고 end_index 감소
        print("변경후 초과 인덱스 : ", start_index, end_index)
    
    else :                                                          #두명 더했을때 limit 미달인경우
        print(limit, "미달", weight[start_index] + weight[end_index])
        print("변경전 미달 인덱스 : ", start_index, end_index)
        safe_boat += 1                                              #보트 추가
        start_index += 1                                            #시작 인덱스 1증가
        end_index -= 1                                              #끝 인덱스 1 감수
        print("변경후 미달 인덱스 : ", start_index, end_index)

if start_index == end_index : 
    safe_boat += 1

print(safe_boat)