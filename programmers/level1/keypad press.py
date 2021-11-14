#2021-11-14
def solution(numbers, hand):
    answer = ''
    yeypad = [[1,  2,  3],
              [4,  5,  6],
              [7,  8,  9],
              ["*",0,"#"]]
    point = [["L",  "-",  "R"],
             ["L",  "-",  "R"],
             ["L",  "-",  "R"],
             ["*",  "-", "#"]]
    now_right = [3, 0]
    now_left = [3, 2]
    distance_right = 0
    distance_left = 0
    
    for i in range(len(numbers)) :
        for x in range(4) :
            for y in range(3):
                if numbers[i] == yeypad[x][y]:  #numbers에 있는 숫자 이중배열에서 찾기                  
                    if point[x][y] == "R":      #찾은 numbers의 좌표 이용해서 point R 찾기
                        now_right[0] = x
                        now_right[1] = y
                        answer += point[x][y]
                    elif point[x][y] == "L":    #찾은 numbers의 좌표 이용해서 point L 찾기
                        now_left[0] = x
                        now_left[1] = y
                        answer += point[x][y]
                    else :                      #가운데 열 2, 5, 8, 0 찾기
                        distance_right = distance(now_right[0], x, now_right[1], y) #중간에 위치한 숫자와 오른쪽 차이
                        distance_left = distance(now_left[0], x, now_left[1], y)    #중간에 위치한 숫자와 왼쪽 차이
                        if distance_right < distance_left :
                            now_right[0] = x    #오른쪽 좌표 갱신
                            now_right[1] = y
                            answer += "R"
                        elif distance_right > distance_left :
                            now_left[0] = x     #왼쪽 좌표 갱신
                            now_left[1] = y
                            answer += "L"
                        else :
                            if hand == "right":
                                now_right[0] = x    #오른쪽 좌표 갱신
                                now_right[1] = y
                                answer += "R"
                            else :
                                now_left[0] = x     #왼쪽 좌표 갱신
                                now_left[1] = y
                                answer += "L"
    print(answer)
    return answer

#중간값 좌표와 오른쪽x, y좌표 / 중간값 좌표와 왼쪽x, y좌표를 절대값으로 더하여 거리 계산
def distance(x1, x2, y1, y2):
    distance_num = abs(x1-x2) + abs(y1-y2)
    return distance_num