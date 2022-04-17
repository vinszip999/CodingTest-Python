# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# <나의 풀이 1>
def solution(n):
    answer = []
    list1 = []
    for i in str(n):
        list1.append(i)
        answer = sorted(list1, reverse=True)
        answer = [int(i) for i in answer]
    return answer


# <나의 풀이 2>
def solution2(n):
    answer = list(str(n))
    answer.reverse()

    return list(map(int, answer))


n = 12345
print(solution(n))  # [5,4,3,2,1]


# <다른 사람의 풀이 1>
def digit_reverse(n):
    return list(map(int, reversed(str(n))))


n = 12345
print(digit_reverse(n))  # [5,4,3,2,1]


# <다른 사람의 풀이 2>
def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(digit_reverse(12345)))
