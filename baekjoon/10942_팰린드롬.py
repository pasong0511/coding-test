import sys
sys.stdin = open("input.txt", "r")

def check_palindrome(job_num, cnt) :
    for i in range(cnt) :
        if job_num[i] != job_num[-i-1] :
            return False
    return True           

def cut_number(num_list, s, e) :
    job_num = num_list[s-1:e]
    cnt = int(len(job_num) / 2)
    return check_palindrome(job_num,cnt)

num = int(input())
num_list = list(map(int, input().split(" ")))
count = int(input())

for question in range(count):
    s, e = map(int, input().split(" "))
    if cut_number(num_list, s, e):
        print("1")
        continue
    print("0")