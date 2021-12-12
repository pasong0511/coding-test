import sys
sys.stdin = open("input.txt", "r")

def DFS(L, s, arr, n) :
    if L == pick :
        for i in range(6) :
            print(result[i], end=" ")
        print()
    else :
        for i in range(s, n) :
            if check[i] == 0 :
                check[i] = 1
                result[L] = arr[i]
                DFS(L+1, i+1, arr, n)
                check[i] = 0

while True:
    lotto = list(map(int, input().split()))
    pick = 6
    result = [0] * pick
    check = [0] * lotto[0]
    DFS(0, 0, lotto[1:], lotto[0])
    if lotto[0] == 0:
        break
    print()
