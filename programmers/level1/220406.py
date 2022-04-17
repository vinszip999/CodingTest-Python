# 함수 solution은 정수 n을 매개변수로 입력받습니다.
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
# 예를들어 n이 118372면 873211을 리턴하면 됩니다.


# <나의 풀이>
def solution(n):
    answer = 0
    list1 = list(str(n))  # string형으로 바꾼 n을 배열로 바꿔서 list1 배열에 넣기
    result = sorted(list1, reverse=True)  # list1 배열을 내림차순으로 정렬하여 result에 넣기
    answer = int(''.join(result))  # result 배열을 문자열로 바꾸고 int형으로 변환 시켜서 answer에 넣어주기
    return answer


n = 118372
print(solution(n))


# <다른 사람의 풀이 1>
def solution(n):
    s = str(n)
    answer = sorted(s, reverse=True)
    answer = int(''.join(answer))

    return answer
