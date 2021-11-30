#2021-11-29
#1단계 전화번호 목록
#딕셔너리 이용
def solution(phone_book):
    hash_map = {}
    #1. 해쉬 맵을 만든다.
    for i in range(len(phone_book)):
        hash_map[phone_book[i]] = 1
    
    print(hash_map)
    
    #2. 접두어가 해쉬맵에 있는지 확인한다.
    for i in phone_book :
        jubdoo = ''
        for j in i : 
            jubdoo += j
            # 3. 접두어를 찾아야한다.(기존 번호와 같은 경우는 제외)
            # 접두어를 찾아야하기 때문에 기존 i와 같은 수를 hash_map에서 찾으면 x
            if jubdoo in hash_map and jubdoo != i:
                return False
    return True

#startswith() 이용
#def solution(phone_book):
#    phone_book.sort()
#    for i in range(len(phone_book)-1) :
#        if phone_book[i+1].startswith(phone_book[i]):
#            return False
#    return True

# 효율성 오류
#def solution(phone_book):
#    phone_book.sort()
#    for i in range(len(phone_book)) :
#        prefix = phone_book[i]
#        prefix_len = len(prefix)
#        for j in range(i+1, len(phone_book)) : 
#            if prefix in phone_book[j][0:prefix_len] :
#                return False
#    return True