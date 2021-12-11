#5-4 후위식연산(자료구조-스택)
import sys
sys.stdin = open("in1.txt", "r")
postfix = input()
print(postfix)

stack = []      #스택 저장용
num1 = 0
num2 = 0

for i in range(len(postfix)) :
    if postfix[i].isdigit() == True:            #postfix[i]가 숫자이면 스택에 push
        stack.append(int(postfix[i]))
        print(stack)
        continue 
    if stack and postfix[i].isdigit != True :   #postfix[i]가 연산자이면 2개 숫자 뽑아서 연산
        print(postfix[i])
        if postfix[i] == "+" :
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.append(num2 + num1)
        elif postfix[i] == "-" :
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.append(num2 - num1)
        elif postfix[i] == "*" :
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.append(num2 * num1)
        elif postfix[i] == "/" :
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.append(num2 / num1)

print(stack)