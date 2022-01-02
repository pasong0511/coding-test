#약수 찾기
def divisors(n) :
    div = []
    for i in range(1, n+1) :
        if n % i == 0:
            div.append(i)
    return div

#최통 약수 : 약수 중에서 공통인 수
def commons(n, m) :
    comm = []
    for i in n :
        if i in m :
            comm.append(i)
    return comm

#최대 공약수 : 공통인 약수 중에서 제일 큰 약수
def gcd(n, m) :
    div_n = divisors(n)             #n의 약수 모두 구하기
    div_m = divisors(m)             #m의 약수 모두 구하기
    comm = commons(div_n, div_m)    #공통인 약수 찾기
    return comm[len(comm)-1]        #제일 마지막에 있는 약수가 최대 공약수

x = 25
y = 65
div_x = divisors(x)
div_y = divisors(y)
print(div_x)
print(div_y)

comm = commons(div_x, div_y)
print(comm)

g = gcd(x, y)
print("최대공약수는", g)