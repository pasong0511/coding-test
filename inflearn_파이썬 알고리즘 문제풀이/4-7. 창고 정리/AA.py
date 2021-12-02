#4-7 창고정리(그리디)
import sys
sys.stdin = open("in1.txt", "r")
n = int(input())
arr = list(map(int, input().split()))
repeat = int(input())
# minimum = 0
# maximum = 0

# minimum = min(arr)                      #초기 최대값, 최소값 저장
# maximum = max(arr)

# for i in range(repeat) : 
#     print(i,"회차")
#     print(arr)
#     if maximum <= max(arr) :            #현재 리스트(arr)에서 기존 맥시멈보다(maximum) 큰숫자 찾기(max(arr))
#         index = arr.index(max(arr))     #해당 큰 숫자 인덱스 찾기
#         print("최대값 찾음 : ", max(arr))
#         arr[index] -= 1
#         maximum = arr[index]            #1개 줄인 최대값 갱신

#     if minimum >= min(arr) :            #현재 리스트(arr)
#         index = arr.index(min(arr))
#         print("최소값 찾음 : ", min(arr))
#         arr[index] += 1
#         minimum = arr[index]

for i in range(repeat):
    maximum = max(arr)
    minimum = min(arr)

    maximum_index = arr.index(maximum)
    minimum_index = arr.index(minimum)

    arr[maximum_index]-=1
    arr[minimum_index]+=1


print(max(arr) - min(arr))