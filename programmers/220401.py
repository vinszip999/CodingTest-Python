# 문자열 s의 길이가 4 혹은 6이고,
# 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
# 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

# <나의 풀이>
def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():  # 문자열에 숫자만 있는지 확인하는 함수
            answer = True
        else:
            answer = False
    else:
        answer = False

    return answer


s = "a234"
print(solution(s))


# <다른 사람의 풀이 1>
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)


print(alpha_string46("a234"))
print(alpha_string46("1234"))


# <다른 사람의 풀이 2>
def alpha_string46(s):
    return s.isdigit() and (len(s) == 4 or len(s) == 6)


print(alpha_string46("a234"))
print(alpha_string46("1234"))
