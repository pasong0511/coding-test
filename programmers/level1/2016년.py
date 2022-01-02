def solution(a, b):
    answer = ''
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #1월부터 12월 까지 일 수
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    day_sum = 0
    
    #a월 b일은 1월 1일부터 몇일이 경과한 숫자인가?
    #n이 5인경우, 1:31일,2:29일,3:31일,4:30일
    for i in range(1, a) :
        day_sum += month[i]
    day_sum += b                    #n-1월까지의 일자 + n월의 일자
    
    for i in range(day_sum) :
        answer = week[i % len(week)]
    print(answer)
    return answer