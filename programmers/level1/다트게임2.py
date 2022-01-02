def bonus_point(bonus, num) :
    point = 0
    if bonus == "S" :
        point = num ** 1
    elif bonus == "D" :
        point = num ** 2
    else :
        point = num ** 3
    return int(point)
    
def option_star(num1, num2=None) :
    num1 = num1 * 2
    if num2 is not None:
        num2 = num2 * 2
        return (num1, num2)
    return (num1)

def option_shap(num1) :
    return (num1 * -1)

def solution(dartResult):
    answer = 0
    stack = []
    for i in range(len(dartResult)) :
        if dartResult[i].isdigit() :            #숫자인경우 스택에 추가
            if dartResult[i] == "0" and dartResult[i-1] == "1":     #0이 확인되고 그 전에 1이 있으면
                stack.pop()                     #먼저 들어간 1 pop()
                stack.append(10)                #10 추가
                continue
            stack.append(int(dartResult[i]))    #숫자 스택에 추가     
        else :                                  #문자인 경우 종류 찾기
            if dartResult[i] in ["S", "D", "T"] :     
                stack.append(bonus_point(dartResult[i], stack.pop()))
            if dartResult[i] == "*":
                num1 = stack.pop()
                try:
                    (a, b) = option_star(num1, stack.pop()) #해당 점수와 바로 전에 얻은 점수
                    stack.append(b)                         #pop해서 stack에 추가
                    stack.append(a)
                except:           
                    stack.append(option_star(num1))         #해당 점수만 계산
            if dartResult[i] == "#" :
                stack.append(option_shap(stack.pop()))
    sum(stack)
    return sum(stack)