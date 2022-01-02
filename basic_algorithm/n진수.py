def convert_num(n, q) :                 #n의 숫자를 q진수로 변환 함수
    rev_base = ''
    while n > 0 :                       #변환 시작
        n, mod = divmod(n, q)
        rev_base += str(mod)            #거꾸로 출력
    return rev_base[::-1]

print(convert_num(78, 2))               #변환할 수, 진법(78은 2진수는 1001110)
print(convert_num(83, 2))               #변환할 수, 진법(83의 2진수는 1010011)