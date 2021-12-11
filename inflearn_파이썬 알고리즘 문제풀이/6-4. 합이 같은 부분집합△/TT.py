import sys
sys.stdin=open("in1.txt", "r")
def DFS(L, sum):
    print("L", L, "sum", sum)
    if sum > total // 2 :           #sum이 전체 리스트 //2 보다 크기 전까지만 수행
        return

    if L == n :                     #인덱스(레벨) 다 돌면 끝
        if sum == (total - sum) :   #전체에서 내가 만든 부분집합의 합을 빼주면 반대편 부분집합의 합이 계산됨
            print("YES")            #같을 경우 YES 출력
            sys.exit(0)             #프로그램 자체 종료

    else : 
        DFS(L+1, sum+a[L])          #레벨 1씩 증가, sum에 a[L]이 가르키는 값 더하기
        DFS(L+1, sum)               #이번 원소는 더하지 않고 그 전 값 그대로 가겠다.(사용하지 않음)


if __name__=="__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)                  #리스트안에 들어가 있는거 전체의 합
    DFS(0, 0)                       #0 : 인덱스 시작 번호, 0: 인덱스 값의 합
    print("NO")