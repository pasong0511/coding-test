#소수
#소수의 배수는 소수가 아니다.
#소수의 배수들을 False로 변경해서 True인 소수만 찾기
def isPrime_list(n):
    sieve = [False, False] + [True] * (n-1)
    primes = []

    for i in range(2, n+1) :
        if sieve[i] == True :
            primes.append(i)
        for j in range(i*2, n+1, i) :       #i의 배수는 False
            sieve[j] = False
    
    return primes

n = 100
print(isPrime_list(n))

#소수 목록 산출