#그리디 : 1이 될때까지
n = 25
k = 3
count_1 = 0
count_2 = 0

while n >= k:
    while n % k != 0 : 
        n = n - 1
        count_1 += 1
    n //= k
    count_2 += 1

while n > 1 :
    n = n - 1
    count_1 += 1

print("count_1 :", count_1)
print("count_2 : ", count_2)