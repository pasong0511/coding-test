import sys
sys.stdin=open("input.txt", "r")
def DFS(L, sum):
    if L == m :
    
    else :
        for i in range(1, n+1) :
            res[L] = i
            DFS(L+1)

if __name__=="__main__":
    n, m=map(int, input().split())
    res = [0] * m
    count = 0
    DFS(0)
    print(0)

    