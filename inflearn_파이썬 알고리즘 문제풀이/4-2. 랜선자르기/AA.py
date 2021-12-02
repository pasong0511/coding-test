#4-2. 랜선자르기
import sys
sys.stdin = open("in1.txt", "r")

def line_count(len) :
    count = 0
    for i in arr :
        count += (i//2)
    return count

k, n = map(int, input().split())
arr = []

for i in range(k) :
    arr.append(int(input()))    #값 저장
arr.sort()                      #정렬
print(arr)

lt = 1
rt = arr[-1]
answer = 0

while lt <= rt :
    mid = (lt + rt) // 2
    if line_count(mid) >= n :   #찾으려는 값보다 mid가 같거나, 크면
        answer = mid
        lt = mid + 1            #lt 조정
    else :                      #찾으려는 값보다 mid가 작으면
        rt = mid - 1            #rt 조정
print(answer)