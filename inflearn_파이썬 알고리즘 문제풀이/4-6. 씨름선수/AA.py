#4-6 씨름선수(그리디)
import sys
#sys.stdin = open("in5.txt", "r")
n = int(input())
spac = []
largest = 0
count = 0

for i in range(n) :
    height, weight = map(int, input().split())
    spac.append((height, weight))
spac.sort(reverse=True)

for height, weight in spac : 
    if largest <= weight :
        largest = weight    #몸무게 최대값 갱신
        count += 1          
print(count)