#소수
#1보다 큰 자연수 중에서 약수가 1과 자기 자신뿐인 수
#약수의 개수가 2개뿐인 수
number = [1, 1023, 2333, 2337, 8191, 10867, 10869]

def isPrime(n) :
    for i in range(2, n) :
        if n % i == 0 :         #나누어 떨어지는 수가 있으면 소수가 아니다.
            return False
    return True

for n in number :
    if isPrime(n) :
        print(n, "은 소수입니다.")
    else : 
        print(n, "은 합성수 입니다.")