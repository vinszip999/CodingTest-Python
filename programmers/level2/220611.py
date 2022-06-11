# 효진이는 멀리 뛰기를 연습하고 있습니다. 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다.
# 칸이 총 4개 있을 때, 효진이는
# (1칸, 1칸, 1칸, 1칸)
# (1칸, 2칸, 1칸)
# (1칸, 1칸, 2칸)
# (2칸, 1칸, 1칸)
# (2칸, 2칸)
# 의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다.
# 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내,
# 여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요.
# 예를 들어 4가 입력된다면, 5를 return하면 됩니다.

# <나의 풀이>
def solution(n):
    if n < 3:
        return n
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 2
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]
    return d[n] % 1234567


n = 4
print(solution(n))  # 5


# n = 3
# print(solution(n))  # 3


# <다른 사람의 풀이 1>
def jumpCase(num):
    a, b = 1, 2
    for i in range(2, num):
        a, b = b, a + b
    return b


print(jumpCase(4))


# <다른 사람의 풀이 2>
def jumpCase2(num):
    answer = 0
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return jumpCase(num - 1) + jumpCase(num - 2)


print(jumpCase2(4))
