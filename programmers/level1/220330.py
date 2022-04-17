'''
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
'''


def solution(answers):
    answer = []
    person1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    sum1 = 0
    sum2 = 0
    sum3 = 0

    while (True):
        for i in range(0, len(answers)):
            if person1[i] == answers[i] and person2[i] == answers[i] and person3[i] == answers[i]:
                sum1 += 1
                sum2 += 1
                sum3 += 1
            else:
                if person1[i] == answers[i] and person2[i] == answers[i]:
                    sum1 += 1
                    sum2 += 1
                elif person1[i] == answers[i] and person3[i] == answers[i]:
                    sum1 += 1
                    sum3 += 1
                elif person2[i] == answers[i] and person3[i] == answers[i]:
                    sum2 += 1
                    sum3 += 1
                else:
                    if person1[i] == answers[i]:
                        sum1 += 1
                    elif person2[i] == answers[i]:
                        sum2 += 1
                    elif person3[i] == answers[i]:
                        sum3 += 1

        if sum2 < sum1 > sum3:
            answer.append(1)

        elif sum1 < sum2 > sum3:
            answer.append(2)

        elif sum1 < sum3 > sum2:
            answer.append(3)

        else:
            if sum1 == sum2 == sum3:
                answer.extend([1, 2, 3])
            else:
                if sum1 == sum2:
                    answer.extend([1, 2])

                elif sum1 == sum3:
                    answer.extend([1, 3])

                elif sum2 == sum3:
                    answer.extend([2, 3])
        break

    return answer


answers = [1, 3, 2, 4, 2]
print(solution(answers))
