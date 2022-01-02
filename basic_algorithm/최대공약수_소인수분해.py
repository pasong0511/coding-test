#소인수 분해와 최대 공약수
#소인수 분해를 통해 최대 공약수 구하기 -> 공통인 소수들의 곱을 찾기
# 126=2*3*3*7, 150=2*3*5*5 (최대 공약수->2*3인 6이다.)

#소인수 분해 업그레이드 : 소수를 먼저 구해두지 않고, 1씩 증가 시켜서 소수 찾으면서 소인수분해
def factorize_upgrade(n) :
    factor = 2
    factors = []

    while (factor ** 2) <= n :      #루트 n까지만 확인 : 
        while (n % factor) == 0 :   #factor는 나머지가 0인 소수
            n = n // factor         #n의 몫을 다시 소수로 나눈다.
            factors.append(factor)
        factor += 1                 #소수를 증가시킨다
    if (n > 1) :                      #제일 마지막도 추가 
        factors.append(n)
    return factors

#공통인 약수 찾기
def commonFactors(n, m) :
    i = 0
    j = 0
    commons = []
    while i < len(n) and j < len(m) :
        if n[i] == m[j] :               #같은 경우 append
            commons.append(n[i])
            i += 1
            j += 1
        elif n[i] < m[j] :
            i += 1
        else :
            j += 1
    return commons

#최대 공약수 : x, y의 공통인 약수의 곱
def gcd(n, m) :
    f1 = factorize_upgrade(n)
    f2 = factorize_upgrade(m)
    factors = commonFactors(f1, f2)
    gcd = 1
    for i in factors :
        gcd *= i
    return gcd

x = 78696
y = 19332

f1 = factorize_upgrade(x)
f2 = factorize_upgrade(y)

print(x,"의 소인수분해",f1)
print(y,"의 소인수분해",f2)

cf = commonFactors(f1, f2)
print(x,y, "의 공통 약수",cf)

gcd_num = gcd(x, y)
print(x, y, "의 최대공약수",gcd_num)