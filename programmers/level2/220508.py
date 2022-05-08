# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다.
# 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때,
# 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# <나의 풀이>
from itertools import permutations


def decimal(num):
    if num == 0 or num == 1:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    nums = set()

    for i in range(1, len(numbers) + 1):
        nums |= set(map(''.join, permutations(numbers, i)))
    nums = set(map(int, nums))

    for j in nums:
        if decimal(j):
            answer += 1
    return answer


numbers = "17"
print(solution(numbers))  # 3


# <다른 사람의 풀이 1>
def solution2(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)


numbers = "17"
print(solution2(numbers))  # 3

# <다른 사람의 풀이 2>
primeSet = set()


def isPrime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def makeCombinations(str1, str2):
    if str1 != "":
        if isPrime(int(str1)):
            primeSet.add(int(str1))

    for i in range(len(str2)):
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])


def solution3(numbers):
    makeCombinations("", numbers)

    answer = len(primeSet)

    return answer


numbers = "17"
print(solution3(numbers))  # 3
