def solution(n, lost, reserve):
    answer = 0
    new_lost = []
    for i in lost:                  #잃어버린 학생이 여유분 있는지 체크
        if i not in reserve:
            new_lost.append(i)
        else:
            reserve.remove(i)

    reserve.sort()
    
    for i in range(len(reserve)) :
        if reserve[i]-1 in new_lost :
            new_lost.remove(reserve[i]-1)
        elif reserve[i]+1 in new_lost :
            new_lost.remove(reserve[i]+1)
    
    print(n - len(new_lost))
    return n - len(new_lost)