import sys
sys.stdin=open("in1.txt", "r")
def DFS(v):
    pass

def DFS(v) :
    global count, path
    if v == n :             #버텍스 끝에 도달
        count += 1
        for i in path :
            print(i, end = " ")
        print()
    else :
        for i in range(1, n+1) :
            if g[v][i] == 1 and check[i] == 0 :
                check[i] = 1                        #i는 방문완료하여 체크리스트 1로 변경
                path.append(i )
                DFS(i)                              #i 버텍스 방문
                check[i] = 0                        #빽 하면서 다시 체크리스트 0으로 변경
                path.pop()


if __name__=="__main__":
    n, m = map(int, input().split())
    g = [[0] * (n+1) for _ in range(n+1)]
    check = [0] * (n+1)
    
    for i in range(m) :
        a, b = map(int, input().split())
        g[a][b] = 1
    
    count = 0
    check[1] = 1
    path = []
    path.append(1)
    DFS(1)
    print(count)