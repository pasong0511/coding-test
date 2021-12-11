# 삽입정렬
# 각 숫자를 적절한 위치에 삽입하기
# 앞에 있는 원소들은 이미 정렬되었다는 가정
# 선택, 버블과는 같은 시간복잡도이지만 실제는 더 빠름
# 시간복잡도 : O(N * N) => O(N^2)

arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
i = 0
j = 0
temp = 0

for i in range(len(arr)-1) :
    j = i
    while (arr[j] > arr[j + 1]) :   #왼쪽에 있는게 더 크면 위치교환
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j+1] = temp
        j = j - 1 
print(arr) 