#2021-11-17
#1단계_완주하지 못한 선주
#해시함수 이용
def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    
    for i in participant :
        hashDict[hash(i)] = i
        sumHash += hash(i)
    print(hashDict)
    print(sumHash)
    
    for i in completion:
        sumHash -= hash(i)
        print(sumHash)
    
    return hashDict[sumHash]
    
#정렬 이용
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#    
#     #len 만큼 돌면서 정렬된 참가자와, 완주자의 순서 비교해서 다를 경우 리턴
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#        
#     #전부 다 돌아도 없는 경우 마지막 주자가 미완주
#     return participant[-1]