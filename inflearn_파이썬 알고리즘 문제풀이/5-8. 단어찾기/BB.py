import sys
sys.stdin = open("in2.txt", "r")
n = int(input())
dic = {}

for i in range(n) :
    word = input()
    dic[word] = 0
print(dic)

for i in range(n-1) :
    word = input()
    dic[word] = 1
print(dic)

for key, value in dic.items() :
    if value == 0 :
        print(key)
        break
