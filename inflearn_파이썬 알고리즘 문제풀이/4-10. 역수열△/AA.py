#4-10 역수열(그리디)
import sys
sys.stdin = open("in0.txt", "r")
n = int(input())
reversed_sequ = list(map(int, input().split()))
# origin_sequ = [0]*n                   #0으로 초기화
origin_sequ = [0, 0, 0, 0, 0, 0, 0, 0]


print(n)
print("역수열", reversed_sequ)
print("원본수열", origin_sequ)

for i in range(n) :
    zero_count = 0                      #0 카운트
    for j in range(n) :
        if origin_sequ[j] == 0:         # origin_sequ에 0이 있을때
            zero_count += 1             # 0 카운트 개수 증가
        if zero_count == reversed_sequ[i] :
            if origin_sequ[zero_count] == 0 :
                origin_sequ[zero_count] = i+1
            else :
                origin_sequ[zero_count+1] = i+1



print(origin_sequ)