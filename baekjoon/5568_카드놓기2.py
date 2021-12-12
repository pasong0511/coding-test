#동건 제작
import sys
#sys.stdin = open("input.txt", "r")

def test(arr, detph=[]):
    if len(detph) == m-1:
        for i in arr:
            result = "".join(detph) + str(i)
            if result in chk:
                continue
            chk.append(result)
            #print(result)
    else:
        size = len(arr)
        for index in range(size):
            test(arr[0:index]+arr[index+1:size], detph + [str(arr[index])])

n = int(input())
m = int(input())
a = []
chk = []
for i in range(n) : 
    num = int(input())
    a.append(num)

test(a, [])


print(len(chk))