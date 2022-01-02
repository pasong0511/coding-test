#2021-12-15
#1단계 모의고사
def correct_answer(pattern, answers):
    count = 0
    for i in range(len(answers)) :              #정답 수만큼만 반복문 돌림
        if answers[i] == pattern[i%len(pattern)] :           #정답과, 찍은 문제 비교
            count += 1                          #정답인 경우 +1
    return count
    
def solution(answers):
    pattern = [[1, 2, 3, 4, 5],                  #사람 1 패턴: people[0]
              [2, 1, 2, 3, 2, 4, 2, 5],          #사람 2 패턴: people[1]
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]    #사람 3 패턴: people[2]
    people = {}
    answer = []
    
    for i in range(3) :
        people[i+1] = correct_answer(pattern[i], answers)       #딕셔너리에 수포자 번호, 맞춘 값 입력
    
    print(people)
    
    return [k for k,v in people.items() if max(people.values()) == v]