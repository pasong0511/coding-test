import sys
import collections
#sys.stdin = open("in1.txt", "r")

str1 = input()
str2 = input()
answer = 0

answer = collections.Counter(str1) - collections.Counter(str2)

if not answer :
    print("YES")
else :
    print("NO")
