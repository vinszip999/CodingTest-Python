# 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

# <나의 풀이>
def solution(s):
    answer = int(s)
    return answer

# <다른 사람의 풀이>
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"))
