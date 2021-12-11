import sys
sys.stdin = open("input.txt", "r")


def solution(num_string, n) : 
    global count
    sum = 0
    sum_string = []
    count += 1
    if n == 1 :
        if int(num_string[0]) % 3 == 0 :
            print(count-1)
            print("YES")
        else :
            print(count-1)
            print("NO")
        return

    for i in num_string : 
        sum += i                                #리스트 전체 더하기
    # print(sum)
    sum_string = list(map(int, str(sum)))       #리스트로 쪼갬
    sum_n = len(sum_string)
    # print(sum_string, sum_n)
    solution(sum_string, sum_n)

num_string = list(map(int, input()))
n = len(num_string)
count = 0
# print(num_string, n)

solution(num_string, n)