import sys
sys.stdin=open("in0.txt", "r")

def DFS(L, start, sum) :
    global count
    if L == k :
        if sum % m == 0 :
            count += 1
    else :
        for i in range(start, n) :
            DFS(L+1, i+1, sum + arr[i])

n, k = map(int, input().split())
arr = list(map(int, input().split()))
m = int(input())
count = 0
print(n, k)
print(arr)

DFS(0, 0, 0)

print(count)