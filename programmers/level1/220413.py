# 1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될때까지 다음 작업을 반복하면,
# 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.

# 1-1. 입력된 수가 짝수라면 2로 나눕니다.
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.

# // : 몫만 가져오는 산술 연산자

# <나의 풀이>
def solution(num):
    answer = 0

    while True:
        if num != 1:
            if answer < 500:
                if num % 2 == 0:
                    num = num / 2
                    answer += 1
                elif num % 2 == 1:
                    num = (num * 3) + 1
                    answer += 1
            else:  # answer >= 500:
                return -1
        else:  # num이 1이 맞다면
            break

    return answer


num = 6  # 8
# num = 16  # 4
# num = 626331  # -1

print(solution(num))


# <다른 사람의 풀이 1>
def collatz(num):
    answer = 0
    while answer < 500:
        answer += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num = (num * 3) + 1
        if num == 1:
            break
    if answer == 500:
        answer = -1

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(1126015))


# <다른 사람의 풀이 2>
def collatz2(num):
    answer = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2  # // : 몫만 가져오는 산술 연산자
            answer = answer + 1
        else:
            num = num * 3 + 1
            answer = answer + 1
    if answer < 500:
        return answer
    else:
        return (-1)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz2(6))
