#4-9 증가하는수열 만들기(그리디)
import sys
sys.stdin = open("in5.txt", "r")
from collections import deque
n = int(input())
arr = list(map(int, input().split()))
arr = deque(arr)
increase_nums = []
direction = ""

if arr[0] <= arr[-1] :
    increase_nums.append(arr[0])
    arr.popleft()
    direction = "L"
else : 
    increase_nums.append(arr[-1])
    arr.pop()
    direction = "R"

for _ in range(1, len(arr)) :
    if increase_nums[-1] < arr[0] and increase_nums[-1] < arr[-1] :    #이전값과 양 끝값 동시에 더 큰지 비교(둘다 증가 값인경우)
        if arr[0] < arr[-1] : #작은거 먼저 pop
            increase_nums.append(arr.popleft())
            direction += "L"
        else :
            increase_nums.append(arr.pop())
            direction += "R"

    elif increase_nums[-1] < arr[0] :
            increase_nums.append(arr.popleft())
            direction += "L"
    elif increase_nums[-1] < arr[-1] :
            increase_nums.append(arr.pop())
            direction += "R"
    else :
        break

print(len(increase_nums))
print(direction)