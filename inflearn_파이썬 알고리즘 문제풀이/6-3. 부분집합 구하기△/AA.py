import sys
sys.stdin = open("input.txt", "t")

def DFS(v) :
    if v == n+1 :

    else : 
        check[v] = 1    #1이면 부분집합으로 사용
        DFS(v+1)
        check[v] = 0    #0이면 부분집합으로 사용하지 않음
        DFS(v+1)
        
if __name__ == "__main__" : 
    n = int(input())
    check = [0] * (n+1)
    DFS(1)