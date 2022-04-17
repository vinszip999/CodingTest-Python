# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,
# commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때
# 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# <나의 풀이>
def solution(array, commands):
    answer = []

    for a in commands:
        i = a[0]
        j = a[1]
        k = a[2]

        if i == j:
            answer.append(array[i - 1])
            continue

        n = array[i - 1:j]
        n.sort()

        result = n[k - 1]
        answer.append(result)

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))


# <다른 사람의 풀이 1>
def solution2(array, commands):
    return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))


# <다른 사람의 풀이 2>
def solution3(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(list(sorted(array[i - 1:j]))[k - 1])
    return answer
