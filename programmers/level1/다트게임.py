def bonus_point(bonus, num) :
    end = 0
    point = 1
    if bonus == "S" :
        end = 1
    elif bonus == "D" :
        end = 2
    else :
        end = 3
    
    for _ in range(1, end+1) :      #한번, 제곱, 세제곱 계산
        point *= num
    return int(point)
    
def option_point(option, num1, num2=None) :
    point = 0
    if option == "*" :
        num1 = num1 * 2
        if num2 is not None:
            num2 = num2 * 2
            return  (num1, num2)
        return  (num1)
    return (num1 * -1)
    
def solution(dartResult):
    answer = 0
    stack = []
    for i in range(len(dartResult)) :
        if dartResult[i].isdigit() :        #숫자인경우 스택에 추가
            if dartResult[i] == "0" and dartResult[i-1] == "1":
                stack[-1] = 10
                continue
            stack.append(int(dartResult[i]))    
        else :
            if dartResult[i] == "S" or dartResult[i] == "D" or dartResult[i] == "T" :     
                n = bonus_point(dartResult[i], stack.pop())
                stack.append(n)
            if dartResult[i] == "*":
                num1 = stack.pop()
                try:
                    (a, b) = option_point("*", num1, stack.pop())
                    stack.append(b)
                    stack.append(a)
                except:
                    (a) = option_point("*", num1)
                    stack.append(a)
            if dartResult[i] == "#" :
                (num1) =option_point("#", stack.pop()) 
                stack.append(num1)
    sum(stack)
    return sum(stack)