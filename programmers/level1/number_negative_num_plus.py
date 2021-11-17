#2021-11-16
def solution(absolutes, signs):
    answer = []
    for a, b in zip(absolutes, signs):
        if b == False :
            answer.append(a*-1)
        else :
            answer.append(a)
    return sum(answer)