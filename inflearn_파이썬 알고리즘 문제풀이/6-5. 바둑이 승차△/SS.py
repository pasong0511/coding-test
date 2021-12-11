import sys
sys.stdin=open("in0.txt", "r")
def DFS(L, sum, tsum):
    global result
    if sum + (total-tsum) < result:
        return
    if L > n-1 : 
        if sum <= max_weight:
            if sum > result :
                result = sum        
                return
    else :
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum)

if __name__=="__main__":
    max_weight, n = map(int, input().split())
    result = 0
    a = []
    for i in range(n) :
        kg = int(input())
        a.append(kg)
    total = sum(a)
    # print(max_weight, n)
    # print(a)
    DFS(0, 0, 0)
    print(result)