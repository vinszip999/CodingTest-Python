# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.
# 예를 들어 2와 7의 최소공배수는 14가 됩니다.
# 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
# n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
from math import gcd


# <나의 풀이>
def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = (answer * arr[i]) // gcd(answer, arr[i])

    return answer


arr = [2, 6, 8, 14]  # 168
# arr = [1, 2, 3]  # 6
print(solution(arr))


# <다른 사람의 풀이 1>
def solution2(arr):
    def lcm(x, y):
        return x * y // gcd(x, y)

    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]


arr = [2, 6, 8, 14]  # 168
# arr = [1, 2, 3]  # 6
print(solution2(arr))
