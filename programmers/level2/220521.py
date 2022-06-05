# 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.
# 예를들어 아래와 같이 이어집니다.
# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5

# 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

# <나의 풀이>
def solution(n):
    answer = [0, 1]
    for i in range(2, n + 1):
        answer.append((answer[i - 1] + answer[i - 2]) % 1234567)

    return answer[-1]


n = 3  # 2
# n = 5  # 5
print(solution(n))


# <다른 사람의 풀이 1>
def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a + b
    return a


print(fibonacci(3))


# <다른 사람의 풀이 2>
def fibonacci2(num):
    answer = [0, 1]

    for i in range(2, num + 1):
        answer.append(answer[i - 1] + answer[i - 2])

    return answer[-1]


print(fibonacci2(3))