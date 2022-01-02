# - 최소 공배수(LCM) = GCD * a * b
# - 최소 공배수 = A * B / 최대공약수
# lcm = (a*b) / gcd
# gcd = (a*b) / lcm

from math import gcd

def lcm(x, y) :
    return x * y // gcd(x, y)

def solution(arr):
    
    answer = 0
    print(arr)
    
    while True :
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]
    return answer

print(solution([2,6,8,14]))