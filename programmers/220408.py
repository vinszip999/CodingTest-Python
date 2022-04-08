# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

# <나의 풀이 1>
def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)
        else:  # 나누어떨어지지 않는 수라면
            answer.append(-1)

    for i in range(0, len(answer) - 1):
        for j in range(0, len(answer) - 1):
            if answer[j] == -1:
                # answer.pop(answer[j])  # -1을 리턴하기 때문에 사용x
                del answer[j]

    return sorted(answer)


arr = [5, 9, 7, 10]
divisor = 5

print(solution(arr, divisor))  # [5, 10]


# <나의 풀이 2>
def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if len(answer) == 0:
        answer.append(-1)

    return sorted(answer)


# arr = [5, 9, 7, 10]
# divisor = 5

# arr = [2, 36, 1, 3]
# divisor = 1

arr = [3, 2, 6]
divisor = 10

print(solution(arr, divisor))  # [5, 10]


# <다른 사람의 풀이 1>
def solution(arr, divisor): return sorted([n for n in arr if n % divisor == 0]) or [-1]


arr = [3, 2, 6]
divisor = 10

print(solution(arr, divisor))


# <다른 사람의 풀이 2>
def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    arr.sort()
    return arr if len(arr) != 0 else [-1]


arr = [3, 2, 6]
divisor = 10

print(solution(arr, divisor))
