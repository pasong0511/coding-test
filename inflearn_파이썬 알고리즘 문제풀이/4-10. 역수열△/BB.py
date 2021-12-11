#4-10 역수열(그리디)
import sys
sys.stdin = open("in0.txt", "r")
n = int(input())
reversed_sequ = list(map(int, input().split()))
origin_sequ = [0]*n                   #0으로 초기화

print("reversed_sequ", reversed_sequ)
print("origin_sequ", origin_sequ)

for i in range(n) :
    for j in range(n) :
        if reversed_sequ[i] == 0 and origin_sequ[j] == 0 :      #역순열이 0값 origin_sequ에 추가
            print(origin_sequ[i])
            origin_sequ[j] = i + 1
            break
        elif origin_sequ[j] == 0 :
            reversed_sequ[i] -= 1

# for i in origin_sequ :
#     print(i, end = " ")