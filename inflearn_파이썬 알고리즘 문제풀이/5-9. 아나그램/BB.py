import sys
sys.stdin = open("in1.txt", "r")
str1 = input()
str2 = input()
dic1 = {}
dic2 = {}

print(str1)
print(str2)

for i in str1 :
    dic1[i] = dic1.get(i, 0) + 1 

for i in str2 :
    dic2[i] = dic2.get(i, 0) + 1

print(dic1)
print(dic2)

for key, value in dic1.items() :
    if dic1[key] != dic2[key] :
        print("NO")
        break
else :
    print("YES")

