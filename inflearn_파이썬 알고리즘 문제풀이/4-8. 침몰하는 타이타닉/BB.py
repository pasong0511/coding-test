#4-8 침몰하는 타이타닉(그리디)
import sys
from collections import deque
from typing import Counter
sys.stdin = open("in1.txt", "r")
n, limit = map(int, input().split())
weight = list(map(int, input().split()))
safe_boat = 0

weight.sort()
weight = deque(weight)

print(weight)

while weight : 
    if len(weight)==1 :
        safe_boat += 1
        break
    if weight[0] + weight[-1] > limit :
        print("초과", weight[0] + weight[-1], weight)
        
        safe_boat += 1
        weight.pop()
    else :
        print("미달", weight[0] + weight[-1], weight)
        safe_boat += 1
        weight.pop()
        weight.popleft()
print(safe_boat)