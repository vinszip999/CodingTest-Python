# H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다.
# 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.
# 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고
# 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때,
# 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

# <나의 풀이>
def solution(citations):
    answer = 0
    citations.sort()
    for i in range(0, len(citations)):
        if (citations[i] >= len(citations) - i):
            answer = max(answer, len(citations) - i)

    return answer


citations = [3, 0, 6, 1, 5]
print(solution(citations))  # 3


# <다른 사람의 풀이 1>
def solution2(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


citations = [3, 0, 6, 1, 5]
print(solution2(citations))  # 3


# <다른 사람의 풀이 2>
def solution3(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l - i:
            return l - i
    return 0


citations = [3, 0, 6, 1, 5]
print(solution3(citations))  # 3
