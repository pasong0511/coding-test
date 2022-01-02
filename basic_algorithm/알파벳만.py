def check_alpah(str_now) :      #알파벳만 추출하여 반환
    new_str = ''
    for char in str_now :
        if char.isalpha() :
            new_str += char
    return new_str

print(check_alpah("sdsds#@!^&#a!!@#!1211sDAS@!#AASCCASD"))