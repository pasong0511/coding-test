import sys
sys.stdin=open("in1.txt", "r")
def DFS(L, s):
    if L == m :
        for i in range(m) :
            print(result[i], end=" ")
        print()
    else : 
        for i in range(s, n+1) :
            result[L] = i
            DFS(L+1, i+1)

n, m = map(int, input().split())
print("n:", n,"m:", m)
result = [0] * m
DFS(0, 1)