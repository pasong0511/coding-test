import sys
sys.stdin = open("in0.txt", "r")
num = int(input())
print(num)

def binary_transform(x) :
    if x == 0:
        return
    else : 
        binary_transform(x // 2)
        print( x % 2 , end = "")

binary_transform(num)
