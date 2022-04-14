# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

# <나의 풀이 1>
def solution(s):
    list1 = s.split(' ')  # ' ' 단위로 자르기 (*꼭 들어가야 함*)
    for i in range(len(list1)):
        list2 = list(list1[i])
        for j in range(len(list2)):
            if j % 2 == 0:
                list2[j] = list2[j].upper()
            else:  # j % 2 == 1
                list2[j] = list2[j].lower()
        list1[i] = ''.join(list2)

    answer = ' '.join(list1)
    return answer


s = "try hello world"  # "TrY HeLlO WoRlD"
print(solution(s))


# <나의 풀이 2> 잘못된 버전
# *문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야하기 떄문*
def solution2(s):
    list1 = []
    for i in range(len(s)):
        if i % 2 == 0:
            list1.append(s[i].upper())
        else:  # j % 2 == 1
            list1.append(s[i])

    answer = ''.join(list1)
    return answer


s = "try hello world"  # "TrY HeLlO WoRlD"
print(solution2(s))


# <다른 사람의 풀이 1>
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))


s = "try hello world"  # "TrY HeLlO WoRlD"
print(toWeirdCase(s))


# <다른 사람의 풀이 2>
def solution3(s):
    answer = ''
    arr = s.split(' ')
    for s in arr:
        for i, x in enumerate(s):
            answer += x.upper() if i % 2 == 0 else x.lower()
        answer += ' '
    return answer[:-1]


s = "try hello world"  # "TrY HeLlO WoRlD"
print(solution3(s))
