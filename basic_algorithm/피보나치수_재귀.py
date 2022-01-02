#피보나치 수 : F(n) = F(n-1) + F(n-2) 가 적용되는 수
#F(0) = 0, F(1) = 1일 때
#F(2) = F(0) + F(1) = 0 + 1 = 1
#F(3) = F(1) + F(2) = 1 + 1 = 2
#F(4) = F(2) + F(3) = 1 + 2 = 3
#F(5) = F(3) + F(4) = 2 + 3 = 5
# 재귀사용 O(2^n)
def fibonacci_numbers(n) :
    current = 0
    next = 1
    if n <= 2:
        return 1
    return fibonacci_numbers(n-1) + fibonacci_numbers(n-2)

print(fibonacci_numbers(3))