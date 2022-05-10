# 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다.
# str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
# 예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

# <나의 풀이>
def solution(s):
    num_list = []  # s 문자열에서 공백을 제거하고 정수형으로 바꾼 배열
    mm_list = []  # 최대값과 최소값이 들어있는 배열

    s_num = s.split()  # 문자열을 공백 기준으로 나눠서 s_num에 대입

    for i in s_num:  # s_num에서 요소 하나씩 꺼내기
        num_list.append(int(i))  # i를 정수형으로 바꿔서 num_list 배열에 추가

    max_num = max(num_list)  # 최대값을 구하는 max 함수를 이용해서 num_list 배열에서 최대값을 구한 후 max_num에 대입
    min_num = min(num_list)  # 최소값을 구하는 min 함수를 이용해서 num_list 배열에서 최소값을 구한 후 min_num에 대입

    mm_list.append(min_num)  # mm_list 배열에 최소값 추가
    mm_list.append(max_num)  # mm_list 배열에 최대값 추가

    result = list(map(str, mm_list))  # 정수형 mm_list 배열을 문자형 배열로 변환 후, result에 대입

    return " ".join(result)  # result 배열을 각 문자 사이에 공백 추가한 후, 합쳐서 return


# s = "1 2 3 4"  # "1 4"
s = "-1 -2 -3 -4"  # "-4 -1"
# s = "-1 -1"  # "-1 -1"

print(solution(s))


# <다른 사람의 풀이 1>
def solution2(s):
    s = list(map(int, s.split()))
    return str(min(s)) + " " + str(max(s))


s = "-1 -2 -3 -4"  # "-4 -1"
print(solution2(s))


# <다른 사람의 풀이 2>
def solution3(s):
    s_list = s.split(" ")
    n = [int(i) for i in s_list]
    n.sort()

    return str(n[0]) + " " + str(n[len(n) - 1])


s = "-1 -2 -3 -4"  # "-4 -1"
print(solution3(s))


# <다른 사람의 풀이 3>
def solution4(s):
    il = sorted([int(c) for c in s.split(' ')])
    answer = ' '.join([str(il[0]), str(il[len(il) - 1])])
    return answer


s = "-1 -2 -3 -4"  # "-4 -1"
print(solution4(s))
