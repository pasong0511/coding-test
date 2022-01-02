import sys
sys.stdin = open("in0.txt")
def DFS(L, sum) :
    global answer
    if sum > T :
        return
    if L == k :
        if sum == T :
            answer += 1
    else:
        for i in range(count_num[L]+1):
            DFS(L+1, sum+(count_valuse[L]*i))

if __name__ == "__main__" :
    T = int(input())
    k = int(input())
    count_valuse = []
    count_num = []
    answer = 0
    for i in range(k) :
        a, b = map(int, input().split())
        count_valuse.append(a)
        count_num.append(b)

    DFS(0, 0)

    print(answer)