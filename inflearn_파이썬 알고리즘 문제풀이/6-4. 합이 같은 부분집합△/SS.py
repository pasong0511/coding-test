import sys
sys.stdin=open("in0.txt", "r")
def DFS(L, sum):
    if sum > (total // 2) :
        return
    if L == n :
        if sum == (total - sum) :
            print("sum", sum, "YES")
            sys.exit(0)
    else :
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

if __name__=="__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    print(n, total)
    DFS(0, 0)