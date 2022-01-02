#약수 찾기
# 0으로 나누어 떨어지는 수는 n의 약수이다.
def divisors(n) :
    div = []
    for i in range(1, n+1) :
        if n % i == 0:
            div.append(i)
    return div

x = 25
div_x = divisors(x)
print(div_x)