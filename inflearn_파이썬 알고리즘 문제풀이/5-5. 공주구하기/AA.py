#5-5 공주구하기(자료구조-큐)
import sys
from collections import deque
sys.stdin = open("in0.txt", "r")
n, pick = map(int, input().split())
prince = deque(list(range(1, n+1)))

count = 1
#print("왕자 모임", prince, pick,"번")

while len(prince) > 1 :                 #왕자 디큐가 1될때까지 반복
    count += 1                          #pick 번째를 추리기 위한 카운트 변수
    prince.append(prince.popleft())     #pick 번째 아니면 디큐에 다시 넣어줌
    if count == pick :                  #pick 번째이면 pop
        none_prince = prince.popleft()
        count = 1                       #다시 pick 번째를 찾기 위해서 초기회
print(prince[0])