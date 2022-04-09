# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

# <나의 풀이>
def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        sum = []
        for j in range(len(arr1[0])):
            sum.append(arr1[i][j] + arr2[i][j])
        answer.append(sum)

    return answer


arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]

print(solution(arr1, arr2))  # [[4,6],[7,9]]


# <다른 사람의 풀이 1>
def sumMatrix(A, B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]))


# <다른 사람의 풀이 2>
def sumMatrix(A, B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] += B[i][j]
    return A


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
