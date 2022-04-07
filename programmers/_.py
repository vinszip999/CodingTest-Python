# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다.
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

# ord() : 문자의 아스키 코드 값을 돌려주는 함수
# chr() : 아스키 코드를 입력받아, 문자를 출력해주는 함수

# <나의 풀이 1>
def solution(s, n):
    answer = ''
    list1 = []

    for i in s:
        list1.append(ord(i))

    for j in range(len(list1)):
        if list1[j] == 90:
            list1[j] = 65 + (n - 1)
        elif list1[j] == 122:
            list1[j] = 97 + (n - 1)
        else:
            if list1[j] == 32:
                list1[j] = 32
            else:
                list1[j] += n

    for c in range(len(list1)):
        list1[c] = chr(list1[c])

    answer = ''.join(list1)

    return answer


# s = "AB"
# s = "z"
s = "a B z"
n = 4
print(solution(s, n))


# <나의 풀이 2>
def solution(s, n):
    answer = ''

    list1 = list(s)
    for i in range(len(s)):
        if list1[i].isupper():
            list1[i] = chr((ord(list1[i]) - ord('A') + n) % 26 + ord('A'))
        elif list1[i].islower():
            list1[i] = chr((ord(list1[i]) - ord('a') + n) % 26 + ord('a'))

    answer = ''.join(list1)

    return answer


s = 'zZyY'
n = 4
print(solution(s, n))


# <다른 사람의 풀이 1>
def caesar(s, n):
    lower_list = "abcdefghijklmnopqrstuvwxyz"
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = []

    for i in s:
        if i == " ":
            result.append(" ")
        elif i.islower() is True:
            new_ = lower_list.find(i) + n
            result.append(lower_list[new_ % 26])
        else:
            new_ = upper_list.find(i) + n
            result.append(upper_list[new_ % 26])

    return "".join(result)


s = 'zZyY'
n = 4
print(solution(s, n))


# <다른 사람의 풀이 2>
def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        else:
            if 65 <= ord(i) <= 90:
                if 91 <= ord(i) + n:
                    answer += chr(ord(i) + n - 26)
                else:
                    answer += chr(ord(i) + n)
            else:
                if ord(i) + n > 122:
                    answer += chr(ord(i) + n - 26)
                else:
                    answer += chr(ord(i) + n)

    return answer


s = 'zZyY'
n = 4
print(solution(s, n))
