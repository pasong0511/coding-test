# 제너레이터를 사용한 버전
# O(N)
def fibonacci_numbers(n):
    a, b = 1, 1
    for n in range(n):
        yield a
        a, b = b, a + b

for n in fibonacci_numbers(3):
    print(n)