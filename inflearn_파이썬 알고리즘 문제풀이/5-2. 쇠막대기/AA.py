#5-2 쇠막대기(스택)
import sys
#sys.stdin = open("in5.txt", "r")
cuting = input()
stack = []
sum = 0
print(cuting)

for i in range(len(cuting)) : 
    if cuting[i] == "(" :
        stack.append(cuting[i])
    elif cuting[i] == ")" and cuting[i-1] == ")" and stack[-1] == "(":
        sum += 1
        stack.pop()
    else :                  #cuting[i] == ")" and stack[-1] == "(" :
        stack.pop()
        sum += len(stack)

print(sum)
print(stack)