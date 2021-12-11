import sys
#sys.stdin=open("in1.txt", "r")

def DFS(L, sum) :
    global count    #최소값 샐 변수(count)
    if L>=count:
        return
    if sum > m:     #sum이 m 보다 클때 종료
        return
    if sum == m :   #합계가 15일때 종료
        if L < count :  #최소값 갱신
            count = L
    else :          #다음 플로우로 넘어감
        for i in range(n) :
            DFS(L+1, sum+a[i])   
        # DFS(L+1, sum + a[L])

if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    m = int(input())
    count = 2147000000
    print(n, a, m)
    a.sort(reverse=True)
    DFS(0, 0)
    print(count)