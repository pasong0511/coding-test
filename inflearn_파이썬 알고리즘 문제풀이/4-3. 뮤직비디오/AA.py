#4-3. 뮤직비디오
import sys
sys.stdin = open("in1.txt", "r")
n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(n, m)
print(arr)

lt = 1
rt = sum(arr)
max_time = max(arr)
answer = 0

def count_dvd(capacity b) :
    dvd_count = 1
    sum = 0
    for i in arr : 
        if sum + i > capacity :
            dvd_count += 1
            sum = i
        else :
            sum += i
    return dvd_count

while lt <= rt :
    mid = (lt + rt) // 2    #2. 중간 값 생성
    print("mid", mid)
    if max_time <= mid and count_dvd(mid) <= m :  #최대 시간 값이 mid 보다 크고 dvd개수가 m보다 작으면
        answer = mid
        rt = mid - 1        # 찾은 값이 mid값보 크면 dvd가 m개보다 커지므로 rt를 mid-1로 조정
        print("mid보다 작음","rt :",rt, "lt :", lt)
        print("answer",answer)
    else : 
        lt = mid + 1
        print("mid보다 큼음", "rt :",rt, "lt :", lt)
print(answer)