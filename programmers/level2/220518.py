# Leo가 본 카펫에서 갈색 격자의 수 brown,
# 노란색 격자의 수 yellow가 매개변수로 주어질 때
# 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# <나의 풀이>
def solution(brown, yellow):
    n = brown + yellow
    for i in range(n, 2, -1):
        if n % i == 0:
            a = n // i
            if yellow == (i - 2) * (a - 2):
                return [i, a]


brown = 10
yellow = 2  # [4, 3]
# brown = 8
# yellow = 1  # [3, 3]
# brown = 24
# yellow = 24  # [8, 6]
print(solution(brown, yellow))


# <다른 사람의 풀이 1>
def solution2(brown, yellow):
    for i in range(1, int(yellow ** (1 / 2)) + 1):
        if yellow % i == 0:
            if 2 * (i + yellow // i) == brown - 4:
                return [yellow // i + 2, i + 2]


brown = 10
yellow = 2  # [4, 3]
print(solution2(brown, yellow))

# <다른 사람의 풀이 2>
import math


def solution3(brown, yellow):
    w = ((brown + 4) / 2 + math.sqrt(((brown + 4) / 2) ** 2 - 4 * (brown + yellow))) / 2
    h = ((brown + 4) / 2 - math.sqrt(((brown + 4) / 2) ** 2 - 4 * (brown + yellow))) / 2
    return [w, h]


brown = 10
yellow = 2  # [4, 3]
print(solution3(brown, yellow))
