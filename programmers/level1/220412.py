# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
# 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
# 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

# <나의 풀이>
def solution(x):
    answer = True
    sum = 0
    list1 = list(str(x))
    for i in list(map(int, list1)):
        sum += i
    if x % sum == 0:
        answer = True
    else:
        answer = False
    return answer


x = 12
print(solution(x))  # true


# <다른 사람의 풀이 1>
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))


# <다른 사람의 풀이 2>
def Harshad2(n):
    # n은 하샤드 수 인가요?
    st = str(n)
    a = 0
    for i in range(len(st)):
        a += int(st[i])

    return True if n % a == 0 else False


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad2(18))
