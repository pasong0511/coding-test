# -*- coding: utf-8 -*-
# 버블정렬
# 옆에 있는 값과 비료해서 더 작은 값을 앞으로 보냄
# 시간복잡도 : N * (N+1) / 2 => O(N*N) => O(N^2)
# 실제는 버블정렬이 더 느리는데 이유는 바로 옆에 있는것을 매번 교환해주기 때문

arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
i = 0
j = 0
temp = 0

print("전",arr)

for i in range(len(arr)) :
    print("i:", i)
    for j in range(0, (len(arr)-1)-i) :
        if arr[j] > arr[j+1]:   #왼쪽에 있는 값이 더 크면
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
        print("j 과정 :", j,":",arr)
    
print("후", arr)