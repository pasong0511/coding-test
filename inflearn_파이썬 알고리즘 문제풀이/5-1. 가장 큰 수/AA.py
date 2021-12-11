#5-1 가장 큰 수(자료구조-스택)
import sys
sys.stdin = open("in0.txt", "r")
num, remove_count = map(int, input().split())
num = list(map(int, str(num)))

print(num)
print(remove_count)


def solution(num, remove_count):
    stack = []
    i = 0
    while remove_count > 0:                                 #remove_count가 0이 되기 전까지 반복
        if len(num) <= i:
            break
        if len(stack) > 0 and stack[-1] < num[i] :         #이미 들어간 스택끝과 i값 비교해서 작은경우 스택 pop
            stack.pop()
            remove_count -= 1
            print("remove_count", remove_count)
        else:
            stack.append(num[i])
            i+=1
    
    if remove_count > 0:
        return stack[:-remove_count]
    return stack

print("".join(map(str, solution(num, remove_count))))