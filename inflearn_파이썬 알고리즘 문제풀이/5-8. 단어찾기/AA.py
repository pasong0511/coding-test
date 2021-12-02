import sys
sys.stdin = open("in1.txt", "r")
n = int(input())
poem = {}
word = ''

for i in range(n) :
    word = input()
    poem[word] = 0

for i in range(n-1) :
    word = input()
    poem[word] = 1
print(poem)

for key, value in poem.items():
    if value == 1:
        print(key)
