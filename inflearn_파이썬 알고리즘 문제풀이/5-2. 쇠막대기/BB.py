#5-2 쇠막대기(스택)
#by.dong
import sys
sys.stdin = open("in5.txt", "r")
cuting = input()
stack = []
sum = 0
print(cuting)

for i in range(len(cuting)) : 
    if cuting[i] == "(" :
        stack.append(cuting[i])
        continue
    stack.pop()
    if cuting[i-1] == ")":
        sum += 1    
        continue
    sum += len(stack)

print(sum)
print(stack)