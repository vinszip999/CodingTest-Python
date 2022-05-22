# 2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

# <나의 풀이>
def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]

    for i in range(len(arr1)):
        temp = [0] * len(arr2[0])
        for j in range(len(arr1[0])):
            for k in range(len(arr2[0])):
                temp[k] += arr1[i][j] * arr2[j][k]
        answer[i] = temp
    return answer


arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1, arr2))  # [[15, 15], [15, 15], [15, 15]]


# arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
# arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
# print(solution(arr1, arr2))  # [[22, 22, 11], [36, 28, 18], [29, 20, 14]]


# <다른 사람의 풀이 1>
def productMatrix(A, B):
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]


a = [[1, 4], [3, 2], [4, 1]]
b = [[3, 3], [3, 3]]
print("결과 : {}".format(productMatrix(a, b)))


# <다른 사람의 풀이 2>
def productMatrix2(A, B):
    answer = []
    for y1 in range(len(A)):
        a = []
        for x2 in range(len(B[0])):
            n = 0
            for x1 in range(len(A[0])):
                n += A[y1][x1] * B[x1][x2]
            a.append(n)
        answer.append(a)
    return answer


a = [[1, 4], [3, 2], [4, 1]]
b = [[3, 3], [3, 3]]
print("결과 : {}".format(productMatrix2(a, b)))
