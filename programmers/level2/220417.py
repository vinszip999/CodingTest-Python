# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# <나의 풀이>
def solution(numbers):
    num = list(map(str, numbers))
    num.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(num)))


numbers = [6, 10, 2]
print(solution(numbers))  # "6210"

# numbers = [3, 30, 34, 5, 9]
# print(solution(numbers))  # "9534330"


# <다른 사람의 풀이 1>
import functools


def comparator(a, b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))  # t1이 크다면 1  // t2가 크다면 -1  //  같으면 0


def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer


numbers = [6, 10, 2]
print(solution(numbers))  # "6210"


# <다른 사람의 풀이 2>
def solution(n):
    return str(int("".join(sorted(map(str, n), key=lambda x: (x * 4), reverse=True))))


numbers = [6, 10, 2]
print(solution(numbers))  # "6210"
