#그리디 : 모험가 길드
data = [2, 3, 1, 2, 2]
data.sort()

result = 0              #총 그룹 수
count = 0               #현재 그룹에 포함된 모험가 수

for i in data :         #i = 공포도
    count += 1          #현재 그룹에 해당 모험가를 포함시킨다.
    if count >= i:      #현재 그룹에 포함된 모험가 수와 현재의 공포도가 크거나 같으면 그룹 결설
        result += 1     #그룹 수 증가
        count = 0       #현재 그룹에 포함된 모험가의 수 초기화
print(result)