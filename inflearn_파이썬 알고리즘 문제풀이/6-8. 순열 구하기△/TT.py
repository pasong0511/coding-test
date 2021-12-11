import sys
sys.stdin=open("in1.txt", "r")

def DFS(L) :
    if L == m:              #뽑은 n개보다 L이 큰 경우 종료
        for i in range(m) :
            print(result[i], end=" ")
        print()
        return
    else : 
        for i in range(1, n+1) :
            if check[i] == 0 :
                check[i] = 1
                result[L] = i
                DFS(L+1)
                check[i] = 0
            print("-----------")
    return

if __name__=="__main__":
    n, m=list(map(int, input().split()))
    result = [0] * m
    check = [0] * (n + 1)
    count = 0
    print(n, m)

    DFS(0)