# 스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

# 예를 들어 스파이가 가진 옷이 아래와 같고
# 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면
# 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.
"""
종류	이름
얼굴	동그란 안경, 검정 선글라스
상의	파란색 티셔츠
하의	청바지
겉옷	긴 코트
"""


# 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때
# 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.


# <나의 풀이>
def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] = 1

    count = 1
    for i in answer.values():
        count *= (i + 1)
    return count - 1


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]  # 5
# clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]  # 3
print(solution(clothes))


# <다른 사람의 풀이 1>
def solution2(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]  # 5
print(solution2(clothes))

# <다른 사람의 풀이 2>
import collections
from functools import reduce


def solution(c):
    return reduce(lambda x, y: x * y, [a + 1 for a in collections.Counter([x[1] for x in c]).values()]) - 1


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]  # 5
print(solution2(clothes))
