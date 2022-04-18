# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
#
# 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다.
# 이 중 가장 큰 숫자는 94 입니다.
#
# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다.
# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중
# 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

# <나의 풀이>
def solution(number, k):
    answer = []  # stack

    for n in number:
        while k > 0 and answer and answer[-1] < n:
            answer.pop()
            k -= 1
        answer.append(n)

    return ''.join(answer[:len(answer) - k])


number = "1924"
k = 2
print(solution(number, k))  # "94"


# number = "1231234"
# k = 3
# print(solution(number, k))  # "3234"
# number = "4177252841"
# k = 4
# print(solution(number, k))  # "775841"


# <다른 사람의 풀이 1>
def solution2(number, k):
    # stack에 입력값을 순서대로 삽입
    stack = [number[0]]
    for num in number[1:]:
        # 들어오는 값이 stack 값보다 크면, 기존의 값을 제거하고 새로운 값으로 바꿈
        # 참고 : len(stack) > 0 == stack
        while len(stack) > 0 and stack[-1] < num and k > 0:
            # 값을 한개 빼서 k는 1이 제거
            k -= 1
            # 내부의 값을 제거
            stack.pop()
        # 새로운 값을 삽입
        stack.append(num)
    # 만일 충분히 제거하지 못했으면 남은 부분은 단순하게 삭제
    # 이렇게 해도 되는 이유는 이미 큰 수부터 앞에서 채워넣었기 때문
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


number = "1924"
k = 2
print(solution2(number, k))  # "94"


# <다른 사람의 풀이 2>
def solution3(number, k):
    answer = ''
    stk = []
    for i in number:
        while stk and stk[-1] < i and k > 0:
            k -= 1
            stk.pop()
        stk.append(i)
    return "".join(stk[:len(stk) - k])


number = "1924"
k = 2
print(solution3(number, k))  # "94"
