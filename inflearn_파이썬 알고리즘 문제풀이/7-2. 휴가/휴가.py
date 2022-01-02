import sys
sys.stdin = open("in0.txt", "r")

def DFS(L, sum) :
    global answer

    if L == n+1 :          #가지가 끝까지 뻗은 경우 중단
        if sum > answer :
            answer = sum
    else :
        if L+time[L] <= n+1 :       #L에 잡힌 상담 함
            DFS(L+time[L], sum+pay[L])
        DFS(L+1, sum)

if __name__ == "__main__" :
    n = int(input())

    time = [0]
    pay = [0]
    answer = -2147000000

    for _ in range(n) :
        a, b = map(int, input().split())
        time.append(a)
        pay.append(b)

    print(time)
    print(pay)

    DFS(1, 0)

    print(answer)