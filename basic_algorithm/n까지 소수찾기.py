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

n = 45
print(findPrimes(45))
