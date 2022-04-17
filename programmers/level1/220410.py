# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.
import math


# <나의 풀이>
def solution(n):
    answer = 0
    sqrt1 = math.sqrt(n)
    if sqrt1 == int(sqrt1):
        answer = math.trunc((sqrt1 + 1) ** 2)
    else:
        answer = -1
    return answer


n = 121
print(solution(n))  # 144


# <다른 사람의 풀이 1>
def nextSqure1(n):
    sqrt = n ** (1 / 2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'


# <다른 사람의 풀이 2>
def nextSqure2(n):
    return n == int(n ** .5) ** 2 and int(n ** .5 + 1) ** 2 or 'no'


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure2(121)))


# <다른 사람의 풀이 3>
def nextSqure3(n):
    from math import sqrt
    return "no" if sqrt(n) % 1 else (sqrt(n) + 1) ** 2


# <다른 사람의 풀이 4>
def solution2(n):
    # n이 양의 정수의 제곱인가?
    num = math.sqrt(n)
    return (num + 1) ** 2 if num == int(num) else -1
