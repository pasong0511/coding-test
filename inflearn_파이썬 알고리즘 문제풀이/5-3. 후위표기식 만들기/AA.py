#5-3 후위표기식 만들기(자료구조-스택)
import sys
sys.stdin = open("in4.txt", "r")
infix = input()
print(infix)
stack = []      #스택 저장용
postifx = []    #출력용

#우선순위 1순위 : * /
#우선순위 2순위 : + -

for i in  range(len(infix)) : 
    print("인덱스 [", i, "] :" , infix[i])
    if infix[i].isdigit() :             #숫자인 경우 출력
        postifx.append(infix[i])
        print("postifx 현황 : ", postifx)
    else :
        if infix[i] == "(" :            #여는 괄호 만났을때 스택에 넣음
            stack.append(infix[i])
            print("스택 현황 : ",stack)
        elif infix[i] == "*" or infix[i] == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/") :    #현재[i] = *, / 이고 스택[-1] = *, /
                postifx.append(stack.pop())                             #기존 스택에 들어있는 * or / pop
            stack.append(infix[i])                                      #현재[i] push
            print("스택 현황 : ",stack)
        elif infix[i] == "+" or infix[i] == "-":
            while stack and stack[-1] != "(" :
                postifx.append(stack.pop())
            stack.append(infix[i])
            print("스택 현황 : ", stack)   
        elif infix[i] == ")" :
            while stack and stack[-1] != "(" :
                postifx.append(stack.pop())
            stack.pop()     #괄호 ( 까지 뽑아줌
            print("스택 현황 : ",stack)

while stack :
    postifx.append(stack.pop())

print(postifx)
anwear = "".join(map(str, postifx))
print(anwear)
    # if infix[i].isdigit() :             #숫자인 경우 출력
    #     postifx.append(infix[i])
    # else :                              #연산자인 경우 스택에 넣는다.     
    #     if infix[i] == "*" or infix[i] == "/" :   
    #         postifx.append(infix[i])
    #     elif infix[i] == "+" or infix[i] == "-" :     #연산자를 스택에 넣을 때는 스택안에 자기보다 우선순위가 같거나, 높은것은 pop, 자신을 스택에 넣음
    #         i = len(stack)
    #         while stack and i >= len(stack) :
    #             if stack[i] == "*" or stack[i] == "/" :
    #                 stack.pop()
    #                 i -= 1
    #             stack.append(infix[i])

    #     elif infix[i] == "(" :            #여는 괄호 만났을때 스택에 넣음
    #         stack.append(infix[i])
    #     elif infix[i] == ")" :          #indix[i]가 )를 만나면 스택의 (까지 pop
    #         while stack and stack[-1] != "(" :
    #             postifx.append(stack.pop())



# sys.stdin = open("in0.txt", "r")
# num, remove_count = map(int, input().split())
# num = list(map(int, str(num)))

# print(num)
# print(remove_count)


# def solution(num, remove_count):
#     stack = []
#     i = 0
#     while remove_count > 0:                                 #remove_count가 0이 되기 전까지 반복
#         if len(num) <= i:
#             break
#         if len(stack) > 0 and stack[-1] < num[i] :         #이미 들어간 스택끝과 i값 비교해서 작은경우 스택 pop
#             stack.pop()
#             remove_count -= 1
#             print("remove_count", remove_count)
#         else:
#             stack.append(num[i])
#             i+=1
    
#     if remove_count > 0:
#         return stack[:-remove_count]
#     return stack

# print("".join(map(str, solution(num, remove_count))))

# #5-2 쇠막대기(스택)
# #by.dong
# import sys
# sys.stdin = open("in5.txt", "r")
# cuting = input()
# stack = []
# sum = 0
# print(cuting)

# for i in range(len(cuting)) : 
#     if cuting[i] == "(" :
#         stack.append(cuting[i])
#         continue
#     stack.pop()
#     if cuting[i-1] == ")":
#         sum += 1    
#         continue
#     sum += len(stack)

# print(sum)
# print(stack)