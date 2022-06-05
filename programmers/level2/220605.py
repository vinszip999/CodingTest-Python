# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
# 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

# <나의 풀이>
def solution(s):
    answer = ''
    s1 = s.split(' ')
    for i in range(len(s1)):
        s1[i] = s1[i].capitalize()
    answer = ' '.join(s1)
    return answer


s = "3people unFollowed me"  # "3people Unfollowed Me"
# s = "for the last week"  # "For The Last Week"
print(solution(s))


# <다른 사람의 풀이 1>
def Jaden_Case(s):
    return s.title()


s = "3people unFollowed me"  # "3people Unfollowed Me"
# s = "for the last week"  # "For The Last Week"
print(Jaden_Case(s))


# <다른 사람의 풀이 2>
def Jaden_Case2(s):
    # 함수를 완성하세요
    answer = []
    for i in range(len(s.split())):
        answer.append(s.split()[i][0].upper() + s.split()[i].lower()[1:])
    return " ".join(answer)


s = "3people unFollowed me"  # "3people Unfollowed Me"
# s = "for the last week"  # "For The Last Week"
print(Jaden_Case2(s))
