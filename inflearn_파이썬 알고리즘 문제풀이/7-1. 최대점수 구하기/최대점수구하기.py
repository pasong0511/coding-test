import sys
sys.stdin = open("in1.txt", "r")

def DFS(L, sum_score, sum_time) :
    global answer

    if sum_time > limit_time:            #sum_time이 limit_time보다 크거나 같아질때 가지뻗기 중지
        return
    if L == n :                         #레벨의 끝까지 도달
        if answer <= sum_score :        #최대 점수 갱신
            answer = sum_score
    else :
        DFS(L+1, sum_score+score[L], sum_time+time[L])   #가지뻗기 중 사용 O
        DFS(L+1, sum_score, sum_time)                   #가지뻗기 중 사용 안 함 X
        

if __name__ == "__main__" :
    n, limit_time = map(int, input().split())

    score = []
    time = []
    answer = -2147000000

    for i in range(n) :
        a, b = map(int, input().split())
        score.append(a)
        time.append(b)

    DFS(0, 0, 0)

print(answer)