def isPrime(n) :
    for i in range(2, n) :
        if n % i == 0 :         #나누어 떨어지는 수가 있으면 소수가 아니다.
            return False
    return True

#n까지의 수에서 소수 찾기
def findPrimes(n) :
    primes = []
    for i in range(2, n+1) :
        if isPrime(i) :
            primes.append(i)
    return primes

#소인수분해 1(정석) : n보다 작은 소수를 먼저 찾아서 n을 나누어 떨어질때까지 나눠본다.
def factorize(n) :
    factors = []
    primes = findPrimes(n)      #2부터 n전까지 소수 리스트 찾기
    print(primes)

    for i in primes :           #2부터 n전까지 소수 리스트로 b나눠서 나누어 떨어진 목록 찾기
        while n % i == 0 :
            factors.append(i)
            n = n // i          #몫을 다시 소수로 나누기
    return factors

#소인수 분해 업그레이드 : 소수를 먼저 구해두지 않고, 1씩 증가 시켜서 소수 찾으면서 소인수분해
def factorize_upgrade(n) :
    factor = 2
    factors = []

    while (factor ** 2) <= n :      #루트 n까지만 확인 : 
        while (n % factor) == 0 :   #factor는 나머지가 0인 소수
            n = n // factor         #n의 몫을 다시 소수로 나눈다.
            factors.append(factor)
        factor += 1                 #소수를 증가시킨다
    if n > 1 :                      #제일 마지막도 추가 
        factors.append(n)
    return factors

n = 45
factor_list = factorize(n)
factor_list2 = factorize_upgrade(n)
print(factor_list)
print(factor_list2)