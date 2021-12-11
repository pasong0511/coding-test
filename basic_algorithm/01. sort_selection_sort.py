# -*- coding: utf-8 -*-
# 선택정렬
# 한번 가장 작은것을 선택해서 제일 앞에 보냄
# 시간복잡도 : O(N * N) => O(N^2)

arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
i = 0
j = 0
index = 0
temp = 0

print("전",arr)

for i in range(len(arr)-1) :
    min = 999
    for j in range(i, len(arr)) :
        if min > arr[j]:
            min = arr[j]
            index = j
    temp = arr[i]
    arr[i] = arr[index]
    arr[index] = temp
    print("과정", arr)
    
print("후", arr)