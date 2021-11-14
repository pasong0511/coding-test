#2021-11-14
def solution(lottos, win_nums):
    answer = []
    count = 0
    zero = 0
    print("구입",lottos)
    print("당첨",win_nums)
    
    zero = lottos.count(0)
    
    for i in win_nums :
        for j in lottos : 
            if i == j :
                count += 1
    print("개수 : ", count)
    print("0개수 : ", zero)
    
    answer.append(rank(count+zero))
    answer.append(rank(count))
        
    print(answer)
    
    return answer

def rank(num):
    if num == 0:
        return 6
    return 7-num