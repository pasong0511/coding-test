#2021-11-16
def solution(a, b):
    answer = []
    for a, b in zip(a, b):
        answer.append(a*b)
    return sum(answer)

# def solution(a, b):
#     answer = 0
#     for i in range(len(a)):
#         answer += a[i]*b[i]
#     return answer