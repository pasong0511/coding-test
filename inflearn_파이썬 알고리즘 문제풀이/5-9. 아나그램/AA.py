import sys
sys.stdin = open("in1.txt", "r")
a = input()
b = input()
str1 = dict()
str2 = dict()

print(a, b)

for x in a :
    str1[x] = str1.get(x, 0) + 1
print(str1)

for i in str1.keys() :
    print(i)