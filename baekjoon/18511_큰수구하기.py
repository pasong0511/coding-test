import sys
sys.stdin = open("input.txt", "r")

def DFS(L, result) : 
    m = len(result)
    if L == m :
        s = ''
        for i in range(m) :
            s += str(result[i])
        if n >= int(s) :                #n보다 작고, max_num보다 큰 값
            return int(s)

    else :
        for i in range(k) :
            result[L] = arr[i]              #result[i]에 값 넣기
            max_num = DFS(L+1, result)       #다음 가지로 뻗기
            if max_num is not None:         #max값일때 max_num 반환
                return max_num
    return None                             #max값이 아닌 경우 None 값 반환

n, k = map(int, input().split())
num_size = len(str(n))
arr = list(map(int, input().split()))
arr.sort(reverse=True)                      #큰 숫자부터 찾기

data = DFS(0,  [0] * num_size)

if(data is None):                           #1000이면 3자리 숫자 나와야하므로 None이면 3자리수 계산
    data = DFS(0,  [0] * (num_size-1))
print(data)