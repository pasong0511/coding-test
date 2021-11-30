#2021-11-30
#1단계_K번째 수
def solution(array, commands): 
    answer = []
    # 1. 자르기
    for i in range(len(commands)) :
        temp = []
        for j in range(commands[i][0], commands[i][1]+1) :
            temp.append(array[j-1])
            # 2. 정렬
            temp.sort()
        # 3. k번째 수 선택하여 리스트 저장
        answer.append(temp[commands[i][2]-1])               
    return answer

# #반복문 하나 쓰고 찾기
# def solution(array, commands): 
#     answer = []
#     for idx in range(len(commands)) :
#         i = commands[idx][0]
#         j = commands[idx][1]
#         k = commands[idx][2]
        
#         sort_array = sorted(array[i-1:j]) #자르기 및 정렬
#         answer.append(sort_array[k-1])    #k번째 수 찾기
        
#     return answer