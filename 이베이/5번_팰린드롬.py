def falindrom_check(sum) :
    #print("작업대상 : ", sum)
    for i in range(int(len(sum) / 2)) :
        if sum[i] == sum[-i-1] :              #i, -i 같으면 True
            continue
            #print("같아",sum[i],":",sum[-i-1])
        else :                              #i, -1 다르면 False
            #print(sum[i],":",sum[-i-1])
            #print("False")
            return False
    #print("True")
    return True

def pick(first, P) :
    sum1 = str(first + P)
    sum2 = str(P + first)
    
    sum1_check = falindrom_check(sum1)
    sum2_check = falindrom_check(sum2)

    #print("sum1 =>", sum1_check)
    #print("sum2 =>", sum2_check)

    if sum1_check or sum2_check :
        print("둘중 하나 트루이기 때문에 트루 반환함")
        return True
    else :
        print("둘다 팰스라서 둘다 팰스 반환")
        return False

def retry(P):
    if len(P) == 0:
        return True
    i = 0
    while True:
        if len(P) == 0:
            break
        print("-------0번째와", i,"번째 넘겨줌---------")
        check = pick(P[0], P[i])
        print(check)   #True, False 반환
        if check is False:
            i += 1
        if check is True:
            P = P[1:i] + P[i+1:]
            if retry(P) is True:
                return True
            i += 1
        if len(P) - 1 == i :
            return False
    return False
        

def solution(P):
    ans = []
    print(P)
    i = 1
    while True :
        if len(P) == 0:
            break
        print("-------0번째와", i,"번째 넘겨줌---------")
        check = pick(P[0], P[i])
        print(check)   #True, False 반환
        print(P)
        if check is True:
            ans.append(P[i])
            P = P[1:i] + P[i+1:]
            i = 1
            continue
        if len(P) - 1 == i :
            break
        i += 1
        
            
    #         if len(P) > 0:
    #             ans.append(P[i])
    #             ans.append(P.pop())
    #             p = p[0:i] + p[i+1]
    #             print("뽑아 낸 후",P)
    #     else :
    #         print("뽑아낼수없다")
    #     if len(P) == 0 :
    #         ans.append(P[i])
    # print(ans)
    return ans



# quiz = ["11","111","11","211"]
# quiz_answer = ["111","211"]

quiz = ["21","123","111","11"] 
quiz_answer = ["123"]

if solution(quiz) == quiz_answer :
    print("★★★★5번 문제 정답★★★★")
else :
    print("★★★★5번 문제 틀림★★★★")