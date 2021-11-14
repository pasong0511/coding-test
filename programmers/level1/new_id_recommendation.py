#2021-11-14
import re

def solution(new_id):
    answer = ''
    answer = modify_lower(new_id)
    answer = remove_none_string(answer)
    answer = modify_tow_dot(answer)
    answer = modify_start_end_dot(answer)
    answer = add_a(answer)
    answer = remove_over_len(answer)
    answer = modify_start_end_dot(answer)
    answer = add_small_len(answer)
    return answer

#1 : 대문자 -> 소문자
def modify_lower(str):
    return str.lower()

#2 : 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
def remove_none_string(str):
    return re.compile("([^a-z0-9-_.])").sub("", str)

#3 : 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
def modify_tow_dot(str):
    return re.compile("(\.+)").sub(".", str)

#4 : 마침표(.)가 처음이나 끝에 위치한다면 제거
def modify_start_end_dot(str):
    return re.compile("(^\.|\.$)").sub("", str)

#5 : 빈 문자열이라면, new_id에 "a"를 대입
def add_a(str):
    if len(str) == 0:
        return "a"
    return str

#6 : 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
def remove_over_len(str):
    return str[0:15]

#7 : 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙
def add_small_len(str):
    if len(str) >= 3 :
        return str;
    return add_small_len(str + str[-1])