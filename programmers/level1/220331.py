'''
프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때,
전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.
'''


# <나의 풀이>
def solution(phone_number):
    answer = ''
    list = []
    for i in phone_number:
        list.append(i)
    list.reverse()  # list = [4, 4, 4, 4, 3, 3, 3, 3, 0, 1, 0]
    for j in range(4, len(list)):
        list[j] = '*'
    list.reverse()
    answer = ''.join(list)
    return answer

phone_number = "01033334444"
print(solution(phone_number))


# <다른 사람의 풀이 1>
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]

print("결과 : " + hide_numbers('01033334444'))


# <다른 사람의 풀이 2>
def hide_numbers(s):
  return '*' * (len(s) - 4) + s[-4:]

print("결과 : " + hide_numbers('01033334444'))


# *문제 응용*
# <핸드폰 뒷 4자리만 *로 바꾸기>
# def solution(phone_number):
#     answer = ''
#     list = []
#     for i in phone_number:
#         list.append(i)
#     list.reverse()
#     for j in range(0, 4):
#         list[j] = '*'
#     # return list
#     list.reverse()
#     answer = ''.join(list)
#     return answer
