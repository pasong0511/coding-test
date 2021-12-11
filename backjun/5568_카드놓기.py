import sys
sys.stdin = open("input.txt", "r")

def DFS(L) :
    global count
    if L == m :
        if result not in visit: # 방문한적이 없는 경우 실행
            # for i in range(m) :         #
            #     print(result[i], end=" ")
            # print()
            visit.append(result.copy()) # copy를 쓴 이유는 배열은 포인터 개념이라 result값이 변하면 visit값 안에 들어가 있는 result 값도 변하기 때문에 배열 복사가 필요.
            count += 1  
    else :
        for i in range(n) :         #n : 4, i는 0, 1, 2, 3 만큼 돌음
            if check[i] == 0 :      #체크 변수가 0인것만 본다(1로 변경한건 방문하지 않음)
                check[i] = 1        #일단 방문하면 변경(0->1)
                result[L] = a[i]    #result[0], result[1]에 1로 a[i] 값 추가
                DFS(L+1)            #L 증가 가지 뻗음
                check[i] = 0        #방문 완료 했으면 다시 변경(1->0)

n = int(input())        #n개의 숫자
m = int(input())        #m개 뽑음
a = []                  #뽑아야할 숫자 카드
visit=[]    # 방문 기록할 변수
result = [0] * (m + 1)
check = [0] * (n + 1)
count = 0
for i in range(n) : 
    num = int(input())
    a.append(num)
# print("n : ", n, "m : ", m)
# print(a)

DFS(0)
print(count)